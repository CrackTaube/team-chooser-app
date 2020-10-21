players = ["Melissa","Alex","Leon","Sophia"]
print(players)

print(players[0])
print(players[1])
print(players[2])
print(players[3])

from random import choice
print(choice(players))

playerA = choice(players)
print(playerA)

teamA=[]
playerA = choice(players)
teamA.append(playerA)
players.remove(playerA)
print("Players left:",players)

teamB=[]
playerB = choice(players)
teamB.append(playerB)
players.remove(playerB)
print("Players left:",players)

while len(players) > 0:
    playerA = choice(players)
    print(playerA)
    teamA.append(playerA)
    players.remove(playerA)
    print("Players left:",players)
    
    playerB = choice(players)
    print(playerB)
    teamB.append(playerB)
    players.remove(playerB)
    print("Players left:",players)

print("Team A:", teamA)
print("Team B:", teamB)
    
players = []
file = open("players.txt", "r")
players = file.read().splitlines()
print(players)

teamA = []
teamB = []

while len(players) > 0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)
    
    if players == []:
        break
    
    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)
    
