# @author Mark White
# Advent of Code - Day 4
# https://adventofcode.com/2024/day/4

debug = False

wordSearch : list[list[int]] = []

data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

with open('day4/input.txt', 'r') as file:
    data = file.read()

for newRow in data.splitlines():
    if debug: print(f"loading line into wordsearch: '{newRow}'")
    rowlist = []
    for column in range(0, len(newRow), 1):
        if newRow[column] != "\n":
            if debug: print(f"loading column into wordsearch: '{newRow[column]}'")
            rowlist.append(newRow[column])
    wordSearch.append(rowlist)

numRows = len(wordSearch)
numCols = 0
if numRows > 0: numCols = len(wordSearch[0])

if debug:
    print(f"generated the word search with {numRows} rows and {numCols} columns")
    for row in wordSearch: print(f"\t{row}")


lookUp = 3 # first row to start looking at XMAS pointing UP
stopDown = numRows - 4 # last row to stop looking for words pointing DOWN
lookBack = 3 # first column to start looking at XMAS pointing BACKWARDS
stopForward = numCols - 4 # last column to stop looking for words going forwards

foundWords = 0

# master for loop to iterate over all the letters in the puzzle - start searching
for rowNum in range(0, numRows):
    for colNum in range(0, numCols):
        cell = wordSearch[rowNum][colNum]
        if debug: print(f"checking ({rowNum}, {colNum}): {cell}")

        if cell == "X": # only search for XMAS when we've found an X
            if colNum <= stopForward: # search forwards if we're before the stop
                if (wordSearch[rowNum][colNum+1] == "M" and
                        wordSearch[rowNum][colNum+2] == "A" and
                        wordSearch[rowNum][colNum+3] == "S"):
                    if debug: print("found xmas going E, starting at ({rowNum}, {colNum})")
                    foundWords += 1
            if colNum >= lookBack: # search backwards if we're after the column start
                if (wordSearch[rowNum][colNum-1] == "M" and
                        wordSearch[rowNum][colNum-2] == "A" and
                        wordSearch[rowNum][colNum-3] == "S"):
                    if debug: print("found xmas going W, starting at ({rowNum}, {colNum})")
                    foundWords += 1
            if rowNum <= stopDown: # search variations of words going down as long as we're away from the bottom of the wordSearch
                #first search S
                if (wordSearch[rowNum+1][colNum] == "M" and
                        wordSearch[rowNum+2][colNum] == "A" and
                        wordSearch[rowNum+3][colNum] == "S"):
                    if debug: print("found xmas going S, starting at ({rowNum}, {colNum})")
                    foundWords += 1
                if colNum <= stopForward: # search SE if we're before the stop
                    if (wordSearch[rowNum+1][colNum+1] == "M" and
                            wordSearch[rowNum+2][colNum+2] == "A" and
                            wordSearch[rowNum+3][colNum+3] == "S"):
                        if debug: print("found xmas going SE, starting at ({rowNum}, {colNum})")
                        foundWords += 1
                if colNum >= lookBack: # search SW if we're after the column start
                    if (wordSearch[rowNum+1][colNum-1] == "M" and
                            wordSearch[rowNum+2][colNum-2] == "A" and
                            wordSearch[rowNum+3][colNum-3] == "S"):
                        if debug: print("found xmas going SW, starting at ({rowNum}, {colNum})")
                        foundWords += 1
            if rowNum >= lookUp: # search variations of words going N as long as we're below the top of the puzzle
                #first search N
                if (wordSearch[rowNum-1][colNum] == "M" and
                        wordSearch[rowNum-2][colNum] == "A" and
                        wordSearch[rowNum-3][colNum] == "S"):
                    if debug: print("found xmas going N, starting at ({rowNum}, {colNum})")
                    foundWords += 1
                if colNum <= stopForward: # search NE if we're before the stop
                    if (wordSearch[rowNum-1][colNum+1] == "M" and
                            wordSearch[rowNum-2][colNum+2] == "A" and
                            wordSearch[rowNum-3][colNum+3] == "S"):
                        if debug: print("found xmas going NE, starting at ({rowNum}, {colNum})")
                        foundWords += 1
                if colNum >= lookBack: # search NW if we're after the column start
                    if (wordSearch[rowNum-1][colNum-1] == "M" and
                            wordSearch[rowNum-2][colNum-2] == "A" and
                            wordSearch[rowNum-3][colNum-3] == "S"):
                        if debug: print("found xmas going NW, starting at ({rowNum}, {colNum})")
                        foundWords += 1
print(f"found {foundWords} words in the search")


mas = 0

lookUp = 1 # first row to start looking at XMAS pointing UP
stopDown = numRows - 1 # last row to stop looking for words pointing DOWN
lookBack = 1 # first column to start looking at XMAS pointing BACKWARDS
stopForward = numCols - 1 # last column to stop looking for words going forwards

M = "M"
S = "S"

# master for loop to iterate over all the letters in the puzzle - start searching for an X of MAS
for rowNum in range(0, numRows):
    for colNum in range(0, numCols):
        cell = wordSearch[rowNum][colNum]
        if debug: print(f"checking mas ({rowNum}, {colNum}): {cell}")

        if cell == "A": # only search for XMAS when we've found an X
            if (rowNum >= lookUp and rowNum < stopDown and
                    colNum >= lookBack and colNum < stopForward):
                # 1.2
                # .A.
                # 3.4
                slot1 = wordSearch[rowNum-1][colNum-1]
                slot2 = wordSearch[rowNum-1][colNum+1]
                slot3 = wordSearch[rowNum+1][colNum-1]
                slot4 = wordSearch[rowNum+1][colNum+1]

                if ((slot1 == M and slot2 == M and slot3 == S and slot4 == S) or 
                        (slot1 == S and slot2 == M and slot3 == S and slot4 == M) or 
                        (slot1 == S and slot2 == S and slot3 == M and slot4 == M) or 
                        (slot1 == M and slot2 == S and slot3 == M and slot4 == S)):
                    if debug: print("found mas, centered at ({rowNum}, {colNum})")
                    mas += 1
print(f"found {mas} MAS patterns in the puzzle")
