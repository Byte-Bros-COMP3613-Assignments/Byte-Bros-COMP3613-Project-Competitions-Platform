from App.database import db
from App.models import rating


## i propose a weighted system for Rating calculation
# Rating will determine rank hence it is here, but we can move it to Student

# rating = (Participation Percentage × 8) + (Avg Weighted score )

#Weighted score = (my score / max score) * (Competiton lvl)/(max competiton level) * 10

#Avg Weighted score = ( Sum of all weighted scores ) / (number of competitions participated in)



#def calculate_rating(user_id):
#   weighted_score = 0
#   Sum_of_weighted_scores = 0
#   number_of_participated_in_competitions = 0
#
#   student_id = user_id
#   student = Student.query.filter_by(id=user_id).first()
#   user_team_ids = []
#
##   look for all teams my user is a part of
#   all_student_teams = session.query(Student_Team).all() ## geting all teams
#   for student_team in all_student_teams:
#       if all_student_teams.student_id == user_id:
#           user_team_ids.append(student_team.team_id) ##list of teams my student is a part of
#   
#   all_competition_team = session.query(Competition_Team).all() ##all competition teams AKA all competition results
#
##   look for every occurence of a user_team_ids in Competiton_Team. teams can participate in multi comps:
#   for team_id in user_team_ids: 
#       for competition_team in all_competition_team: ##looking through all comeptition teams
#            if competition_team.team_id == team_id:  ##finding a competition the user was in
#
#               number_of_participated_in_competitions+=1
#               my_score = competition_team.points_earned
#               current_comp_id = competition_team.comp_id
#               current_comp = Competition.query.filter_by(id = current_comp_id).first()
#               max_score_current_comp = current_comp.max_score
#               level_of_current_comp = current_comp.level
#               max_lvl = 10
#               weighted_score = ( (my_score / max_score_current_comp) * (level_of_current_comp/max_lvl) * 10)
#               Sum_of_weighted_scores = Sum_of_weighted_scores + weighted_score
#
#   avg_weighted_score = Sum_of_weighted_scores / number_of_participated_in_competitions
#   num_of_all_competitions = Competition).query.count()
#   participation  = (number_of_participated_in_competitions / num_of_all_competitions) * 8
#   rating = participation * avg_weighted_score
#   student.rating = rating
#   return user_id



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











