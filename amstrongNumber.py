number = int(input("Enter a number to check if it is amstrong number: "))
number_of_digits = len(str(abs(number)))
dup_number = number
digit = []
while number > 0:
	digit.append(number%10)
	number = number//10
sum_of_powers = 0
for num in digit:
	sum_of_powers += num**number_of_digits

if sum_of_powers == dup_number:
	print(dup_number, "is an amstrong number")
else:
	print(dup_number, "is not an amstrong number")
