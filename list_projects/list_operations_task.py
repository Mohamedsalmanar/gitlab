list = []
while True:
	user = int(input("1. Add Student \n2. Insert Student \n3. Remove Student \n4. Pop Last Student \n5. Show line \n6. Exit\n"))
	if user == 1:
		name = input("Enter the name to add in list:")
		list.append(name)
	elif user == 2:
		index = int(input("Enter the index in list:"))
		name = input("Enter the name to insert in list:")
		list.insert(index, name)
	elif user == 3:
		name = input("Enter the name of the student to remove:")
		list.remove(name)
	elif user == 4:
		list.pop()
	elif user == 5:
		print(list)
	elif user == 6:
		break
	else:
		print("Choose from the given options:")
