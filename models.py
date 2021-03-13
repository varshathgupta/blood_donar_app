from flask_login import UserMixin
from . import db
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    usersd = db.relationship('Userd',backref='author', lazy=True)


class Userd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    age = db.Column(db.Integer, nullable=False)
    bg = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    address = db.Column(db.Text, nullable=False)
    availablity = db.Column(db.String, nullable=False)
    lastdonation = db.Column(db.DateTime, nullable=False)
    degree = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)