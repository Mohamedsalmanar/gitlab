l1=[100,200,300,400]
l2=[10,20,30,40]
for elem in l1:
	print(elem)
l3=[l1,l2]
for inner_list in l3:
	for elem in inner_list:
		print(elem,end =' ')
	print()
