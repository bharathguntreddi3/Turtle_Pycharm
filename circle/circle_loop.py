import turtle

b = turtle.Turtle ()
b.speed(0)
b.up()
b.goto(-300, -300)
color1 = ["red", "blue", "yellow", "green"]
for i in range(4):
	b.down()
	b.begin_fill()
	b.circle(50)
	b.color(color1[i])
	b.end_fill()
	b.up()
	b.forward(100)
	b.down()

b.up()
b.forward(-50)
b.setheading(90)
b.forward(100)
for i in range(4):
	b.up()
	b.forward(100)
	b.down()
	b.down()
	b.begin_fill()
	b.circle(50)
	b.color(color1[i])
	b.end_fill()

b.up()
b.forward(150)
b.left(135)
b.forward(170)
for i in range(4):
	b.up()
	b.forward(100)
	b.down()
	b.down()
	b.begin_fill()
	b.circle(50)
	b.color(color1[i])
	b.end_fill()
	
turtle.done()