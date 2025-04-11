#guess the number
import random
random_no = random.randint(1,10)

while True: #11 is less than 10 true/false
	num = input("Enter the number between 1 and 10")
	if num == random_no:
		print("you guessed the right number")
		break;
	else:
		print("please try again")
