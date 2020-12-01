import numpy as np

input = np.loadtxt('./input')

def part1():
  for i in input:
    for n in input:
      if (i + n == 2020):
        print('two numbers that add to 2020',i*n)
        return

def part2():
  for i in input:
    for n in input:
      for f in input:
        if (i+n+f == 2020):
          print('three numbers that add to 2020',i*n*f)
          return

part1()
part2()