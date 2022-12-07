from sys import stdin

score_shape = {'A': 1, 'B': 2, 'C': 3}
same_shapes = {'X': 'A', 'Y': 'B', 'Z': 'C'}
win_shapes = {'A': 'Y', 'B': 'Z', 'C': 'X'}

WIN = 6
DRAW = 3


def rps_startegy():
    score = 0
    for line in stdin:
        l_split = line.split()
        op_move, my_move = l_split[0], l_split[1]
        # print(op_move == win_shape[op_move])
        if op_move == same_shapes[my_move]:
            score += DRAW
        elif my_move == win_shapes[op_move]:
            score += WIN
        score += score_shape[same_shapes.get(my_move)]
    return score


# print(rps_startegy())
