#You’re building a program to manage a line of students waiting outside a classroom. 
#You can add new students, insert someone who cuts in line, remove a student who leaves, and pop the last student who got tired and left.
line = ['Alice','Alice','Bob','Charlie']
line.append('Drake')
print(line)
line.insert(1, 'Evans')
print(line)
line.pop(1)
print(line)
line.sort()
print(line)
line = [name for name in line if name != 'Alice']
print(line)
line.remove('Alice')
print(line)
#list to find cubes of first 10 natural numbers
#long form
cubes = []
for no in range(1,11):
	cubes.append(no**3)
print(cubes)

#simple form
cubes = [no**3 for no in range(1,11)]
print(cubes)
