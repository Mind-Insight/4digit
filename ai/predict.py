def predict_personality(video_path):
    # Извлекаем признаки из видео
    video_features = extract_video_features(video_path)

    # Пропускаем через модель
    with torch.no_grad():  # Выключаем вычисление градиентов для инференса
        output = model(
            video_features, text_features=None
        )  # Подаем None, если текст не используется

    return output


# Путь к видео
video_path = "test/video.mp4"

# Получаем предсказания
output = predict_personality(video_path)

# Печатаем результат
print("Предсказанные черты личности: ", output)
