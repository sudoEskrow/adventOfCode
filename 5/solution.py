import math

input = open('./input').read().splitlines()
# input = ['FFFFFFFLLL', 'BBBBBBBLLL', 'FFFFFFFRRR']
seat_id_list = []

max_rows = 127
max_column = 7
highest_seat_id = 0

for bpass in input:
    row = max_rows
    lowest_row = 0
    column = max_column
    lowest_column = 0
    for char in bpass[:7]:
        if char == 'F':
            row = (lowest_row + row) / 2
            row = math.floor(row)
        elif char == 'B':
            lowest_row = (lowest_row + row) / 2
            lowest_row = math.ceil(lowest_row)
    for char in bpass[7:]:
        if char == 'L':
            column = (lowest_column + column) / 2
            column = math.floor(column)
        elif char == 'R':
            lowest_column = (lowest_column + column) / 2
            lowest_column = math.ceil(lowest_column)
    # print(bpass[:7])
    if row != lowest_row:
        print('rows not matching', row, lowest_row)
    if column != lowest_column:
        print('columns not matching', column, lowest_column)
    seat_id = row * 8 + column
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id
    seat_id_list.append(seat_id)


def solution_2(lst):
    return [i for x, y in zip(lst, lst[1:])
            for i in range(x + 1, y) if y - x > 1]


print('Part 1 solution is', highest_seat_id)
print(solution_2(sorted(seat_id_list)))
