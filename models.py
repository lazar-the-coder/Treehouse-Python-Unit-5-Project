from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db.init_app(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Title", db.String())
    date = db.Column("Date", db.DateTime, default=datetime.datetime.now)
    skills = db.Column("Skills", db.Text)
    description = db.Column("Description", db.Text)
    link = db.Column("Repo Link", db.Text)