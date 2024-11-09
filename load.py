import os
import cv2
import torch
import numpy as np
from moviepy.editor import VideoFileClip
import speech_recognition as sr
from torch import nn
import pytorch_lightning as pl


NUM_CLASSES = 5
class PersonalityModel(pl.LightningModule):
    def __init__(self):
        super(PersonalityModel, self).__init__()
        self.fc_video = nn.Linear(224 * 224 * 3, 512)
        self.fc_text = nn.Linear(768, 512)
        self.fc_out = nn.Linear(512 + 512, NUM_CLASSES)

    def forward(self, video_features, text_features):
        video_outputs = self.fc_video(video_features.view(video_features.size(0), -1))
        text_outputs = text_features  # Заглушка для текстовых фич
        combined = torch.cat((video_outputs, text_outputs), dim=1)
        output = self.fc_out(combined)
        return output


def extract_video_features(video_path):
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
        return torch.zeros(1, 3, 224, 224)
    video_tensor = torch.tensor(frames).permute(0, 3, 1, 2).float()
    return video_tensor.mean(dim=0).unsqueeze(0)


def extract_audio_text(video_path):
    audio_path = "extracted_audio.wav"
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)

    return text


def preprocess_text_features(text):
    return torch.zeros(1, 512)



def load_trained_model(model_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = PersonalityModel()
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    model.to(device)
    return model


def analyze_video(video_path, model_path):
    model = load_trained_model(model_path)
    video_features = extract_video_features(video_path).to(model.device)
    text = extract_audio_text(video_path)
    text_features = preprocess_text_features(text).to(model.device)

    with torch.no_grad():
        output = model(video_features, text_features)

    return output.cpu().numpy(), text


if __name__ == "__main__":
    video_path = "test/video.mp4"
    model_path = "personality_model.pth"

    personality_traits, transcription = analyze_video(video_path, model_path)
    print("Тип личности (OCEAN):", personality_traits)
    print("Распознанный текст:", transcription)
