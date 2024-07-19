from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/home')
@app.route('/')
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


@app.route('/index')
def index():
    return render_template('index.html', name=name, movies=movies)


name = 'Hyoung'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]
