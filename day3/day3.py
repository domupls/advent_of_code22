from sys import stdin
from string import ascii_letters


# part one
def sum_item_priority():
    priority = 0
    for line in stdin:
        half = int(len(line[:-1])/2)
        comp1, comp2 = [*line[:half]], [*line[half:-1]]
        for c in comp1:
            if c in comp2:
                priority += ascii_letters.index(c) + 1
                break
    return priority


# print(sum_item_priority())

# part two
def sum_group_priority():
    priority = 0
    group = []
    for line in stdin:
        group.append([*line[:-1]])
        if len(group) == 3:
            for c in group[0]:
                if c in group[1] and c in group[2]:
                    priority += ascii_letters.index(c) + 1
                    group = []
                    break
    return priority


# print(sum_group_priority())
