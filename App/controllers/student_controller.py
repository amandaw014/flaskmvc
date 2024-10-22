from App.database import db
from App.models import Student

def create_student(name, email):
    new_student = Student(name=name, email=email)
    db.session.add(new_student)
    db.session.commit()
    return new_student

def get_all_students():
    return Student.query.all()

def get_all_students_json():
    return [student.to_dict() for student in Student.query.all()]
