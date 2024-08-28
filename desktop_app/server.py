from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from gui import app_instance  # Ensure this import is correct
from utils import get_local_ip
import os
import time

app = Flask(__name__)
CORS(app)

# Configure the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dictionary to store filenames and their upload timestamps
uploaded_files = {}

@app.route('/get_ip', methods=['GET'])
def get_ip():
    ip = get_local_ip()
    return jsonify({'ip': ip})

@app.route('/next', methods=['GET'])
def next_slide():
    app_instance.next_slide()
    return jsonify({'status': 'ok'})

@app.route('/prev', methods=['GET'])
def prev_slide():
    app_instance.prev_slide()
    return jsonify({'status': 'ok'})

@app.route('/show_screen', methods=['GET'])
def show_screen():
    app_instance.show_screen()
    return jsonify({'status': 'ok'})

@app.route('/upload_presentation', methods=['POST'])
def upload_presentation():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = 'presentation.pdf'  # Fixed filename to ensure overwrite
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        timestamp = time.time()
        uploaded_files[filename] = timestamp
        return jsonify({'status': 'ok', 'filename': filename, 'timestamp': timestamp}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf'}

def run_flask_app():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run_flask_app()