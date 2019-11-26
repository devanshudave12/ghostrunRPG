# Name - Devanshu Dave
# course - Computer Science 30
# period - 4
# Date Created - 23/11/19
# Description -  code shows the locations or prints the map of the game

import random
from tabulate import tabulate


# defining the function to start game
def startgame():
    '''print the map in formated and in the form of table'''
    final = []   # making a list
    game = []     # making a list
    game1 = []    # list for game1
    finalgame = []  # making list for final one whch will be main list
    f1 = []
    i = 6    # index is set equal to 6
    # list for locations
    list = ['start', ['livingroom', 'bathroom', 'kitchen', 'bedroom', "hall"]]
    # using loop for printing
    for j in range(1):
        final.append(list[0])  # adding a value in a list
        for i in range(20):
            final.append(random.choice(list[len(list)-1]))  # adding it to list
            # adding  it into final list
        game.append(final)
        final = []
    for k in game[0]:
        if k not in game1:
            game1.append(k)
    finalgame.append(game1)  # adding it to the main list

    a = finalgame[0][:3]    # it will divide the output into to 2 rows
    b = finalgame[0][3:]    # it will divide the output into to 2 rows

    # print()
    # print(a)
    # print(b)
    c = []
    c.append(a)
    c.append(b)
    print(tabulate(c, tablefmt="fancy_grid"))   # printing it in a table

# startgame()
