# Flask Encrypted File App

This project is a Flask application that allows users to upload files, which are then encrypted and stored securely. Users can also download and decrypt these files. 

## Project Structure

```
flask_encrypted_file_app
├── app.py                # Main application file
├── key.key               # Encryption key for file encryption/decryption
├── requirements.txt      # List of dependencies
├── uploads               # Directory for storing uploaded and encrypted files
├── templates
│   └── index.html       # HTML template for the upload form
├── .gitignore            # Files and directories to ignore in Git
└── README.md             # Project documentation
```

## Requirements

To run this project, you need to have Python installed. You can install the required packages using the following command:

```
pip install -r requirements.txt
```

## Setup

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Generate an encryption key using the following Python code:

   ```python
   from cryptography.fernet import Fernet
   key = Fernet.generate_key()
   with open("key.key", "wb") as key_file:
       key_file.write(key)
   ```

4. Make sure the `uploads` directory exists. If not, create it.

## Running the Application

To start the Flask application, run the following command:

```
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

- Navigate to the home page to upload a file.
- After uploading, the file will be encrypted and stored in the `uploads` directory.
- You can implement additional functionality to download and decrypt the files as needed.

## License

This project is licensed under the MIT License.