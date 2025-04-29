#l=[10,20,30,40,50,60,70,80]
#print(l[0:3])
#print(l[2:5])
#print(l[2::2])
#print(l[6:2:-1])
#print(l[6:2:-2])

#l1=[10,20,30]
#l2=[30,20,10]
#l3 = l1+l2
#print(l3)

#print(l3*3)

l1 = [10,20,30]
l2 = [30,20,10]
l3 =[]
#l3.append(l1[0] + l2[0])
#l3.append(l1[1] + l2[1])
#l3.append(l1[2] + l2[2])

#print(l3)

i = 0
while i<3:
	l3.append(l1[i] + l2[i])
	i=i+1

print(l3)
	
