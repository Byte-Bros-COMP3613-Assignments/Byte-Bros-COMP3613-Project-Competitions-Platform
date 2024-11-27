from App.database import db
from App.models import Competition, Moderator, CompetitionTeam, Team, Student#, Student, Admin, competition_student
from datetime import datetime

def create_competition(mod_name, comp_name, date, location, level, max_score):
    comp = get_competition_by_name(comp_name)
    if comp:
        print(f'{comp_name} already exists!')
        return None
    
    mod = Moderator.query.filter_by(username=mod_name).first()
    if mod:
        newComp = Competition(name=comp_name, date=datetime.strptime(date, "%d-%m-%Y"), location=location, level=level, max_score=max_score)
        try:
            newComp.add_mod(mod)
            db.session.add(newComp)
            db.session.commit()
            print(f'New Competition: {comp_name} created!')
            return newComp
        except Exception as e:
            db.session.rollback()
            print("Something went wrong!")
            return None
    else:
        print("Invalid credentials!")

def get_competition_by_name(name):
    return Competition.query.filter_by(name=name).first()

def get_competition(id):
    return Competition.query.get(id)

def get_all_competitions():
    return Competition.query.all()

def get_all_competitions_json():
    competitions = Competition.query.all()

    if not competitions:
        return []
    else:
        return [comp.get_json() for comp in competitions]

def display_competition_results(name):
    comp = get_competition_by_name(name)

    if not comp:
        print(f'{name} was not found!')
        return None
    elif len(comp.teams) == 0:
        print(f'No teams found for {name}!')
        return []
    else:
        comp_teams = CompetitionTeam.query.filter_by(comp_id=comp.id).all()
        comp_teams.sort(key=lambda x: x.points_earned, reverse=True)

        leaderboard = []
        count = 1
        curr_high = comp_teams[0].points_earned
        curr_rank = 1
        
        for comp_team in comp_teams:
            if curr_high != comp_team.points_earned:
                curr_rank = count
                curr_high = comp_team.points_earned

            team = Team.query.filter_by(id=comp_team.team_id).first()
            leaderboard.append({"placement": curr_rank, "team": team.name, "members" : [student.username for student in team.students], "score":comp_team.points_earned})
            count += 1
        
        return leaderboard




###############OBSERVER DESIGN PATTERN EXAMPLE##########
# from flask_sqlalchemy import SQLAlchemy
# from app import app
# db = SQLAlchemy(app)

# #Observer 

# class Publisher(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     subscribers = db.relationship('Subscriber', backref='publisher', lazy=True)

#     def __init__(self, name):
#       self.name = name

#     def subscribe(self, subscriber):
#       self.subscribers.append(subscriber)

#     def notify_subscribers(self, message):
#         for subscriber in self.subscribers:
#             subscriber.update(message)

# class Subscriber(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)
#     state = db.relationship('State', backref="subscriber", lazy=True)

#     def __init__(self, name, publisher_id):
#       self.publisher_id =  publisher_id
#       self.name = name
  
#     def update(self, message):
#       print(f'{self.name}: received {message}')
#       self.state.append(State(message))
#       db.session.add(self)
#       db.session.commit()

# class State(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   message = db.Column(db.String(50), nullable=False)
#   subscriber_id = db.Column(db.Integer, db.ForeignKey('subscriber.id'), nullable=False)

#   def __init__(self, message):
#     self.message = message