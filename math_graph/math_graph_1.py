import turtle 
import math as g

b = turtle.Turtle()
b.speed(10000)

b.color("blue")

b.begin_fill()

for i in range(200):
	b.forward(10)
	b.left(g.sin(i/10)*25)
	b.left(20)

b.end_fill()

turtle.done()