import re

# @author Mark White
# Advent of Code - Day 1, part 2
# https://adventofcode.com/2024/day/1

list1 = []
list2 = []

with open('day1/input.txt', 'r') as file:
    for line in file:
        args = re.split(r"\s+", line)
        # print("line:\"" + line + "\"\targs:")
        # print (args)
        list1.append(int(args[0]))
        list2.append(int(args[1]))

list1.sort()
list2.sort()
list2.reverse()

print(len(list1))
print(len(list2))

score = 0

for first in list1:
    second_count = list2.count(first)
    similarity = first * second_count
    # print(str(first) + " * " + str(second_count) + " = " + str(similarity))
    score += similarity

print("final difference: " + str(score))

