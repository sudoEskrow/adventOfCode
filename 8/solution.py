input = open('./input').read().split('\n')
# input = open('./testinput').read().split('\n')

index = 0
accumulator = 0
visited_ops = []


def operation(op):
    op = op.split(' ')
    global index
    global accumulator
    if op[0] == 'nop':
        index += 1
    elif op[0] == 'acc':
        index += 1
        accumulator += int(op[1])
    elif op[0] == 'jmp':
        index += int(op[1])


def find_loop(inp):
    global index
    global visited_ops
    if index not in visited_ops:
        visited_ops.append(index)
        operation(inp[index])
        find_loop(inp)


def solution_2():
    global index
    global accumulator
    global visited_ops
    instructions = input.copy()
    for i, inst in enumerate(instructions):
        visited_ops = []
        accumulator = 0
        index = 0
        instructions = input.copy()
        if inst[0] == 'n':
            instructions[i] = inst.replace('nop', 'jmp')
        elif inst[0] == 'j':
            instructions[i] = inst.replace('jmp', 'nop')
        try:
            find_loop(instructions)
        except:
            return accumulator
    return accumulator


def solution_1():
    find_loop(input)
    return accumulator


print('Solution to part 1 is', solution_1())
print('Solution to part 2 is', solution_2())
