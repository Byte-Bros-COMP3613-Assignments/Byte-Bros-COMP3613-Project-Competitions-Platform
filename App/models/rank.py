from App.database import db

from .competition_team import *
from .student import *

#Rank table allows us to have the rank history
#Each user will have a new rank after every competition result is added
#not just every competition, but every result!



class Rank(db.Model):
    __tablename__ = 'rank'
    
    id = db.Column(db.Integer, primary_key=True) # Primary key
    rank = db.Column(db.Integer, default=999) # A student's individual rank, calculated as a function of their rating.
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False) # Stores User.id for a Student.
    #think of competition_team as a row in a results table 
    #we want rank to update for each result we add and we want to keep every entry so we have a history
    competition_team_id = db.Column(db.Integer, db.ForeignKey('competition_team.id'), nullable=False)

    def __init__(self, rank, student_id, competition_team_id):
        self.rank = rank
        self.student_id = student_id
        self.competition_team_id = competition_team_id
