import random

#NCAA Tournament Randomizer

team1 = "Auburn"
team2 = "Wisconsin"
team3 = "Marquette"
team4 = "Texas"

teams = {
    team1: "Tigers",
    team2: "Badgers",
    team3: "Golden Eagles",
    team4: "Longhorn",
}

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
