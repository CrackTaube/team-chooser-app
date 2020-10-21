#created 2020-10-21

from random import choice

players = []
file = open("players_alex.txt", "r")
players = file.read().splitlines()
print(players)

teamA = []
teamB = []

while len(players) > 0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)
    print("Players left: " + str(players))

    if players == []:
        break

    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)
    print("Players left: " + str(players))

print("Team A: ", teamA)
print("Team B: ", teamB)


file = open("teamnames_alex.txt", "r")
teamNames = file.read().splitlines()


teamA_name = choice(teamNames)
teamB_name = choice(teamNames)


print("Name von Team A", teamA_name)
print("Name von Team B", teamB_name)