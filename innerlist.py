l1 = [10, 20, 30, 40]
l2 = [100, 200, 300, 400]
l3 = [l1, l2]
for innerlist in l3:
	for elem in innerlist:
		print(elem, end = ' ')
print()
