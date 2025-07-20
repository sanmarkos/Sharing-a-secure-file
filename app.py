from flask import Flask, request, redirect, render_template, send_file, session, url_for, flash
import os
from cryptography.fernet import Fernet
import io

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key!
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)

# Hardcoded credentials for demonstration
USERNAME = "admin"
PASSWORD = "password"

def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.endswith('.enc')]
    return render_template("index.html", files=files)

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    file = request.files['file']
    if file:
        data = file.read()
        encrypted_data = fernet.encrypt(data)
        filename = file.filename + ".enc"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, "wb") as f:
            f.write(encrypted_data)
        return redirect('/')
    return "No file uploaded", 400

@app.route('/download/<filename>', methods=['GET'])
@login_required
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            encrypted_data = f.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        original_filename = filename.replace(".enc", "")
        return send_file(
            io.BytesIO(decrypted_data),
            as_attachment=True,
            download_name=original_filename
        )
    return "File not found!", 404

@app.route('/delete/<filename>', methods=['POST'])
@login_required
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return redirect('/')
    return "File not found!", 404

if __name__ == "__main__":
    app.run(debug=True)