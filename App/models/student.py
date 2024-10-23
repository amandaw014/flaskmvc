from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from .associations_table import *

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(80), unique=True, nullable=False)
    competitions = db.relationship('Competition', secondary='student_competition', back_populates='students')

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)