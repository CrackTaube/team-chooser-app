#create players list 

players = ["Melissa","Alex","Leon","Sophia"]
print(players)

print(players[0])
print(players[1])
print(players[2])
print(players[3])


#add random, append, remove function 

from random import choice
print(choice(players))

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


#choose more players and open a new file 

players = []
file = open("players.txt", "r")
players = file.read().splitlines()
print(players)

teamA = []
teamB = []


#odd players

while len(players) > 0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)
    
    if players == []:
        break
    
    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)
    
