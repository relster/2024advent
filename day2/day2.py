import re

# @author Mark White
# Advent of Code - Day 2
# https://adventofcode.com/2024/day/2

def isReportSafeRecursive(reportList):
    return checkLevel(reportList, -1, False, 0)

def checkLevel(levelsToBeChecked, priorLevel, isIncreasing, cardinal):
    testLevel = levelsToBeChecked.pop(0)
    if cardinal >= 2 and validDifferences(priorLevel, testLevel): # third level or beyond, isIncreasing should be valid, priorLevel should be valid
        if (isIncreasing and priorLevel < testLevel) or (not isIncreasing and priorLevel > testLevel):
            return len(levelsToBeChecked) == 0 or checkLevel(levelsToBeChecked, testLevel, isIncreasing, cardinal + 1)
    elif cardinal == 1 and validDifferences(priorLevel, testLevel): # this is the second item, special item to determine if we're increasing or decreasing
        if testLevel > priorLevel:
            return len(levelsToBeChecked) == 0 or checkLevel(levelsToBeChecked, testLevel, True, cardinal + 1)
        else:
            return len(levelsToBeChecked) == 0 or checkLevel(levelsToBeChecked, testLevel, False, cardinal + 1)
    elif cardinal == 0: #cardinal = 0 here
        return len(levelsToBeChecked) == 0 or checkLevel(levelsToBeChecked, testLevel, False, 1)
    return False

def validDifferences(priorLevel, testLevel):
    diff = abs(priorLevel - testLevel)
    return diff >= 1 and diff <= 3



with open('day2/input.txt', 'r') as file:
    safeCount = 0
    for line in file:
        args = re.split(r"\s+", line)
        levels = []
        
        # convert string list into int list
        for arg in args:
            if arg == "":
                continue #skip over blanks
            levels.append(int(arg))
        
        # check if the report levels are safe
        if isReportSafeRecursive(list(levels)):
            safeCount += 1
            print("good list recur: " + str(levels))
        else:
            print("bad list recur: " + str(levels))

    print("Safe Reports (Recursive): " + str(safeCount))