import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os
import tensorflow as tf
from fer import FER


# Обнаружение лиц и эмоций с помощью FER
def detect_faces_and_emotions(video_path):
    # Загрузка видео
    cap = cv2.VideoCapture(video_path)

    # Модель для распознавания эмоций
    emotion_detector = FER(mtcnn=True)

    results = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Конвертация в RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Распознавание эмоций
        emotions = emotion_detector.detect_emotions(rgb_frame)

        # Обработка результатов
        for result in emotions:
            box = result["box"]
            emotion, score = max(result["emotions"].items(), key=lambda x: x[1])

            # Сохранение результатов
            results.append(
                {"frame": frame, "box": box, "emotion": emotion, "score": score}
            )

            # Отображение
            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f"{emotion} ({score:.2f})",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 0, 0),
                2,
            )

        # Показать кадры
        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return results


# Пусть модель обрабатывает видео
video_path = "dataset/ved.mp4"
results = detect_faces_and_emotions(video_path)

# Сохранение результатов в файл
with open("results.txt", "w") as f:
    for result in results:
        f.write(f"{result['emotion']} - {result['score']}\n")
