import random
from tabulate import tabulate


def startgame():
    final = []
    game = []
    game1 = []
    finalgame = []
    f1 = []
    i = 6
    list = ['start', ['livingroom', 'bathroom', 'kitchen', 'restroom', "hall"]]
    for j in range(1):
        final.append(list[0])
        for i in range(20):
            final.append(random.choice(list[len(list)-1]))
            # append it into final list
        game.append(final)
        final = []
    for k in game[0]:
        if k not in game1:
            game1.append(k)
    finalgame.append(game1)

    a = finalgame[0][:3]
    b = finalgame[0][3:]

    # print()
    # print(a)
    # print(b)
    c = []
    c.append(a)
    c.append(b)
    print(tabulate(c, tablefmt="fancy_grid"))

startgame()
