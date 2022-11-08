from turtle import Turtle


class Bricks(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)
        self.value = 0

    def set_bricks(self):
        y = 250
        x = -565
        for _ in range(2):
            for _ in range(17):
                brick = Bricks((x, y))
                x += 70
                brick.value = 8
                brick.color("red")
            y -= 30
            x = -565
        for _ in range(2):
            for _ in range(17):
                brick = Bricks((x, y))
                x += 70
                brick.value = 4
                brick.color("orange")
            y -= 30
            x = -565
        for _ in range(2):
            for _ in range(17):
                brick = Bricks((x, y))
                x += 70
                brick.value = 2
                brick.color("green")
            y -= 30
            x = -565
        for _ in range(2):
            for _ in range(17):
                brick = Bricks((x, y))
                x += 70
                brick.value = 1
                brick.color("yellow")
            y -= 30
            x = -565