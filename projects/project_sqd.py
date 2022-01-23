import turtle
import random

sqd = turtle.Turtle()
sqd.speed(0)

b = turtle.Screen()
b.bgcolor("black")


sqd.hideturtle()

def pot():
	for i in range(500):
		turtle.colormode(255)

		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)

		sqd.color(r, g, b)

		sqd.forward(i)
		sqd.right(100)

pot()

turtle.done()