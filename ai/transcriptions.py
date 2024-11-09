import pickle


def load_pkl_file(file_path):
    with open(file_path, "rb") as f:
        data = pickle.load(f)
    return data


annotations = load_pkl_file("dataset/transcription_training.pkl")
for key in annotations.keys():
    print(key)
