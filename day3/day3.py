import re

# @author Mark White
# Advent of Code - Day 3
# https://adventofcode.com/2024/day/3

debug = False

instructionPattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"
dont = "don't()"
do = "do()"


def getSum(line: str, part1=True):
    totalSum = 0
    matches = re.finditer(instructionPattern, line, re.MULTILINE)
    adding = True
    for matchnum, match in enumerate(matches, start=1):
        if match.group(0) == dont: adding = False
        elif match.group(0) == do: adding = True
        else:
            if adding or part1:
                if debug: print(f"match {matchnum}: {match}, groups: {match.groups()}")
                left = int(match.group(2))
                right = int(match.group(3))
                sum = left * right
                totalSum += sum
    return totalSum

# testString = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# print(f"part 1: totalSum: {getSum(testString)}")
# print(f"part 2: totalSum: {getSum(testString, False)}")

testString = None

with open('day3/input.txt', 'r') as file:
    testString = file.read()

print(f"part 1 totalSum: {getSum(testString)}")
print(f"part 2 totalSum: {getSum(testString, False)}")
