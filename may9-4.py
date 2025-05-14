def fin_power(base,power):
	result=1
	while power>=1:
		result=result*base
		power-=1
	return result

result=find_power(2,5)
print(result)
