import random
import levels
import os

clear = lambda: os.system('cls')

stage = 0
row = 0
column = 0

while stage + 1 <= levels.levels:
    level = levels.level[stage]

    genrow = level[-1]
    gencolumn = level[-2]
    heigh = level[-3]
    width = level[-4]
    inside = 1

    while inside == 1:
        clear()
        x = ((genrow - 1) * width + gencolumn) * 4
        y = x - 4
        room = level[y:x]

        print('You are currently in: row ', genrow, ' and column ', gencolumn)
        direct = ['-', '-', '-', '-']
        wr = 0
        for i in room:
            if room[wr] > 0:
                direct[wr] = str(wr + 1)
            wr = wr + 1
        print('----[', direct[0], ']----')
        print('[', direct[3], ']-----[', direct[1], ']')
        print('----[', direct[2], ']----')

        c = int(input())
        c = c - 1

        if room[c] == 0:
            print('Ooops... You can\'t go here')
        elif room[c] == 1:
            if c == 0:
                genrow = genrow - 1
            elif c == 1:
                gencolumn = gencolumn + 1
            elif c == 2:
                genrow = genrow + 1
            elif c == 3:
                gencolumn = gencolumn - 1
        elif room[c] == 2:
            genrow = random.randint(1, heigh)
            gencolumn = random.randint(1, width)
        elif room[c] == 3:
            print('You escaped! Now come back to your boring life...')
            stage = stage + 1
            inside = 0
