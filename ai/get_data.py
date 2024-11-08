import pickle

# Загрузка данных из .pkl файла
with open('dataset/transcription_training.pkl', 'rb') as f:
    data = pickle.load(f)

# Печать структуры данных
print(type(data))
print(data.keys() if isinstance(data, dict) else len(data))
