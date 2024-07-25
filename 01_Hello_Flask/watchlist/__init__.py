import os
import sys

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# 系统平台判断
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# 创建Flask应用实例
# 配置数据库的连接信息
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
# 对于SQLite, [sqlite:////数据库文件的绝对路径]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
app.config['SECRET_KEY'] = 'my_dev_env_secret_key'  # 等同于 app.secret_key = 'dev'
db = SQLAlchemy(app)  # 初始化扩展，传入程序实例app

# 实例化扩展类
login_manager = LoginManager(app)
login_manager.login_message = 'Please login to access this page.'


@login_manager.user_loader
def load_user(user_id):
    from watchlist.models import User
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = 'login'


@app.context_processor
def inject_user():
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)


from watchlist import views, errors, commands

# import os
# import sys
# import click
# from flask import Flask, flash, redirect, render_template, request, url_for
# from flask_sqlalchemy import SQLAlchemy
# from markupsafe import escape
# from werkzeug.security import check_password_hash, generate_password_hash
# from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
