import random

def randomize_color():

    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)

    return (r, b, g)

class box:

    def __init__(self, x, y, h = 25, w = 25, color = (255, 0, 0)):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.color = color


