number = int(input("Enter the no to check if it is prime or not prime"))
number2 = number**0.5
while(number<=number2):
	number%number2 == 0
	print(number,"is prime")
	break;
