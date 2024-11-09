from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')  # HTML-файл с формой

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'video' not in request.files:
        return "No file part"
    file = request.files['video']
    if file.filename == '':
        return "No selected file"

    if file:
        # Сохраните видео
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        # При вызове вашей функции для обработки видео и классификации
        result = process_video(file_path)
        return f"Predicted personality type: {result}"

if __name__ == '__main__':
    app.run(debug=True)