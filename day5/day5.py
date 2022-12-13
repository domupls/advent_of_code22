from sys import argv

filename = argv[1]


# part one
def supply_stack():
    stack_list = []
    message = ""
    with open(filename) as f:
        file = f.read()
    stacks, instructions = file.split('\n\n')
    for crates in stacks.split('\n'):
        stack_list.append([crate for crate in crates[1::4]])
    transposed_arr = [list(stack) for stack in zip(*stack_list[:-1])]
    for stack in transposed_arr:
        while ' ' in stack:
            stack.remove(' ')
    for ins in instructions.split('\n'):
        res = [int(i) for i in ins.split() if i.isdigit()]
        count, from_, to = res[0], res[1], res[2]
        for _ in res:
            while count != 0:
                char = transposed_arr[from_-1].pop(0)
                transposed_arr[to-1].insert(0, char)
                count -= 1
    for i in transposed_arr:
        message += i[0]
    return message


# print(supply_stack())
