import turtle 
b = turtle.Turtle()

g = turtle.Screen()
g.bgcolor("black")

b.color("yellow")

b.begin_fill()
b.fillcolor("red")
b.circle(100, 180)  #extent 
b.end_fill()

b.begin_fill()
b.fillcolor("red")
b.circle(100, steps=3)
b.end_fill()

b.begin_fill()
b.fillcolor("red")
b.circle(100, steps=4)
b.end_fill()

b.begin_fill()
b.fillcolor("red")
b.circle(100, steps=5)
b.end_fill()

b.begin_fill()
b.fillcolor("red")
b.circle(100, steps=6)
b.end_fill()








turtle.done()