import turtle
import random
import math

sq = turtle.Turtle()

b = turtle.Screen()

b.bgcolor("black")

sq.speed(0)
sq.pensize(2)

sq.left(45)

def sq1():
	for i in range(300):
		turtle.colormode(255)
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)

		sq.pencolor(r, g, b)
		sq.forward(i )
		sq.right(90)

sq1()

sq.left(90)

def sq2():
	for i in range(100):
		turtle.colormode(255)
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)

		sq.pencolor(r, g, b)
		sq.forward(i )
		sq.right(90)

sq2()

sq.forward(100)
sq.right(90)
sq.forward(100)
sq.right(90)
sq.forward(50)
sq.left(90)
sq.forward(250)

sq2()

sq.right(90)
sq.forward(100)
sq.left(90)
sq.forward(50)
sq.right(90)
sq.forward(250)

sq2()

sq.right(90)
sq.forward(100)
sq.left(90)
sq.forward(50)
sq.right(90)
sq.forward(250)

sq2()

sq.hideturtle()



turtle.done()