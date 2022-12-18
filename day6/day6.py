from sys import argv

filename = argv[1]


# both parts
def char_marker(distinct_chars):
    marker_stack = []
    with open(filename) as f:
        file = f.read()
    for i in range(len(file)-1):
        marker_stack.append(file[i])
        if len(set(marker_stack[-distinct_chars:])) == distinct_chars:
            return i+1


print(char_marker(4))
print(char_marker(14))
