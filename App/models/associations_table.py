from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

# Define the association table
student_competition = db.Table('student_competition',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('competition_id', db.Integer, db.ForeignKey('competition.id'), primary_key=True)
)

