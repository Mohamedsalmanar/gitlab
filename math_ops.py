s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}

print("Set 1 = ", s1,"\n""Set 2 =", s2)

print("Union: ", s1.union(s2))

print("Intersection", s1.intersection(s2))

print("Difference: ", s1.difference(s2))
print(s1 - s2)

print("Symmetric_difference:", s1.symmetric_difference(s2))
print(s1 ^ s2)

print(20 in s1)

print(20 not in s1)

#Adding elements in set:
s = { 'Hi', True, 5}
s.add(200)
print(s)

#Removing elements in set:
s.remove('Hi')
print(s)

#Randomly removing elements
print(s.pop())
print(s)

#clear
print(s.clear())
