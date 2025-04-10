from flask import Flask, render_template, request, jsonify
import os
from posture_blink_detection import process_video

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['video']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    posture_result, blink_rate = process_video(filepath)
    response = {
        'posture': posture_result,
        'blinks_per_minute': blink_rate
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
