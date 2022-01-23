import turtle
b = turtle.Turtle()

b.speed(100)

b.color("red", "yellow")

b.begin_fill()

for i in range(100):  #for loop for the number of iterations of lines
	b.forward(100)
	b.left(167)   #each iteration with 167 degrees

b.end_fill()  #color fill

b.hideturtle()

turtle.done()