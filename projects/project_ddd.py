import turtle
import random
ddd = turtle.Turtle()

b = turtle.Screen()
b.bgcolor('black') 
ddd.speed(0) 
turtle.title("rgb spiral design")
ddd.hideturtle()

def spiral():

     x = 1 

     while x < 400: 
       
          r = random.randint(0,255) 
          g = random.randint(0,255)  
          b = random.randint(0,255) 
           
          turtle.colormode(255)  
          ddd.pencolor(r,g,b) 
          ddd.forward(x) 
          ddd.right(90.991) 
          x = x+1 

spiral()
      
turtle.done() 
