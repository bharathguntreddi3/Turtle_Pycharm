import turtle

b = turtle.Turtle()

b.getscreen().bgcolor("black")
# b.title("BHARATH_GUNTREDDI")

b.speed(0)

def circle(x, y, color, radius):
	b.up()
	b.goto(x, y)
	b.down()

	b.begin_fill()
	b.fillcolor(color)
	b.circle(radius)
	b.end_fill()

	b.up()
	b.home()
	b.down()

circle(0, -50, "blue", 50)

circle(400, 200, "green", 60)

circle(400, -200, "pink", -50)

circle(-400, -200, "red", -50)

circle(-400, 200, "yellow", 50)

# circle(-400, 200, "yellow", -50)

# circle(150, 100, "yellow", +50)

# circle(-100, 99, "yellow", -50)

# circle(-200, 200, "yellow", -50)

# circle(0, 0, "yellow", -50)

# circle(-150, 150, "yellow", 50)

# circle(-90, 123, "yellow", 50)


# b.up()
# b.goto(400,200)
# b.down()

# b.begin_fill()
# b.fillcolor("green")
# b.circle(50)
# b.end_fill()

# b.up()
# b.home()
# b.down()

# b.up()
# b.goto(400,-200)
# b.down()

# b.begin_fill()
# b.fillcolor("pink")
# b.circle(-50)
# b.end_fill()

# b.up()
# b.home()
# b.down()

# b.up()
# b.goto(-400,-200)
# b.down()

# b.begin_fill()
# b.fillcolor("red")
# b.circle(-50)
# b.end_fill()

# b.up()
# b.home()
# b.down()

# b.up()
# b.goto(-400,200)
# b.down()

# b.begin_fill()
# b.fillcolor("yellow")
# b.circle(50)
# b.end_fill()



turtle.done()