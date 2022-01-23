import turtle
b = turtle.Turtle()  #adds an arrow

b.shape("turtle")   #changes the shape of the point

# b.colormode(255)  #to set color code to rgb

'''
b.forward(100)  #moves the arrow forward
b.left(45)   #rotates 45 degrees
b.forward(100)   #and agian moves forward
b.right(90)   #moves right 90 degrees
b.forward(100) #moves forward
'''

b.color("blue", "red", )

b.begin_fill()

for i in range(4):
	b.forward(50)
	b.left(90)


b.penup()  #jumps to the next line doesnt draw a line
b.forward(100)
b.pendown()



for i in range(4):
	b.forward(50)
	b.left(90)


b.penup()
b.forward(100)
b.pendown()

for i in range(4):
	b.forward(50)
	b.left(90)

b.end_fill()

turtle.done()






 