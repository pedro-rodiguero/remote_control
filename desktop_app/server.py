from flask import Flask, jsonify
from flask_cors import CORS
from gui import app_instance
from utils import get_local_ip

app = Flask(__name__)
CORS(app)

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

def run_flask_app():
    app.run(host='0.0.0.0', port=5000)