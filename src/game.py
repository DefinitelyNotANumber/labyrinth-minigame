import random
import levels


stage = 0
row = 0
column = 0

while stage + 1 <= len(levels.level):
    level = levels.level[stage]
    genrow = level[-1]
    gencolumn = level[-2]
    height = level[-3]
    width = level[-4]
    inside = True
    print('This level is ', height, ' x ', width)

    while inside:
        x = ((genrow - 1) * width + gencolumn) * 4  # some weird math, don't ask me
        y = x - 4
        room = level[y:x]

        print('You are currently in: row ', genrow, ' and column ', gencolumn)   # uhh.. basically all of the UI
        directions = ['-', '-', '-', '-']
        wr = 0
        for i in room:
            if room[wr] > 0:
                directions[wr] = str(wr + 1)
            wr += 1
        print('----[', directions[0], ']----')
        print('[', directions[3], ']-----[', directions[1], ']')
        print('----[', directions[2], ']----')

        c = int(input()) - 1
        action = room[c]

        if action == 0:
            print('Ooops... You can\'t go here')
        elif action == 1:
            if c == 0:
                genrow -= 1
            elif c == 1:
                gencolumn += 1
            elif c == 2:
                genrow += 1
            elif c == 3:
                gencolumn -= 1
        elif action == 2:
            genrow = random.randint(1, height)
            gencolumn = random.randint(1, width)
        elif action == 3:
            print('You escaped! Now come back to your boring life...')
            stage += 1
            inside = False
