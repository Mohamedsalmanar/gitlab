#l1 = [10,20,30]
#l2 = [40,50,60]
#l1.append(40)
#print(len(l1))
#l1.insert(3,25)
#l1.remove(25)
#del l1[1]
#l1.pop()
#l1.extend([25,52])
#print(l1)
#l2.extend('pqrs').extend('xyz')
#print(l2)

#l1 = [100,10,20,30]
#l1.sort(reverse=True)
#print(l1)

#l1 = [100,10,20,30]
#l1.sort(reverse=False)
#print(l1)

#l1 = [100,10,20,30]
#l1.sort()
#print(l1)

#l1 = [100,True,20]
#l1.sort()
#print(l1)

#print(min(l1))
#print(max(l1))
#print(sum(l1))


l1 = [10,20,30]
l2 = l1
print(l2)
l1[0] = 111
print(l2)

print(id(l1))
print(id(l2))
