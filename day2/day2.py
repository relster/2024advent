import re

# @author Mark White
# Advent of Code - Day 2
# https://adventofcode.com/2024/day/2

def isReportSafe(reportList):
    isSecond = False
    isIncreasing = False
    prior = -1
    for level in reportList:
        if level == "":
            continue
        level = int(level)
        if prior == -1:
            prior = level
            isSecond = True
            continue
        if isSecond:
            if level > prior: # this level is higher than the last, the reprot must always increase now
                isIncreasing = True
                isSecond = False
            if level < prior: # this level is less than the last one, the report must now always decrease
                isIncreasing = False # this was already set, resetting just to be safe
                isSecond = False
        if level == prior: # can't be equal adjacent reports
            return False
        # check the math first 
        diff = abs(prior - level)
        if diff < 1 or diff > 3:
            return False # too far out of range, not safe
        if isIncreasing and prior > level:
            return False # prior is greater than current level, meaning we're now decreasing, unsafe
        if not isIncreasing and prior < level:
            return False # should be decreasing but prior is less than current report, meaning we're increasing, unsafe
        # made it through the test, reset prior, move on
        prior = level
    return True


with open('day2/input.txt', 'r') as file:
    safeCount = 0
    for line in file:
        args = re.split(r"\s+", line)
        if isReportSafe(args):
            safeCount += 1
        # print("line:\"" + line + "\"\targs:")

    print("Safe Reports: " + str(safeCount))