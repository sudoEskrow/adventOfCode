import numpy as np
import re

input = np.loadtxt('./input', dtype=str, delimiter=' ')


def solution_1():
    valid_passwords = 0
    for password_set in input:
        min, max = re.split("-", password_set[0])
        letter = password_set[1][0]
        if (int(min) <= password_set[2].count(letter) <= int(max)):
            valid_passwords += 1

    print("Valid passwords for Solution 1 are:", valid_passwords)


def solution_2():
    valid_passwords = 0
    for password_set in input:
        pos1, pos2 = re.split("-", password_set[0])
        letter = password_set[1][0]
        valid_positions = 0
        if (password_set[2][int(pos1)-1] == letter):
            valid_positions += 1
        if (password_set[2][int(pos2)-1] == letter):
            valid_positions += 1
        if (valid_positions == 1):
            valid_passwords += 1
    print("Valid passwords for Solution 2 are:", valid_passwords)


solution_1()
solution_2()
