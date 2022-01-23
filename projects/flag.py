import turtle
flag = turtle.Turtle()

b = turtle.Screen()
b.bgcolor("red")

def stick():
	flag.pensize(3)
	flag.goto(0, -500)
	flag.goto(0, 300)

stick()

def flag_color(color):
	for i in range(2):
		flag.color(color)
		flag.begin_fill()
		flag.fillcolor(color)
		flag.forward(400)
		flag.right(90)
		flag.forward(80)
		flag.right(90)
		flag.end_fill()
		
flag_color("orange")

flag.goto(0, 220)
flag_color("white")		

flag.goto(0, 140)
flag_color("green")

flag.forward(200)

flag.color("blue")
flag.circle(40)

flag.left(90)
flag.forward(40)


def chakra():
	for i in range(24):
		flag.forward(40)
		flag.backward(40)
		flag.left(15)

flag.hideturtle()

chakra()













turtle.done()