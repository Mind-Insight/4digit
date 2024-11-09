import cv2
import os

def extract_faces_from_video(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    frame_id = 0
    os.makedirs(output_folder, exist_ok=True)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for i, (x, y, w, h) in enumerate(faces):
            face = frame[y:y+h, x:x+w]
            face_path = os.path.join(output_folder, f"frame_{frame_id}_face_{i}.jpg")
            cv2.imwrite(face_path, face)
        
        frame_id += 1

    cap.release()

# Пример использования
extract_faces_from_video("dataset/ved.mp4.mp4", "output_faces")
