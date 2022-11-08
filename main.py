from turtle import Screen, Turtle, getcanvas
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Bricks

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.title("Breakout")
screen.tracer(0)


screen.listen()
paddle = Paddle((0, -350))
ball = Ball()
scoreboard = Scoreboard()

brick_list = []


def set_bricks():
    y = 250
    x = -565
    for _ in range(2):
        for _ in range(17):
            brick = Bricks((x, y))
            x += 70
            brick.value = 8
            brick.color("red")
            brick_list.append(brick)
        y -= 30
        x = -565
    for _ in range(2):
        for _ in range(17):
            brick = Bricks((x, y))
            x += 70
            brick.value = 4
            brick.color("orange")
            brick_list.append(brick)
        y -= 30
        x = -565
    for _ in range(2):
        for _ in range(17):
            brick = Bricks((x, y))
            x += 70
            brick.value = 2
            brick.color("green")
            brick_list.append(brick)
        y -= 30
        x = -565
    for _ in range(2):
        for _ in range(17):
            brick = Bricks((x, y))
            x += 70
            brick.value = 1
            brick.color("yellow")
            brick_list.append(brick)
        y -= 30
        x = -565

def motion(event):
    x = event.x
    paddle.go_to(x)


canvas = getcanvas()
x, y = canvas.winfo_pointerx(), canvas.winfo_pointery()
canvas.bind('<Motion>', motion)


set_bricks()
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.xcor() > 580 or ball.xcor() < -580:
        ball.bounce_x()

    if ball.ycor() > 380:
        ball.bounce_y()

    if ball.distance(paddle) < 45 and ball.ycor() > -340:
        ball.bounce_y()

    for bricks in brick_list:
        if ball.distance(bricks) < 35:
            bricks.hideturtle()
            brick_list.remove(bricks)
            scoreboard.score_point(bricks.value)
            ball.bounce_y()

    if ball.ycor() < -450:
        ball.reset_position()
        scoreboard.live_lost()
        if scoreboard.lives == 0:
            game_is_on = False

    if not brick_list:
        set_bricks()
        ball.x_move += 1
        ball.y_move += 1


screen.exitonclick()