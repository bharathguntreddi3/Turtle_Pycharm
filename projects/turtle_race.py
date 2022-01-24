import turtle
import random

race = turtle.Turtle()

start_race = False
race.shape("turtle")
b = turtle.Screen()
bet = b.textinput(title = "Bet On A Turtle", prompt = "Enter the Turtle color and the bet amount :")
colors = ["red", "green", "blue", "yellow", "orange", "pink"]
position = [-70, -40, -10, 20, 50, 80]
turtles =[]

for i in range(0, 6):
	race.color(colors[i])
	race.up()
	race.goto(-230, position[i])
	race.down()
	turtles.append(turtles)

if bet:
	start_race = True 

while start_race:
	for race in turtles:
		if race.xcor() > 230:
			start_race = False
			win_color = race.pencolor()
			if win_color == bet:
				print(" &d is the winner, you won the bet " % (win_color))
			else:
				pirnt("&d is the winner , you lost the bet " % (win_color))

		distance = random.randint(0, 10)
		race.forward(distance)

turtle.done()