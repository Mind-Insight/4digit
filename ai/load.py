import torch
from model import PersonalityModel

model_path = "personality_model.pth"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = PersonalityModel().to(device)
model.load_state_dict(torch.load(model_path))
model.eval()
