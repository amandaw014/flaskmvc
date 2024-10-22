# App/controllers/result.py
import csv
from App.models import Result, Competition, Student
from App.database import db

def import_competition_results(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            competition = Competition.query.filter_by(name=row['competition_name']).first()
            student = Student.query.filter_by(name=row['student_name']).first()
            if competition and student:
                result = Result(
                    score=row['score'],
                    competition_id=competition.id,
                    student_id=student.id
                )
                db.session.add(result)
        db.session.commit()

def get_competition_results(competition_id):
    return Result.query.filter_by(competition_id=competition_id).all()

def get_competition_results_json(competition_id):
    results = get_competition_results(competition_id)
    return [result.to_json() for result in results]
