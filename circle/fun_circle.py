import turtle
import math as g
b = turtle.Turtle()

b.speed(10)

b.color("red", "yellow")


for i in range(2000):
	b.forward(g.sqrt(i))
	b.left(i%180)



turtle.done()