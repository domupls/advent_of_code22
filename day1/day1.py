from sys import stdin


# part one
def max_calories():
    glo_max = 0
    loc_max = 0
    for line in stdin:
        if line == '\n':
            if loc_max > glo_max:
                glo_max = loc_max
            loc_max = 0
        else:
            loc_max += int(line)
    return glo_max


print(max_calories())
