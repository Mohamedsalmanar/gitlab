l1 = [10,20,30]
l2 = l1
print(id(l1))
print(id(l2))
l3 = list(l1)
print(id(l1))
print(id(l3))

print(l1 == l2)
print(l1 is l2)
print(l1 == l3)
print(l1 is l3)
