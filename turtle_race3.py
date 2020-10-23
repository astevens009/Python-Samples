# TODO: Import the modules
import turtle
import random

def move_turtle():
    units_to_move = random.randrange(150, 200)
    return units_to_move

# TODO: Create a screen
wn = turtle.Screen()
wn.bgcolor("black")

# TODO: Create two turtles
odo = turtle.Turtle()
odo.color("gold")
odo.shape("turtle")

quark = turtle.Turtle()
quark.color("firebrick")
quark.shape("turtle")

# TODO: Move the turtles to their starting positions
odo.up()
odo.goto(-100, 20)

quark.up()
quark.goto(-100, -20)

# TODO: Begin race
for count in range(1, 5):
    odo.forward(move_turtle())
    quark.forward(move_turtle())

wn.exitonclick()