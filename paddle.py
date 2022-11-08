from turtle import Turtle, getcanvas


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def go_to(self, x):
        x = x - 600
        self.goto(x, self.ycor())