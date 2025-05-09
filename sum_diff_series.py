def find_power(base, power):
	result = 1
	while power > 0:
		result = result *base
		power = power -1
	return result

result = 0
base = 3
power = 0
while power <= 4:
	output = find_power(base, power)
	if power % 2 == 0:
		result = result + output
	else :
		result = result - output
	power += 1
print(result)
