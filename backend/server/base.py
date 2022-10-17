from flask import Flask, send_file
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

