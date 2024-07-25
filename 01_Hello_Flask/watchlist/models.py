from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from watchlist import db


# 创建数据库模型
class User(db.Model, UserMixin):
    """
    用户表
    """
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(20))  # Name
    username = db.Column(db.String(20))  # Username
    password_hash = db.Column(db.String(128))  # Password hash

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


# 创建数据库模型
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    title = db.Column(db.String(60))  # Title
    year = db.Column(db.String(4))  # Year
