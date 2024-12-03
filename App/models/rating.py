from App.database import db

from .competition_team import *
from .student import *

#Rank table allows us to have the rank history
#Each user will have a new rank after every competition result is added
#not just every competition, but every result!



class Rating(db.Model):
    __tablename__ = 'rating'
    
    id = db.Column(db.Integer, primary_key=True) # Primary key
    rating_score = db.Column(db.Integer, default=999) # A student's individual rating score. Calculated in the controller
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False) # Stores User.id for a Student.
    #think of competition_team as a row in a results table 
    #we want rank to update for each result we add and we want to keep every entry so we have a history
    competition_team_id = db.Column(db.Integer, db.ForeignKey('competition_team.id'), nullable=False)

    def __init__(self, rating_score, student_id, competition_team_id):
        self.rating_score = rating_score
        self.student_id = student_id
        self.competition_team_id = competition_team_id
