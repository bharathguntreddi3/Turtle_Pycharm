import turtle

b = turtle.Turtle()

b.hideturtle()

b.speed(0)

b.goto(0,0)

b.begin_fill()
b.fillcolor("blue")
b.circle(50)
b.end_fill()

b.up()
b.right(90)
b.forward(150)
b.setheading(90)
b.down()

b.begin_fill()
b.fillcolor("green")
b.circle(-50)
b.end_fill()

b.up()
b.left(90)
b.forward(150)
b.down()

b.begin_fill()
b.fillcolor("maroon")
b.circle(-50)
b.end_fill()

b.up()
b.right(45)
b.forward(230)
b.down()

b.begin_fill()
b.fillcolor("red")
b.circle(-50)
b.end_fill()

b.up()
b.right(75)
b.forward(230)
b.down()

b.begin_fill()
b.fillcolor("pink")
b.circle(-50)
b.end_fill()

b.up()
b.right(45)
b.forward(230)
b.down()

b.begin_fill()
b.fillcolor("black")
b.circle(-50)
b.end_fill()

b.up()
b.right(25)
b.forward(210)
b.down()

b.begin_fill()
b.fillcolor("yellow")
b.circle(-50)
b.end_fill()

b.up()
b.right(40)
b.forward(200)
b.down()

b.begin_fill()
b.fillcolor("white")
b.circle(-50)
b.end_fill()

b.up()
b.right(65)
b.forward(210)
b.down()

b.begin_fill()
b.fillcolor("purple")
b.circle(-50)
b.end_fill()

b.up()
b.right(50)
b.forward(180)
b.down()


turtle.done()