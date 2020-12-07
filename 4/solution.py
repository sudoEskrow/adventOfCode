import itertools
from os import error
import re

with open('./input', 'r') as file:
    blocks = list("".join(group) for empty, group in itertools.groupby(
        file, key=str.isspace) if not empty)

newblocks = []

for block in blocks:
    newblock = block.replace('\n', ' ')
    newblocks.append(newblock.strip())

passports = []
for item in newblocks:
    passports.append(dict(dictitem.split(':') for dictitem in item.split(' ')))

valid_passports = []


def solution_1():
    for passport in passports:
        if len(passport) == 8 or ('cid' not in passport and len(passport) == 7):
            valid_passports.append(passport)
    return len(valid_passports)


def solution_2():
    hgt_pattern = re.compile(
        '((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)')
    hcl_pattern = re.compile('#[\da-f]{6}')
    ecl_pattern = re.compile('(amb|blu|brn|gr[yn]|hzl|oth){1}')
    pid_pattern = re.compile('^\d{9}$')
    validated_passports = 0
    for passport in valid_passports:
        try:
            if (1920 <= int(passport.get('byr')) <= 2002 and
                    2010 <= int(passport.get('iyr')) <= 2020 and
                    2020 <= int(passport.get('eyr')) <= 2030 and
                    hgt_pattern.match(passport.get('hgt')) and
                    hcl_pattern.match(passport.get('hcl')) and
                    ecl_pattern.match(passport.get('ecl')) and
                    pid_pattern.match(passport.get('pid'))):
                validated_passports += 1
        except TypeError:
            # print(passport)
            pass
    return validated_passports


print('The valid passports are:', solution_1())

print('The validated passports are:', solution_2())
