import random 

sum1 = 0
sum2 = 0
count = 0
temp = 0

while(1):
	n = random.randrange(1,10)
	m = random.randrange(1,10)


	sum1 = sum1 + n 
	count = count + 1 

	print("player 1 turn" ,count, "score :", sum1)

	if(sum1 >= 100):
		temp =1 
		break

	print("player 2 turn" ,count, "score :", sum2)
	if(sum2 >= 100):
		temp = 2 
		break

if(temp == 1):
	print("playe 1 wins ")
else:
	print("player 2 wins ")
