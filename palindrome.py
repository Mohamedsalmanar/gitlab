no = int(input("Enter the number to check"))
no2 = no
reverse = 0
while no > 0:
	rem = no%10 
	reverse = (reverse * 10) + rem
	no = no//10
if no2 == reverse:
	print(no2, "This is palindrome")
else:
	print(no2, "Not a palindrome")
