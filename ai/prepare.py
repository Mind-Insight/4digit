def extract_video_features(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (224, 224))  # Преобразуем кадры к размеру 224x224
        frames.append(frame)

    cap.release()
    frames = np.array(frames)
    if len(frames) == 0:
        return torch.zeros(1, 3, 224, 224).to(device)

    video_tensor = torch.tensor(frames).permute(0, 3, 1, 2).float()
    return video_tensor.mean(dim=0).unsqueeze(0).to(device)
