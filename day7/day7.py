from sys import argv
from collections import defaultdict


filename = argv[1]


def accumulate(list_: list):
    prev = ""
    for i in range(len(list_)):
        yield prev + list_[i]
        prev += list_[i]


# part one

# values default to zero
dirs = defaultdict(int)


def find_size_of_dir():
    with open(filename) as f:
        file = f.readlines()
    for line in file:
        match line.split():
            # set "outermost" directory
            case ['$', 'cd', '/']:
                curr_dir = ['/']
            # remove one level from directory
            case ['$', 'cd', '..']:
                curr_dir.pop()
            # add nested directory
            case ['$', 'cd', dir_name]:
                curr_dir.append(dir_name + '/')
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, _:
                for path in list(accumulate(curr_dir)):
                    dirs[path] += int(size)
    return sum(s for s in dirs.values() if s <= 100_000)


print(find_size_of_dir())
