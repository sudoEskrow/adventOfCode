import numpy as np

input = np.loadtxt('./input', dtype=str, comments=None)


row_size = len(input[0])
arr_size = len(input)


def solution_1():
    trees_hit = 0
    pos = 0
    for row_num, row in enumerate(input):
        if(row[pos] == '#'):
            trees_hit += 1
        pos += 3
        if pos >= row_size:
            pos -= row_size
        if row_num+1 == arr_size:
            print('hit', trees_hit, 'trees')
            return


def calc_hits(right, down):
    trees_hit = 0
    pos = 0
    for row_num, row in enumerate(input):
        if (row_num % down == 0):
            if(row[pos] == '#'):
                trees_hit += 1
            pos += right
            if pos >= row_size:
                pos -= row_size
            if row_num+down >= arr_size:
                return trees_hit


solution_1()
# print(calc_hits(3, 1))
sol_2 = calc_hits(1, 1) * calc_hits(3, 1)*calc_hits(5, 1) * \
    calc_hits(7, 1)*calc_hits(1, 2)
print('Solution 2 is: ', sol_2)
