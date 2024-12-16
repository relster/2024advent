# @author Mark White
# Advent of Code - Day 16
# https://adventofcode.com/2024/day/16

debug = True

class Coords:
    row = -1
    column = -1
    def __init__(self, r, c):
        self.row = r
        self.column = c

class Reindeer:
    coords : Coords = None

    def __init__(self, r, c):
        self.coords = Coords(r, c)
    def __init__(self, c:Coords):
        self.coords = c

def tryMoveReindeer(reindeer, direction):
    
    pass

puzzle : list[list[int]] = []

start : Coords = None
end : Coords = None

teststring = ["####", "#SE#", "####"]
with open('day16/testinput.txt', 'r') as file:
    currentRow = 0
    # for line in file:
    for line in teststring:
        puzzleRow : list[int] = []
        currentColumn = 0
        for column in line:
            if column != "\n":
                if (column == "S") :
                    start = Coords(currentRow, currentColumn)
                elif column == "E" :
                    end = Coords(currentRow, currentColumn)
                puzzleRow.append(column)
                currentColumn += 1
        puzzle.append(puzzleRow)
        currentRow += 1
if debug:
    print(f"About to start on puzzle, start ({start}), end ({end})")
    for row in puzzle:
        print(f"\t{row}")

reindeer = Reindeer(start)
points = 0
direction = "E"

