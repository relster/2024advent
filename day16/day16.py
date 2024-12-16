# @author Mark White
# Advent of Code - Day 16
# https://adventofcode.com/2024/day/16

debug = True
EAST = "e"
NORTH = "n"
SOUTH = "s"
WEST = "w"
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

# define special puzzle pieces
START = "S"
END = "E"
WALL = "#"

class Coords:
    row = -1
    column = -1
    def __init__(self, r: int, c: int):
        self.row = r
        self.column = c
    def __str__(self):
        return f'Coords({self.row}, {self.column})'

class Reindeer:
    coords : Coords = None
    direction : str = None
    def __init__(self):
        self.coords = Coords(0,0)
        self.direction = EAST
    def __init__(self, r, c, d):
        self.coords = Coords(r, c)
        self.direction = d
    def __init__(self, c:Coords, d: str):
        self.coords = c
        self.direction = d
    
    def moveFoward(self):
        if self.direction == NORTH:
            self.coords.row -= 1
        elif self.direction == EAST:
            self.coords.column += 1
        elif self.direction == SOUTH:
            self.coords.row += 1
        elif self.direction == WEST:
            self.coords.column -= 1
        else:
            print(f"ERROR: moveForward failed, invalid internal direction {self.direction}") # failure to move a valid direction

    def turnRight(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = NORTH
        else:
            print(f"ERROR: turnRight failed, invalid internal direction {self.direction}") # failure to move a valid direction
    
    def turnLeft(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == EAST:
            self.direction = NORTH
        elif self.direction == SOUTH:
            self.direction = EAST
        elif self.direction == WEST:
            self.direction = SOUTH
        else:
            print(f"ERROR: turnLeft failed, invalid internal direction {self.direction}") # failure to move a valid direction
    
    def __str__(self):
        return f'Reindeer({self.coords}, {self.direction})'

puzzle : list[list[int]] = []

def standingOn(re:Reindeer):
    return puzzle[re.coords.row][re.coords.column]

def isReindeerValid(re: Reindeer):
    return standingOn(re) != WALL

def isAtEnd(re:Reindeer):
    return standingOn(re) == END

def tryMoveReindeer(re:Reindeer):
    points = 0
    while (isReindeerValid(re)):
        if isAtEnd(re):
            # we're done the puzzle
            return True
        
    pass



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
                if (column == START) :
                    start = Coords(currentRow, currentColumn)
                elif column == END :
                    end = Coords(currentRow, currentColumn)
                puzzleRow.append(column)
                currentColumn += 1
        puzzle.append(puzzleRow)
        currentRow += 1
if debug:
    print(f"About to start on puzzle, start ({start}), end ({end})")
    for row in puzzle:
        print(f"\t{row}")

reindeer = Reindeer(start, EAST)
points = 0
print(f"{reindeer} is in a valid position? {reindeer.isValid(puzzle)}")
reindeer.moveFoward()
print(f"{reindeer} is in a valid position? {reindeer.isValid(puzzle)}")
