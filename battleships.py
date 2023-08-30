# TASK: https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
def validate_battlefield(field):
    c = True
    vectors = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    while c:
        len = 0
        for i in range(10):
            for j in range(10):
                while field[i][j] == 1:
                    field[i][j] = 2
                    len += 1
                    near = 0
                    vec = [0, 0]
                    for a, b in vectors:
                        if 0 <= i + a < 10 and 0 <= j + b < 10:
                            if field[i + a][j + b] == 1:
                                if vec==[0, 0]: vec = [a, b]
                                if [a, b] != vec: return False
                                near += 1
                        if near > 1: return False
                    i += vec[0]
                    j += vec[1]
                if len: break
            if len: break
        if len in ships:
            ships.remove(len)
        else:
            return False
        if not ships: c = False

    return True

battleField =  [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
if validate_battlefield(battleField) == False: print("Correct validation")