from sys import stdin


# part one
def range_full_overlap(range1, range2):
    x1, x2 = range1.start, range1.stop
    y1, y2 = range2.start, range2.stop
    return x1 >= y1 and x2 <= y2


def find_fully_overlaping():
    overlap_pairs_count = 0
    for line in stdin:
        ranges = [list(map(int, (r.split('-'))))
                  for r in line.strip('\n').split(',')]
        range1, range2 = range(ranges[0][0], ranges[0][1]), range(
            ranges[1][0], ranges[1][1])
        if range_full_overlap(range1, range2) or range_full_overlap(range2, range1):
            overlap_pairs_count += 1
    return overlap_pairs_count


# print(find_fully_overlaping())


# part two
def range_overlap(range1, range2):
    x1, x2 = range1.start, range1.stop
    y1, y2 = range2.start, range2.stop
    return x1 <= y2 and y1 <= x2


def find_semi_overlaping():
    overlap_pairs_count = 0
    for line in stdin:
        ranges = [list(map(int, (r.split('-'))))
                  for r in line.strip('\n').split(',')]
        range1, range2 = range(ranges[0][0], ranges[0][1]), range(
            ranges[1][0], ranges[1][1])
        if range_overlap(range1, range2) or range_overlap(range2, range1):
            overlap_pairs_count += 1
    return overlap_pairs_count


# print(find_semi_overlaping())
