from flask import Flask
from flask import url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/home')
@app.route('/')
@app.route('/index')
def hello():
    return ("Hello Flask!2024.7.17"
            "<h1> Hello, World! </h1>"
            "<img src='https://helloflask.com/totoro.gif'>")


@app.route('/user/<name>')
def user_page(name):
    return f"Hello, {escape(name)}!"


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='hyoung'))
    print(url_for('user_page', name='yzlevol'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'
