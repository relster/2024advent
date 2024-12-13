import re
from button import Button, ButtonA, ButtonB

# @author Mark White
# Advent of Code - Day 13
# https://adventofcode.com/2024/day/13

buttonPattern = r"Button (\w)\: X\+(\d+), Y\+(\d+)"
prizePattern = r'Prize: X=(\d+), Y=(\d+)'

def findOptimal(prize: list[int], buttons: list[Button]):
    prizeX = prize[0]
    prizeY = prize[1]
    buttonA = buttons[0]
    buttonB = buttons[1]

    bTimes = int(prizeX / buttonB.xMove) # starting w/ b because we know it's cheaper
    while bTimes >= 0: # check things as long as we have bTimes to check
        bMoveX = bTimes * buttonB.xMove
        aTimes = int((prizeX - bMoveX) / buttonA.xMove)
        checkX = prizeX - bMoveX - (aTimes * buttonA.xMove) == 0
        
        bMoveY = bTimes * buttonB.yMove
        checkY = prizeY - bMoveY - (aTimes * buttonA.yMove) == 0

        if checkX and checkY:
            return [aTimes, bTimes]
        else:
            bTimes = bTimes - 1
    return None



    # aXMove = buttonA.xMove #if isX else buttonA.yMove
    # bXMove = buttonB.xMove #if isX else buttonB.yMove
    # aYMove = buttonA.yMove
    # bYMove = buttonB.yMove
    
    # bTimes = xPrize / bXMove
    # xTally = bTimes * bXMove
    # yTally = bTimes * bYMove
    # if (xTally == xPrize) and (yTally == yPrize):
    #     return [0, bTimes]
    # else:
    #     xRemainder = xPrize - xTally
    #     aTimes = xRemainder / aXMove
    #     if (aTimes * aXMove == xRemainder) and (aTimes * aYMove):
    #         return [aTimes, bTimes]
    #     else:
    #         if bTimes == 0:
    #             return [-1, -1]
    #         else:
    #             moves = findOptimal([xPrize-bXMove, yPrize], buttons)
    #             return [moves[0], moves[1]+1]

with open('day13/testinput.txt', 'r') as file:
    totalAPresses = 0
    totalBPresses = 0
    totalWins = 0
    totalTries = 0

    buttonA: Button = None
    buttonB: Button = None
    prize = [0,0]

    for line in file:
        button: Button = None
        match = re.search(buttonPattern, line, re.MULTILINE)
        if match: # we have button text
            buttonType = match.group(1)
            match buttonType:
                case "A":
                    button = ButtonA(int(match.group(2)), int(match.group(3)))
                    buttonA = button
                case "B":
                    button = ButtonB(int(match.group(2)), int(match.group(3)))
                    buttonB = button
            # print(button)
        else:
            match = re.search(prizePattern, line)
            if match:
                prize = [int(match.group(1)), int(match.group(2))]
                totalTries = totalTries + 1
                # print("Prizes at: " + str(prize))
                # do stuff to actually see if we can pull prize here
                answer = findOptimal(prize, [buttonA, buttonB])
                if answer:
                    totalAPresses = totalAPresses + answer[0]
                    totalBPresses = totalBPresses + answer[1]
                    totalWins = totalWins + 1
                    print(f"We won prize {totalTries}")

    costA = totalAPresses * buttonA.moveCost
    costB = totalBPresses * buttonB.moveCost
    print(f"Wins: {totalWins}; total A: {totalAPresses} (cost: {costA}), total B: {totalBPresses} (cost: {costB}); ultimate cost: {costA + costB}")