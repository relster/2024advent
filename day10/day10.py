# @author Mark White
# Advent of Code - Day 10
# https://adventofcode.com/2024/day/10

debug = False

if debug:
    data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
else:
    with open('day10/input.txt', 'r') as file:
        data = file.read()


map : list[list[int]] = []

for rowcount, row in enumerate(data.splitlines()):
    if debug: print(f"{rowcount}, {row}")
    rowcells = []
    for cell in row:
        rowcells.append(int(cell))
    map.append(rowcells)

def printMap():
    for row in map:
        print(f"\t{row}")

printMap()