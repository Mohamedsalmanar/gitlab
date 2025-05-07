#nested_tuple=((10,20), (30,40))
#print(nested_tuple[0])
#print(nested_tuple[0][0])
#print(nested_tuple[1][0])

#t = ((10,20) , (30,40))
#print(t[0])
#print(t[0][0])

#t[0][0] = 222
#print(t)

#t = ([10,20],(30,40))
#for l in t :
#	print(l)

#data = ([10,20,30], [40,50,60], [70,80.90])
#print(sum(data[0]),sum(data[1]),sum(data[2]))
#print(data[1])
#print(data[0][1], data[1][1], data[2][1])

#List_wise_total = [sum(lst) for lst in data]
#print(tuple(list_wise_total))
#sec_list = data[1]
#print(sec_list)
#sec_list_every = [lst[1] for lst in data]
#print(sec_list_every)

numbers = (no for no in range(1,11))
print(numbers)

numbers = (no for no in range(1,11))
for number in numbers:
	print(number)
