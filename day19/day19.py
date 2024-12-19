# @author Mark White
# Advent of Code - Day 19
# https://adventofcode.com/2024/day/19

from functools import lru_cache

debug = False
fileData = True

if not fileData:
    data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""
else:
    with open('day19/input.txt', 'r') as file:
        data = file.read()

availableTowelsDict = dict(w = [], u = [], b = [], r = [], g = [])
availableTowels = []
maxTowelPatternLength = 0
patternsMade = 0
patternOptionsMade = 0

# @lru_cache(maxsize=None)
def makePattern(design: str, dp: dict[str, int]):
    if debug: print(f"finding a pattern for {design}")

    if design in dp:
        return dp[design]
    
    patternOptions = 0
    
    for towel in availableTowelsDict[design[0]]:
        # iterate over all the towels, see if the design starts with our towel
        if design.startswith(towel):
            remainingDesign = design[len(towel):]
            if len(remainingDesign) > 0: # there's more design to match
                patternOptions += makePattern(remainingDesign, dp)
                # there's no else, because if this towel didn't allow any patterns to match behind it, we'll just ignore it as a working pattern at all
            else: # no more design to match up, return the current towel used
                patternOptions += 1
    dp[design] = patternOptions
    return patternOptions

# main processing loop for each row in the input
for rowcount, row in enumerate(data.splitlines()):
    if debug: print(f"{rowcount}: {row}")
    
    if rowcount > 1:
        # attempt to build a towel pattern
        dp: dict[str, int] = {}
        patternCountForDesign = makePattern(row, dp)
        if patternCountForDesign:
            if debug: print(f" made {patternCountForDesign} patterns for design")
            patternsMade += 1
            patternOptionsMade += patternCountForDesign
            print(f" patterns: {patternsMade}\toptions:{patternCountForDesign}")
        else:
            if debug: print("unable to make a pattern")
    elif rowcount == 0: # first row, pull out the list of available towels
        for towel in row.split(", "):
            availableTowelsDict[towel[0]].append(towel)
            availableTowels.append(towel)
            if len(towel) > maxTowelPatternLength: maxTowelPatternLength = len(towel)
        
        for color in availableTowelsDict:
            availableTowelsDict[color] = sorted(availableTowelsDict[color], key=len, reverse=True)

        print(f"created the list of availableTowels: {availableTowelsDict}")

print(f"We were able to make {patternsMade} patterns and {patternOptionsMade} total options!")