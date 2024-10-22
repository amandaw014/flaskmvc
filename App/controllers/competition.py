from App.database import db
from App.models import Competition

def create_competition(title, description):
    new_competition = Competition(title=title, description=description)
    db.session.add(new_competition)
    db.session.commit()
    return new_competition

def get_all_competitions():
    return Competition.query.all()

def get_all_competitions_json():
    return [competition.to_dict() for competition in Competition.query.all()]
