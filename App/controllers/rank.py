from App.database import db
from App.models import rank


## i propose a weighted system for Rating calculation
# Rating will determine rank hence it is here, but we can move it to Student

# (Participation Percentage × 8) + ( (log(Max Level+1) / log(Competition Level+1) ) x 10 +  (my score/max score) x 7

# Formula = A + B + C


##participated in competitions = 
# get all student ID's
#for first ID
#count all instances of this ID in competition_teams
#save the last comp this student participated in
#this last comp is what we will use to get the level, score and max score from
### WHY?
# well we want to have your rating decrease slighlty for every competition you miss
# but we dont want to reset them like if they got 0/100 

##all competitions = 
#count all competiton in competitions OR   ID of last competition + 1

## max level we set as 10


##Logic explained
# we want to encourage participations the most
# we want to maker higher ranked competitions sort of exponentially more valvuable
#Score should still matter


