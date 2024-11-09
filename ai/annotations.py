import pickle


def load_pkl_file(file_path):
    with open(file_path, "rb") as f, open("dataset/transcription_training.pkl", "rb") as trans:
        data = pickle.load(f, encoding="latin1")
        data_trans = pickle.load(trans)
    return (data, data_trans)


<<<<<<< HEAD
annotations, transcriptions = load_pkl_file("dataset/annotation_training.pkl")

parse = {}

for key in annotations:
    for key1 in annotations[key]:
        parse[key1] = []
    break

for key in annotations:
    for key1 in annotations[key]:
        if key == 'interview':
            continue
        parse[key1].append(annotations[key][key1])

for key in transcriptions:
    parse[key].append(transcriptions[key])

print(parse)
=======
annotations = load_pkl_file("dataset/annotation_training.pkl")
print(annotations["interview"])
>>>>>>> 73b085efb588b97c9121738fd7cd091d4d000ead
