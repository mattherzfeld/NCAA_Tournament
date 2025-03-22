import random

#NCAA Tournament Randomizer

team1 = "Auburn"
team2 = "Wisconsin"

def randomizer():
    x1 = random.randint(0,10)
    y1 = random.randint(0,10)

    print(x1)
    print(y1)

    if x1 > y1:
        print(team1 + " wins the game over " + team2 +"!")
    
    elif x1 < y1:
        print(team2 + " wins the game over " + team1 +"!")
              
    else:
        print("They tied! Overtime!")
        return randomizer()

#Calling Function
randomizer()
