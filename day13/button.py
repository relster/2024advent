class Button:
    name = ""
    xMove = 0
    yMove = 0
    moveCost = 0

    def __init__(self, moveX, moveY):
        self.xMove = moveX
        self.yMove = moveY

    def __str__(self):
        return f'Button {self.name}: X={self.xMove}, Y={self.yMove}, cost={self.moveCost}'

class ButtonA(Button):
    name = "A"
    moveCost = 3

class ButtonB(Button):
    name = "B"
    moveCost = 1