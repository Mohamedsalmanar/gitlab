#def find_power(base,power):
#	result = 1
#	while power>=1:
#		result = result * base
#		power-=1
#	return result
#result = find_power(2,5)
#print(result)

def find_power(base,power):
	result=1
	while power>0:
		result = result*base
		power-=1
	print(result,"hi")
	return result
result = 0
base = 3
power = 0
while power<=4:
	output=find_power(base,power)
	print(output,end=' ')
	power+=1
	if power%2==0:
		result=result+output
	else:
		result = result-output
