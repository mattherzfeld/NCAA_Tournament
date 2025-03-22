import random

#NCAA Tournament Randomizer

team1 = "Auburn"
team2 = "Wisconsin"

def randomizer(x,y):
    x1 = random.randint(0,10)
    y1 = random.randint(0,10)

    print(x1)
    print(y1)

    if x1 > y1:
        print("{x} wins the game over {y}!")
    
    elif x1 < y1:
        print("{y} wins the game over {x}!")
              
    else:
        print("Somehow they tied?!")

randomizer(team1, team2)