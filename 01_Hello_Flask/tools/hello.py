from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello Flask! Today is 2024.7.19."
