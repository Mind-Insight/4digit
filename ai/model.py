from pytorch_lightning import Trainer
import os
import cv2
import torch
import numpy as np
import pytorch_lightning as pl
from torch import nn
from torch.utils.data import Dataset, DataLoader
import pickle


VIDEO_DIR = "videos"
BATCH_SIZE = 8
NUM_CLASSES = 5


def load_pkl_file(file_path):
    with open(file_path, "rb") as f:
        data = pickle.load(f, encoding="latin1")
    return data


annotations = load_pkl_file("dataset/annotation_training.pkl")
transcriptions = load_pkl_file("dataset/transcription_training.pkl")
parse = {}

for key in annotations:
    for key1 in annotations[key]:
        parse[key1] = []
    break

for key in annotations:
    for key1 in annotations[key]:
        if key == "interview":
            continue
        parse[key1].append(annotations[key][key1])

for key in transcriptions:
    parse[key].append(transcriptions[key])


class VideoPersonalityDataset(Dataset):
    def __init__(self, video_dir, parsed_data):
        self.video_dir = video_dir
        self.parsed_data = parsed_data
        self.keys = list(parsed_data.keys())

    def __len__(self):
        return len(self.parsed_data)

    def __getitem__(self, idx):
        key = self.keys[idx]
        personality_values = self.parsed_data[key][:5]
        text = self.parsed_data[key][5] if len(self.parsed_data[key]) > 5 else ""
        video_path = os.path.join(self.video_dir, key)
        video_features = self.extract_video_features(video_path)
        personality_tensor = torch.tensor(personality_values, dtype=torch.float).to(
            "cuda" if torch.cuda.is_available() else "cpu"
        )
        return video_features, text, personality_tensor

    def extract_video_features(self, video_path):
        cap = cv2.VideoCapture(video_path)
        frames = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (224, 224))
            frames.append(frame)

        cap.release()
        frames = np.array(frames)
        if len(frames) == 0:
            return torch.zeros(1, 3, 224, 224).to(
                "cuda" if torch.cuda.is_available() else "cpu"
            )
        video_tensor = torch.tensor(frames).permute(0, 3, 1, 2).float()
        return (
            video_tensor.mean(dim=0)
            .unsqueeze(0)
            .to("cuda" if torch.cuda.is_available() else "cpu")
        )


class PersonalityModel(pl.LightningModule):
    def __init__(self):
        super(PersonalityModel, self).__init__()
        # посмотреть готовую модель вместо Linear(готовые архитектуры)
        self.fc_video = nn.Linear(224 * 224 * 3, 512)
        self.fc_text = nn.Linear(768, 512)
        self.fc_out = nn.Linear(512 + 512, NUM_CLASSES)

    def forward(self, video_features, text_features):
        video_outputs = self.fc_video(video_features.view(video_features.size(0), -1))
        text_outputs = torch.zeros(video_outputs.size(0), 512).to(self.device)
        combined = torch.cat((video_outputs, text_outputs), dim=1)
        output = self.fc_out(combined)
        return output

    def training_step(self, batch, batch_idx):
        video_features, text_inputs, personality = batch
        video_features = video_features.to(self.device)
        personality = personality.to(self.device)
        outputs = self.forward(video_features, text_inputs)
        loss = nn.MSELoss()(outputs, personality)
        self.log("train_loss", loss)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-4)


if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dataset = VideoPersonalityDataset(VIDEO_DIR, parse)
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)
    for batch in dataloader:
        print("Batch загружен:", batch)
        break

    model = PersonalityModel().to(device)
    trainer = Trainer(
        max_epochs=10,
        accelerator="gpu" if torch.cuda.is_available() else "cpu",
        devices=1,
    )
    trainer.fit(model, dataloader)
    torch.save(model.state_dict(), "personality_model.pth")
    print("Модель сохранена в personality_model.pth")
