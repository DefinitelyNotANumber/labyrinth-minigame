# Yes, doing it is tidous. No I won't create a better system, because I'm lazy
# Basically every room is made from 4 numbers (one line), and said rooms are separated into rows
# 0 - wall
# 1 - open passage
# 2 - random teleport
# 3 - exit to the next level

level = [[0, 1, 1, 0,  # Row 1
          0, 0, 1, 1,
          0, 2, 1, 0,

          1, 2, 1, 0,  # Row 2
          1, 0, 0, 1,
          1, 3, 1, 0,

          1, 1, 0, 0,  # Row 3
          0, 1, 2, 1,
          1, 0, 0, 1,

          3, 3, 1, 1],  # Last 4 digits are: columns, rows, starting column, starting row


         [2, 1, 0, 0,
          0, 1, 0, 1,
          0, 1, 1, 1,
          0, 1, 1, 1,
          0, 0, 1, 1,
          0, 0, 0, 0,

          0, 1, 1, 0,
          0, 1, 1, 1,
          1, 0, 0, 1,
          1, 0, 1, 0,
          1, 1, 0, 0,
          0, 2, 0, 1,

          1, 0, 1, 0,
          1, 1, 0, 0,
          0, 0, 1, 1,
          1, 0, 1, 0,
          2, 1, 0, 0,
          0, 0, 1, 1,

          1, 1, 0, 0,
          0, 0, 1, 1,
          1, 0, 1, 0,
          1, 1, 1, 0,
          0, 1, 0, 1,
          1, 0, 1, 1,

          2, 0, 1, 0,
          1, 1, 1, 0,
          1, 0, 0, 1,
          1, 0, 1, 0,
          3, 2, 1, 0,
          1, 0, 1, 0,

          1, 1, 0, 0,
          1, 0, 0, 1,
          0, 1, 0, 0,
          1, 0, 0, 1,
          1, 1, 0, 0,
          1, 0, 2, 1,

          6, 6, 2, 3]]
