from App.database import db
from App.models import rating
from App.models import *

## i propose a weighted system for Rating calculation
# Rating will determine rank hence it is here, but we can move it to Student

# rating = (Participation Percentage × 8) + (Avg Weighted score )

#Weighted score = (my score / max score) * (Competiton lvl)/(max competiton level) * 10

#Avg Weighted score = ( Sum of all weighted scores ) / (number of competitions participated in)


def create_rating (rating_score, student_id):
    new_rating_model = Rating(rating_score=rating_score,student_id=student_id)
    db.session.add(new_rating_model)
    db.session.commit()
    print ("new rating made!")


def print_my_ratings(user_id):
    user_ratings = Rating.query.filter_by(student_id = user_id).all()
    for rating in user_ratings:
        print(f"Rating ID: {rating.id}, Score: {rating.rating_score}, StudentID: {rating.student_id}")


def calculate_rating(user_id):
    weighted_score = 0
    Sum_of_weighted_scores = 0
    number_of_participated_in_competitions = 0

    student_id = user_id
    student = Student.query.filter_by(id=user_id).first()
    user_team_ids = []

    #look for all teams my user is a part of
    all_student_teams = StudentTeam.query.all() ## geting all teams
    participated_competitions = set()
    
    for student_team in all_student_teams:
        if student_team.student_id == user_id:
            user_team_ids.append(student_team.team_id) ##list of teams my student is a part of
  
    all_competition_team = CompetitionTeam.query.all() ##all competition teams AKA all competition results

    #look for every occurence of a user_team_ids in Competiton_Team. teams can participate in multi comps:
    for team_id in user_team_ids: 
        #all_competition_team = CompetitionTeam.query.filter_by(team_id = team_id).all()
        for competition_team in all_competition_team: ##looking through all comeptition teams
            if competition_team.team_id == team_id and competition_team.comp_id not in participated_competitions:  ##finding a competition the user was in
                number_of_participated_in_competitions+=1
                my_score = competition_team.points_earned
                current_comp_id = competition_team.comp_id
                current_comp = Competition.query.filter_by(id = current_comp_id).first()
                participated_competitions.add(competition_team.comp_id)

                #print (student.username)
                #print(current_comp.name)
                #print(competition_team.team_id)
                #myteamz= Team.query.filter_by(id = team_id).first()
                #print(myteamz.name)

                my_last_competition_team = competition_team.id
                max_score_current_comp = current_comp.max_score
                level_of_current_comp = current_comp.level
                max_lvl = 10
                weighted_score = ( (my_score / max_score_current_comp) * (level_of_current_comp/max_lvl) * 100)
                Sum_of_weighted_scores = Sum_of_weighted_scores + weighted_score

    num_of_all_competitions = Competition.query.count() + 1

    if number_of_participated_in_competitions == 0:
        avg_weighted_score = 0
        participation = 0
    elif number_of_participated_in_competitions != 0:     
        avg_weighted_score = Sum_of_weighted_scores / number_of_participated_in_competitions
        participation  = (number_of_participated_in_competitions / num_of_all_competitions) * 8  

    rating = participation * avg_weighted_score

    create_rating(rating,user_id)

    student.rating_score = rating
    #print (student.username, student.rating_score, number_of_participated_in_competitions , num_of_all_competitions )


#subscriber list is all students
def update_all_rating():
    for student in Student.query.all():
        calculate_rating(student.id)


#######LOGIC#######
#       get all the team ids the user was a part of
#       look at the all competition_team for matches
#       if a match:
#           number_of_participated_in_competitions+=1
#           Get competitin team score AKA my score
#           Get Competition_ID
#           Get Competiton max_score
#           Get competiton_level
#           Competition max level = 10
#           weighted_score = ( (my_score / max_score) * (competiton_level/max_lvl) * 10)
#           Sum_of_weighted_scores =  Sum + weighted_score
#
#       iterate and go to next team id
#
#   avg_weighted_score = Sum_of_weighted_scores / number_of_participated_in_competitions

#   find total amount of comeptitions
#   participation  = (number_of_participated_in_competitions / total_amt_competitions) * 8

#   rating = participation * avg_weighted_score
#   find student from student_id
#   update student rating_score 
