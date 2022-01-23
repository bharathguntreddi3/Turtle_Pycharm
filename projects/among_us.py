import turtle

us = turtle.Turtle()

b = turtle.Screen()

b.bgcolor("black")



#us.speed(0)

def character():
	us.pensize(10)
	us.color("red")
	us.begin_fill()
	us.fillcolor("red")

	# us.speed(0)

	us.up()
	us.goto(0, -100)
	us.down()

	us.left(90)
	us.forward(300)

	us.right(180)
	us.circle(100, -180)

	us.right(180)
	us.forward(300)

	us.right(180)
	us.circle(25, -180)

	us.right(180)
	us.forward(150)

	# us.right(180)
	us.circle(50, -180)

	us.forward(150)

	us.right(180)
	us.circle(25, -180)

	us.end_fill()



def goggle():

	us.pensize(10)
	us.color("blue")
	us.up()
	us.goto(200, 200)
	us.down()

	# us.speed(0)

	us.begin_fill()
	us.fillcolor("blue")
	us.right(90)
	us.circle(25, -180)

	us.right(180)
	us.forward(120)

	us.right(180)
	us.circle(25, -180)

	us.right(180)
	us.forward(120)
	us.end_fill()



def bag():

	us.pensize(10)
	us.up()
	us.home()
	us.down()

	# us.speed(0)

	us.color("red")

	us.begin_fill()
	us.fillcolor("red")

	us.left(90)
	us.forward(50)
	us.left(360)
	us.circle(25, -180)

	us.right(180)
	us.forward(100)

	us.right(180)
	us.circle(25, -180)

	us.right(180)
	us.forward(100)

	us.end_fill()

character()

goggle()

bag()



turtle.done()