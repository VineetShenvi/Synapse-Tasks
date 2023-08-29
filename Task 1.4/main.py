from itertools import permutations
import random
from prettytable import PrettyTable

class Player1:
    name = 'Courage the Cowardly Dog'
    age = 25
    elo = 1000.39
    tenacity = 1000
    isBoring = False
    score = 0
    wins = 0
    losses = 0
    draws = 0

p1 = Player1()

class Player2:
    name = 'Princess Peach'
    age = 23
    elo = 945.65
    tenacity = 50
    isBoring = True
    score = 0
    wins = 0
    losses = 0
    draws = 0

p2 = Player2()

class Player3:
    name = 'Walter White'
    age = 50
    elo = 1650.73
    tenacity = 750
    isBoring = False
    score = 0
    wins = 0
    losses = 0
    draws = 0

p3 = Player3()

class Player4:
    name = 'Rory Gilmore'
    age = 16
    elo = 1700.87
    tenacity = 500
    isBoring = False
    score = 0
    wins = 0
    losses = 0
    draws = 0

p4 = Player4()

class Player5:
    name = 'Anthony Fantano'
    age = 37
    elo = 1400.45
    tenacity = 400
    isBoring = True
    score = 0
    wins = 0
    losses = 0
    draws = 0

p5 = Player5()

class Player6:
    name = 'Beth Harmon'
    age = 20
    elo = 2500.34
    tenacity = 150
    isBoring = False
    score = 0
    wins = 0
    losses = 0
    draws = 0

p6 = Player6()

obj_list = [p1, p2, p3, p4, p5, p6]

matches = list(permutations(obj_list,2))

def simulateMatch(obj1, obj2, match_no):
    print(f"\nMatch Number {match_no}:")
    print(f"{obj1.name} vs {obj2.name}")
    elo_diff=abs(obj1.elo-obj2.elo)
    if obj1.elo>obj2.elo:
        higher_elo=obj1
        lower_elo=obj2
    else:
        higher_elo = obj2
        lower_elo=obj1
    if obj1.tenacity>obj2.tenacity:
        higher_tenacity=obj1
        lower_tenacity = obj2
    else:
        higher_tenacity = obj2
        lower_tenacity = obj1
    if elo_diff>100:
        winner = higher_elo
        loser=lower_elo
        print(f"Winner: {winner.name}")
        winner.score+=1
        winner.wins+=1
        loser.losses+=1
    elif elo_diff<100 and (obj1.isBoring or obj2.isBoring):
        print("Match drawn.")
        obj1.score += 0.5
        obj1.draws += 1
        obj2.score += 0.5
        obj2.draws += 1
    elif elo_diff<100 and elo_diff>50:
        tenacity_product = random.randint(1,11)*lower_elo.tenacity
        if tenacity_product>higher_elo.elo:
            winner = lower_elo
            loser=higher_elo
        else:
            winner = higher_elo
            loser = lower_elo
        print(f"Winner: {winner.name}")
        winner.score += 1
        winner.wins += 1
        loser.losses += 1
    elif elo_diff<50:
        winner = higher_tenacity
        loser = lower_tenacity
        print(f"Winner: {winner.name}")
        winner.score += 1
        winner.wins += 1
        loser.losses += 1

count=1
for match_up in matches:
    player1 = match_up[0]
    player2 = match_up[1]
    simulateMatch(player1, player2, count)
    count+=1

myTable = PrettyTable(["Player Name", "Score", "Wins", "Losses", "Draws"])
for obj in obj_list:
    myTable.add_row([obj.name, int(obj.score), obj.wins, obj.losses, obj.draws])
print(myTable)




