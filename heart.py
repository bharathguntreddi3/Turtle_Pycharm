import turtle
heart = turtle.Turtle()

b = turtle.Screen()
b.bgcolor("black")

turtle.title("BHARATH_GUNTREDDI")

heart.color("red")

heart.up()
heart.goto(0, -100)
heart.down()

heart.begin_fill()

heart.fillcolor("red")
heart.left(140)
heart.forward(300)
heart.circle(-90, 200)
heart.left(120)
heart.circle(-90,200)
heart.forward(300)
heart.goto(0,-100)

heart.end_fill()






turtle.done()