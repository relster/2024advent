# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"Button (\w)\: X\+(\d+), Y\+(\d+)"

test_str = ("Button A: X+94, Y+34\n")


with open('day13/testinput.txt', 'r') as file:
    for line in file:

        matches = re.search(regex, line, re.MULTILINE)
        print (matches)
        # for matchNum, match in enumerate(matches, start=1):
            
        #     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            
        #     for groupNum in range(0, len(match.groups())):
        #         groupNum = groupNum + 1
                
        #         print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
