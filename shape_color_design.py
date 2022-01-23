import turtle

shape = turtle.Turtle()

color =["blue", "green", "red", "pink", "yellow", "purple"]

def color_shape(a):
	for i in range(200):
		shape.circle(50, steps=a)
		shape.forward(i)
		shape.color()
		shape.left(45)
color_shape(6)


turtle.done()