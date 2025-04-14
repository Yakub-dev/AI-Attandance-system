@app.route('/')
def home():
    return render_template('index.html')

@app.route('/attendance')
def attendance_page():
