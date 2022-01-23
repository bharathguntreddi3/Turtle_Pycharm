import turtle

inf = turtle.Turtle()

b = turtle.Screen()

b.bgcolor("black")

inf.color("skyblue")

inf.right(45)

inf.speed(0)

for i in range(155):

	inf.circle(30)

	if 7 < i < 65:
		inf.left(5)
	if 85 < i <138:
		inf.right(5)
	if i < 85:
		inf.forward(10)
	else:
		inf.forward(5)


turtle.done()