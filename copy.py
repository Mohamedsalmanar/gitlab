#Deep Copy
l1 = [10,20,30]
l2 = l1
print(l2)
l1[0] = 111
print(l2)

print(id(l1))

print(id(l2))
