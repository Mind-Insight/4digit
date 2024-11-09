import librosa
import numpy as np
from transformers import pipeline


def extract_audio_features(video_path):
    # Извлечение аудио из видео
    audio_path = "temp_audio.wav"
    os.system(f"ffmpeg -i {video_path} -q:a 0 -map a {audio_path}")

    # Извлечение признаков с помощью librosa
    y, sr = librosa.load(audio_path, sr=16000)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs, axis=1)


def extract_text_transcription(video_path):
    # Используем предобученный трансформер для распознавания речи
    speech_to_text = pipeline(
        "automatic-speech-recognition", model="facebook/wav2vec2-large-960h"
    )
    audio_path = "temp_audio.wav"
    os.system(f"ffmpeg -i {video_path} -q:a 0 -map a {audio_path}")
    transcription = speech_to_text(audio_path)
    return transcription["text"]


# Пример использования
audio_features = extract_audio_features("example_video.mp4")
text_transcription = extract_text_transcription("example_video.mp4")
print("Аудио-признаки:", audio_features)
print("Транскрипция:", text_transcription)
