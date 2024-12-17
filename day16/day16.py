# @author Mark White
# Advent of Code - Day 16
# https://adventofcode.com/2024/day/16

debug = True

# define directions we can turn
EAST = "e"
NORTH = "n"
SOUTH = "s"
WEST = "w"
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

# define points for moving
POINTS_FORWARD = 1
POINTS_TURN = 1000

# actions a reindeer can take
ACTION_MOVE = "m"
ACTION_LEFT = "l"
ACTION_RIGHT = "r"

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
        self.space = space
    def __str__(self):
        return f'Coords({self.row}, {self.column})'

class PuzzleSpace:
    coords : Coords = None
    space : str = None # START, END, WALL, or open
    def __init__(self, coords : Coords, space : str):
        self.coords = coords
        self.space = space
    def isWall(self):
        return self.space == WALL
    def isEnd(self):
        return self.space == END

class Reindeer:
    coords : Coords = None
    direction : str = None
    def __init__(self):
        self.coords = Coords(0,0)
        self.direction = EAST
    def __init__(self, c:Coords, d: str):
        self.coords = c
        self.direction = d
    def copy(self):
        return Reindeer(Coords(self.coords.row, self.coords.column), self.direction)
    
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

puzzle : list[list[Coords]] = []

def standingOn(coords:Coords) -> PuzzleSpace:
    return puzzle[coords.row][coords.column]

def isReindeerValid(re: Reindeer):
    return not standingOn(re.coords).isWall()

def isAtEnd(re:Reindeer):
    return standingOn(re.coords).isEnd()

def peekDirectionValid(re : Reindeer, direction : str):
    checkCoords = Coords(re.coords.row, re.coords.column)
    if direction == NORTH:
        checkCoords.row = re.coords.row - 1
    elif direction == EAST:
        checkCoords.column = re.coords.column + 1
    elif direction == SOUTH:
        checkCoords.row = re.coords.row + 1
    elif direction == WEST:
        checkCoords.column = re.coords.column - 1
    else:
        print(f"ERROR: peekDirection failed, invalid internal direction {direction}") # failure to provide a valid direction
    
    return not standingOn(checkCoords).isWall()

def dfs(re:Reindeer):
    pass

def tryMoveReindeer(re:Reindeer, action): # doesn't work, too recursive
    points = 0
    if (action == ACTION_MOVE):
        re.moveFoward()
        points += POINTS_FORWARD
    elif (action == ACTION_LEFT):
        re.turnLeft()
        re.moveFoward()
        points += POINTS_TURN + POINTS_FORWARD
    elif (action == ACTION_RIGHT):
        re.turnRight()
        re.moveFoward()
        points += POINTS_TURN + POINTS_FORWARD
    else:
        print(f"failed tryMoveReindeer({re}, {action}) with an unknown action")
        return 999999999
    
    if isReindeerValid(re):
        if isAtEnd(re):
            # we're done the puzzle
            return points
        else:
            movePoints = points + tryMoveReindeer(re.copy(), ACTION_MOVE)
            leftPoints = points + tryMoveReindeer(re.copy(), ACTION_LEFT)
            rightPoints = points + tryMoveReindeer(re.copy(), ACTION_RIGHT)
            points = [movePoints, leftPoints, rightPoints]
            return min(points) # return the cheapest path

    else:
        return 999999999 # not in a valid spot, couldn't move here
        
    pass



start : Coords = None
end : Coords = None

teststring = ["####", "#ES#", "####"]
with open('day16/testinput.txt', 'r') as file:
    currentRow = 0
    for line in file:
    # for line in teststring:
        puzzleRow : list[int] = []
        currentColumn = 0
        for column in line:
            if column != "\n":
                currentCoords = Coords(currentRow, currentColumn)
                if (column == START) :
                    start = currentCoords
                elif column == END :
                    end = currentCoords
                puzzleRow.append(currentCoords)
                currentColumn += 1
        puzzle.append(puzzleRow)
        currentRow += 1
if debug:
    print(f"About to start on puzzle, start ({start}), end ({end})")
    for row in puzzle:
        print(f"\t{row}")

reindeer = Reindeer(start, EAST)

pathPoints = findPath(reindeer)
print(pathPoints)

# movePoints = tryMoveReindeer(reindeer.copy(), ACTION_MOVE)
# leftPoints = tryMoveReindeer(reindeer.copy(), ACTION_LEFT)
# rightPoints = tryMoveReindeer(reindeer.copy(), ACTION_RIGHT)
# # cover the case where S has open spaces to it's left, even though we always start facing east
# reindeer.direction = WEST
# reversePoints = 2000 + tryMoveReindeer(reindeer.copy(), ACTION_MOVE)
# points = [movePoints, leftPoints, rightPoints, reversePoints]
# print(f"best path: {min(points)}") # return the cheapest path