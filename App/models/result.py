from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    score = db.Column(db.Float, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)