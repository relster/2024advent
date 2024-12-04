import re

# @author Mark White
# Advent of Code - Day 2 part 2
# https://adventofcode.com/2024/day/2#part2

def isReportSafeRecursive(reportList):
    isSafe = checkLevel(list(reportList), -1, -1, False, 0, False)
    print("Tested " + str(reportList) + " and isSafe? " + str(isSafe))
    return isSafe

def checkLevel(levelsToBeChecked, priorLevel, skipLevel, isIncreasing, cardinal, wasLevelSkipped):
    if len(levelsToBeChecked) == 0:
        return True
    testLevel = levelsToBeChecked.pop(0)

    if cardinal >= 2: # third level or beyond, isIncreasing should be valid, priorLevel should be valid
        if validDifferencesSkip(priorLevel, testLevel, skipLevel):
            if (isIncreasing and priorLevel < testLevel) or (not isIncreasing and priorLevel > testLevel):
                return len(levelsToBeChecked) == 0 or checkLevel(levelsToBeChecked, testLevel, priorLevel, isIncreasing, cardinal + 1, wasLevelSkipped)
            elif not wasLevelSkipped and ((isIncreasing and skipLevel < testLevel) or (not isIncreasing and skipLevel > testLevel)):
                # as long as we haven't already skipped another level, we can test against the skiplevel to validate the trend line
                altLevelsToBeChecked = list(levelsToBeChecked)
                altLevelsToBeChecked.insert(0,testLevel) # this re-winds the recursive function to go back and reset what the trend line should be based off of the current testLevel vs. the skipLevel
                
                return len(levelsToBeChecked) == 0 or checkLevel(levelsToBeChecked, testLevel, skipLevel, isIncreasing, cardinal + 1, True) or checkLevel(altLevelsToBeChecked, skipLevel, -1, False, 1, True)
        else: # current item isn't a valid difference, but let's see if we skip it, are we still okay?
            if not wasLevelSkipped: # we haven't already skipped one, lets skip and move on
                if len(levelsToBeChecked) > 0:
                    return checkLevel(levelsToBeChecked, skipLevel, -1, isIncreasing, cardinal, True)
                else:
                    return True # this is the last item in the list, and we're skipping it, but haven't skipped before, thus the list is now safe            
    elif cardinal == 1: # this is the second item, special item to determine if we're increasing or decreasing
        # allow for invalid differences between the first two if we skip the first one
        if (validDifferences(priorLevel, testLevel)):
            if testLevel > priorLevel:
                return len(levelsToBeChecked) == 0 or checkLevel(levelsToBeChecked, testLevel, priorLevel, True, cardinal + 1, wasLevelSkipped)
            else:
                return len(levelsToBeChecked) == 0 or checkLevel(levelsToBeChecked, testLevel, priorLevel, False, cardinal + 1, wasLevelSkipped)
        return not wasLevelSkipped and (len(levelsToBeChecked) == 0 or checkLevel(list(levelsToBeChecked), testLevel, -1, False, cardinal, True) or checkLevel(levelsToBeChecked, priorLevel, -1, False, cardinal, True)) #act as if we just had to wipe the first item or the first item never existed
    elif cardinal == 0: #cardinal = 0 here
        return len(levelsToBeChecked) == 0 or checkLevel(levelsToBeChecked, testLevel, -1, False, 1, False)
    return False

def validDifferencesSkip(priorLevel, testLevel, skipLevel):
    return validDifferences(priorLevel, testLevel) or validDifferences(skipLevel, testLevel)

def validDifferences(priorLevel, testLevel):
    diff = abs(priorLevel - testLevel)
    return diff >= 1 and diff <= 3




# isReportSafeRecursive([10])

with open('day2/tests.txt', 'r') as file:
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

    print("Safe Reports (Recursive): " + str(safeCount))