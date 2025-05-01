#len

l1 = [1, 2, 3, 4, 5]
print(len(l1))

l2 = [6, 7, 8, 9, 10]
l1.append(l2)
print("Append:", l1)

l1 = [1,2,3,4,5]
l1.extend(l2)
print("Extend:", l1)

l2.append("abcd")
print("append: ", l2)
l2.extend("abcd")
print("extend: ", l2)

print(l1)
del l1[0]
print("Deleted", l1)

l1.pop()
print(l1)

l2.extend("pqrs")
print(l2)

l2.reverse()
print(l2)


l1 = [100,True,20]
l1.sort()
print(l1)

l1 = [100, 10, 20, 30]
l1.sort(reverse=True)
print(l1)

l1 = [100, 10, 20, 30]
l1.sort(reverse=False)
print(l1)
