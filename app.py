from flask import Flask, render_template, request, jsonify, send_from_directory
import subprocess
import sys
import os

app = Flask(__name__)


ATTENDANCE_FOLDER = "Attendance"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/attendance')
def attendance_page():

    files = [f for f in os.listdir(ATTENDANCE_FOLDER) if f.endswith('.csv')]
    return render_template('attendance.html', files=files)


@app.route('/take-attendance', methods=['POST'])
def take_attendance():
    try:
        result = subprocess.run([sys.executable, 'main.py'], capture_output=True, text=True)
        return jsonify({"status": "success", "output": result.stdout, "error": result.stderr})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})


@app.route('/download/<filename>')
def download_file(filename):
    try:
       
        return send_from_directory(ATTENDANCE_FOLDER, filename, as_attachment=True)
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
