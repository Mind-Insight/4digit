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
        return torch.zeros(1, 3, 224, 224).to(self.device)
    video_tensor = torch.tensor(frames).permute(0, 3, 1, 2).float() / 255.0
    video_tensor = video_tensor.to(self.device)
    with torch.no_grad():
        video_features = self.resnet(video_tensor)
    return video_features.mean(dim=0).unsqueeze(0)
