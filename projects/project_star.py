import turtle

star = turtle.Turtle()

b = turtle.Screen()  #created screen object 
b.title("BHARATH_GUNTREDDI") 

star.shape("turtle") 

star.getscreen().bgcolor("black")  #screen object created and background color changed 
star.speed(10)

star.color("red")

star.penup()
star.goto((-100, 100))
star.pendown()


def draw(star, size):
	if size <= 10:
		return 
	else:
		star.begin_fill()
		for i in range(5):
			star.forward(size)
			draw(star, size/3)
			star.left(216)
		star.end_fill()
draw(star,300)

star.hideturtle()

turtle.done()