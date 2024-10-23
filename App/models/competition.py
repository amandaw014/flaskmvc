from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .associations_table import *


# Competition model
class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    results = db.relationship('Result', backref='competition', lazy=True)
    students = db.relationship('Student', secondary='student_competition', back_populates='competitions')

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)