import turtle

b = turtle.Turtle()
b.speed(10)

b.color("blue")

for i in range(1000):
	b.forward(10)
	b.left(i%20)
	
	b.penup()

	b.forward(10)
	b.right(45)
	b.left(i%45)

	b.pendown()

turtle.done()