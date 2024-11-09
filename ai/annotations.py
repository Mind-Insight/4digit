import pickle


def load_pkl_file(file_path):
    with open(file_path, "rb") as f:
        data = pickle.load(f, encoding="latin1")
    return data


annotations = load_pkl_file("dataset/annotation_training.pkl")
