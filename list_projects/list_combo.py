l1 = [1,2,3]
l2 = [3,1,4]
l3 = [7,8,9]
#output = [1,2,3,4,5,6]
l3 = [l1]+[l2]+[l3]
print(l3)
print(l1)
l1.extend([4,5,6])
print(l1)
#create a combo where each l1,l2 is combined
#output [(1,2)(2,3)....
l1=[1,2,3]
l4 = []
for num1 in l1:
	for num2 in l2:
		if num1 != num2:
			l4.append((num1, num2))
print(l4)
#Same using List comprehension
l4 = [(num1,num2) for num1 in l1 for num2 in l2 if num1!=num2] 
print(l4)

l3 = list(zip(*l3))
print(l3)
