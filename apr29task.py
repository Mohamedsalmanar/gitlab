q = [90,87,65,67,89]
h = [96,97,95,69,99]
a = [99,98,100,76,49]

marks = [q,h,a]

#Task: 
#1) Print q, h, a marks in separate lines
#2) Calculate Total and Percentage of q, h and a
#3) Calculate Average of Tamil (first subject) 
#4) Calculate highest total among these three

#Task 1
#for exams in marks: 
#    print(exams)

#Task 2: Calculate Total and Percentage of q, h and a


for exams in marks: 
	total = 0
	for subject in exams:
		total = subject+total
	print(total)
