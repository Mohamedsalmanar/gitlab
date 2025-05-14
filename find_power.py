base = int(input("Enter the Base number: "))
power = int(input("Enter the power: "))

def findpower(base,power):
	result = 1
	while power>=1:
		result = base * result
		power = power - 1
	return result

print(findpower(base,power))
