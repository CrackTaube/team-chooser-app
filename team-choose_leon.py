
from random import choice

# creating an empty list
players = []

teams = []

# number of elemetns as input
n = int(input("Gib an wie viele, Player es gibt: "))

m = int(input("Wie viele Teams soll es geben?: "))

# iterating till the range
for i in range(0, n):
    ele = str(input("Player: "))

    players.append(ele)  # adding the element


for i in range(0, m):
    eles = str(input("Teams: "))

    teams.append(eles)  # adding the element

teamA = []
teamB = []

# loop until there are no players left
while len(players) > 0:

    # choose a random player for team A
    playerA = choice(players)
    teamA.append(playerA)
    # remove the player from the players list
    players.remove(playerA)

    # break out of the loop if there are no players left
    if players == []:
        break

    # choose a random player for team B
    playerB = choice(players)
    teamB.append(playerB)
    # remove the player from the players list
    players.remove(playerB)

# choose random team names for the 2 teams
teamNameA = choice(teams)
teams.remove(teamNameA)
teamNameB = choice(teams)
teams.remove(teamNameB)

# print the teams
print('\nHier sind deine Teams:\n')
print(teamNameA, teamA)
print(teamNameB, teamB)
