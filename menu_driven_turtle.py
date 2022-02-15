import turtle 
import random 
b = turtle.Turtle()
s = turtle.Screen()
s.title("BHARATH_GUNTREDDI")
design = s.textinput(title = "graphic designs", prompt = "enter a number : 1.Among b, 2.flag, 3.infinity, 4.squarelamo, 5.mixspiral, 6.squarespiral, 7.starpix")
#Among us pattern
if design == 1:
	def character():
		b.pensize(10)
		b.color("red")
		b.begin_fill()
		b.fillcolor("red")

		# b.speed(0)

		b.up()
		b.goto(0, -100)
		b.down()

		b.left(90)
		b.forward(300)

		b.right(180)
		b.circle(100, -180)

		b.right(180)
		b.forward(300)

		b.right(180)
		b.circle(25, -180)

		b.right(180)
		b.forward(150)

		# b.right(180)
		b.circle(50, -180)

		b.forward(150)

		b.right(180)
		b.circle(25, -180)

		b.end_fill()



	def goggle():

		b.pensize(10)
		b.color("blue")
		b.up()
		b.goto(200, 200)
		b.down()

		# b.speed(0)

		b.begin_fill()
		b.fillcolor("blue")
		b.right(90)
		b.circle(25, -180)

		b.right(180)
		b.forward(120)

		b.right(180)
		b.circle(25, -180)

		b.right(180)
		b.forward(120)
		b.end_fill()



	def bag():

		b.pensize(10)
		b.up()
		b.home()
		b.down()

		# b.speed(0)

		b.color("red")

		b.begin_fill()
		b.fillcolor("red")

		b.left(90)
		b.forward(50)
		b.left(360)
		b.circle(25, -180)

		b.right(180)
		b.forward(100)

		b.right(180)
		b.circle(25, -180)

		b.right(180)
		b.forward(100)

		b.end_fill()

	character()

	goggle()

	bag()

#flag pattern
if design == 2:

	def stick():
		b.pensize(3)
		b.goto(0, -500)
		b.goto(0, 300)

	stick()

	def flag_color(color):
		for i in range(2):
			b.color(color)
			b.begin_fill()
			b.fillcolor(color)
			b.forward(400)
			b.right(90)
			b.forward(80)
			b.right(90)
			b.end_fill()
			
	flag_color("orange")

	b.goto(0, 220)
	flag_color("white")		

	b.goto(0, 140)
	flag_color("green")

	b.forward(200)

	b.color("blue")
	b.circle(40)

	b.left(90)
	b.forward(40)


	def chakra():
		for i in range(24):
			b.forward(40)
			b.backward(40)
			b.left(15)

	b.hideturtle()

	chakra()

#infinity pattern
	if design == 3:
		b.color("skyblue")

	b.right(45)

	b.speed(0)

	for i in range(155):

		b.circle(30)

		if 7 < i < 65:
			b.left(5)
		if 85 < i <138:
			b.right(5)
		if i < 85:
			b.forward(10)
		else:
			b.forward(5)

if design == 4:
	def pot():
		for i in range(500):
			turtle.colormode(255)

			r = random.randint(0, 255)
			g = random.randint(0, 255)
			b = random.randint(0, 255)

			b.color(r, g, b)

			b.forward(i)
			b.right(100)

	pot()


if design == 5:
	sq.left(45)

def sq1():
	for i in range(300):
		turtle.colormode(255)
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)

		b.pencolor(r, g, b)
		b.forward(i )
		b.right(90)

sq1()

sq.left(90)

	def sq2():
		for i in range(100):
			turtle.colormode(255)
			r = random.randint(0, 255)
			g = random.randint(0, 255)
			b = random.randint(0, 255)

			b.pencolor(r, g, b)
			b.forward(i )
			b.right(90)

	sq2()

	b.forward(100)
	b.right(90)
	b.forward(100)
	b.right(90)
	b.forward(50)
	b.left(90)
	b.forward(250)

	sq2()

	b.right(90)
	b.forward(100)
	b.left(90)
	b.forward(50)
	b.right(90)
	b.forward(250)

	sq2()

	b.right(90)
	b.forward(100)
	b.left(90)
	b.forward(50)
	b.right(90)
	b.forward(250)

	sq2()

	b.hideturtle()





















turtle.done()