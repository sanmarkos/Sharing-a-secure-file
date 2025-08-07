# Flask Encrypted File App

This project is a Flask application that allows users to upload files, which are then encrypted and stored securely. Users can also download and decrypt these files.

## Project Structure

```
Sharing-a-secure-file/
├── app.py
├── key.key
├── requirements.txt
├── uploads/
├── templates/
│   ├── index.html
│   └── login.html
├── static/
│   └── style.css
├── README.md
└── .gitignore
```

## How to Clone the Project

To get started, clone the repository to your local machine:

```
git clone https://github.com/sanmarkos/Sharing-a-secure-file.git
cd Sharing-a-secure-file
```

## How to Run

1. Install dependencies:
   ```
pip install flask cryptography
```

2. Generate a Fernet key:
   ```python
   from cryptography.fernet import Fernet
   key = Fernet.generate_key()
   with open("key.key", "wb") as key_file:
       key_file.write(key)
   ```

3. Start the app:
   ```
   python app.py
   ```

4. Open your browser at `http://127.0.0.1:5000`

**Default login credentials:**
- Username: `admin`
- Password: `password`

## Usage

- Navigate to the home page to upload a file.
- After uploading, the file will be encrypted and stored in the `uploads` directory.
- You can implement additional functionality to download and decrypt the files as needed.

## License

This project is licensed under the MIT License.
