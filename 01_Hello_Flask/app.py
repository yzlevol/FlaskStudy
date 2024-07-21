from flask import Flask, url_for, render_template
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
db = SQLAlchemy(app)  # 初始化扩展，传入程序实例app


# # 配置数据库的连接信息
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
# 对于SQLite, [sqlite:////数据库文件的绝对路径]

# 创建数据库模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(20))  # Name


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    title = db.Column(db.String(60))  # Title
    year = db.Column(db.String(4))  # Year


@app.cli.command()  # 注册为命令,可以传入name参数来自定义命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息


@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()

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

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')


@app.route('/hello')
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


# @app.route('/index')
# def index():
#     return render_template('index.html', name=name, movies=movies)


@app.route('/')
@app.route('/index')
def index():
    user = User.query.first()  # 读取用户记录
    movies = Movie.query.all()  # 读取所有电影记录
    return render_template('index.html', user=user, movies=movies)


