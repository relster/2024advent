# @author Mark White
# Advent of Code - Day 18
# https://adventofcode.com/2024/day/18

import Maze

debug = False

if debug:
    puzzleDimensions = 7 # 7 or 71 for full input
    maxBytesToProcess = 12
else:
    puzzleDimensions = 71 # 7 or 71 for full input
    maxBytesToProcess = 1024

puzzle : list[list[int]] = []
for row in range(0, puzzleDimensions):
    newRow = []
    for col in range(0, puzzleDimensions):
        newRow.append(".")
    puzzle.append(newRow)

def printPuzzle():
    for row in puzzle: print(f"\t{row}")

if debug:
    print(f"generated the blankPuzzle with {puzzleDimensions} rows and {puzzleDimensions} columns")
    printPuzzle()

data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

if not debug:
    with open('day18/input.txt', 'r') as file:
        data = file.read()

bytesProcessed = 0
unusedBytes = []

for newRow in data.splitlines():
    x, y = newRow.split(",")
    if bytesProcessed >= maxBytesToProcess:
        unusedBytes.append((int(x), int(y)))
    else:
        if debug: print(f"loading line into puzzle: '{newRow}'")
        puzzle[int(y)][int(x)] = "#"
    bytesProcessed += 1
    
if True:
    print(f"updated the puzzle with fallen bytes")
    printPuzzle()

maze = Maze.Maze(puzzle)
solution = maze.find_shortest_path((0,0), (puzzleDimensions-1, puzzleDimensions-1))
print(f"solution found in {len(solution)-1} steps: {solution}")
for byte in unusedBytes:
    if debug: print(f"searching for {byte} in solution list")
    x, y = byte
    puzzle[int(y)][int(x)] = "#"
    maze = Maze.Maze(puzzle)
    tempsolution = maze.find_shortest_path((0,0), (puzzleDimensions-1, puzzleDimensions-1))
    if not tempsolution: print(f"found the blocker: {byte}")
    else:
        print(f"there's still a solution after adding {byte}: {len(tempsolution)-1} steps")
    # if byte in solution: print (f"solution found at {solution.index(byte)}: {byte}")