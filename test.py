from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.bgcolor("green")
screen.title("Vítejte v Hadí hře")
screen.setup(width=600, height=600)
screen.tracer(False)

# apple
apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

# head
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# body part
body_parts = []

# define


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def move_up():
    head.direction = "up"

def move_down():
    head.direction = "down"

def move_left():
    head.direction = "left"

def move_right():
    head.direction = "right"

# Kliknutí na klávesy

screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# Hlavní cyklus

while True:
    screen.update()

    if head.xcor() > 290 or head.xcor() < - 290 or head.ycor() > 290 or head.ycor() < - 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # skryjeme části
        for one_body_part in body_parts:
            one_body_part.goto(1500, 1500)

        # Vyčistíme body_parts
        body_parts.clear()
    if head.distance(apple) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        apple.goto(x, y)

        # přidáváme části těla
        new_body_part = Turtle("square")
        new_body_part.color("purple")
        new_body_part.penup()
        body_parts.append(new_body_part)

    for index in range(len(body_parts)-1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)


    move()
    time.sleep(0.1)
    screen.update()


screen.exitonclick()