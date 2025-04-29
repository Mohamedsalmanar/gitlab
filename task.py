q = [90,87,65,67,89]
h = [96,97,95,69,99]
a = [99,98,100,76,49]

marks = [q,h,a]

#Task: 
#1) Print q, h, a marks in separate lines
#2) Calculate Total and Percentage of q, h and a
#3) Calculate Average of Tamil (first subject) 
#4) Calculate highest total among these three

#i = 0
#total = 0
#while i < 5:
#	total = q[i] + total 
#	i = i + 1
#print(total)


total=0
for exam in marks:
	for subject in exam:
		print(subject)



