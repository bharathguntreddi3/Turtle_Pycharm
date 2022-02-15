import turtle

tuxedo = turtle.Turtle()
tuxedo.speed(0)
colors = ["red", "blue", "yellow", "green", "orange"]
for i in range(100):
	tuxedo.color(colors[i%5])
	tuxedo.pensize(5)
	tuxedo.forward(i)
	tuxedo.left(60)

turtle.done()