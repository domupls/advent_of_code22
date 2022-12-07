from sys import stdin

score_shape = {'A': 1, 'B': 2, 'C': 3}
same_shapes = {'X': 'A', 'Y': 'B', 'Z': 'C'}
win_shapes = {'A': 'Y', 'B': 'Z', 'C': 'X'}

WIN = 6
DRAW = 3

# part one


def rps_strategy():
    score = 0
    for line in stdin:
        l_split = line.split()
        op_move, my_move = l_split[0], l_split[1]
        if op_move == same_shapes[my_move]:
            score += DRAW
        elif my_move == win_shapes[op_move]:
            score += WIN
        score += score_shape[same_shapes.get(my_move)]
    return score


# print(rps_strategy())

# part two
def rps_end_strategy():
    score = 0
    for line in stdin:
        l_split = line.split()
        op_move, my_exit = l_split[0], l_split[1]
        if my_exit == 'Y':
            score += DRAW + score_shape[op_move]
        elif my_exit == 'Z':
            score += WIN + score_shape[same_shapes[win_shapes[op_move]]]
        else:
            my_move = [k for k, v in same_shapes.items() if v == op_move][0]
            score += score_shape[[k for k,
                                  v in win_shapes.items() if v == my_move][0]]
    return score


# print(rps_end_strategy())
