from App.database import db
from App.models import rank


## i propose a weighted system for Rating calculation
# Rating will determine rank hence it is here, but we can move it to Student

# rating = (Participation Percentage × 8) + (Avg Weighted score )

#Weighted score = (my score / max score) * (Competiton lvl)/(max competiton level) * 10

#Avg Weighted score = ( Sum of all weighted scores ) / (number of competitions participated in)



#def calculate_rating(user_id):
#   weighted_score = 0
#   Sum_of_weighted_scores = 0
#   number_of_participated_in_competitions = 0

#   student_id = user_id

#   look for all occurences of my student ID in Student_Team and get Team_ID

#   for every occurence of Team_ID in Competiton_Team:

#       number_of_participated_in_competitions++
#       Get competitin team score AKA my score
#       Get Competition_ID
#       Get Competiton max_score
#       Get competiton_level
#       Comeptition max level = 10
#       weighted_score = ( (my_score / max_score) * (competiton_level/max_lvl) * 10)
#       Sum_of_weighted_scores =  Sum + weighted_score
#   
#   avg_weighted_score = Sum_of_weighted_scores / number_of_participated_in_competitions

#   find total amount of comeptitions
#   participation  = (number_of_participated_in_competitions / total_amt_competitions) * 8

#   rating = participation * avg_weighted_score
#   find student from student_id
#   update student rating_score











