from email import message
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def wish():
    message = "This is my first flask project {name}"
    return message.format(name=os.getenv("NAME", "John"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)