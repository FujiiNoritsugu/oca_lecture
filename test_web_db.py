from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fujii:dummy_pass@localhost:5432/fujii'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)

    def __init__(self, name):
        self.name = name

db.create_all()

while True:
    name = input("type your name:")
    p = person(name)
    db.session.add(p)
    db.session.commit()

