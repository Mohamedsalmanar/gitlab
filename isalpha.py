s = "a1b2c3"
word = ""
number = ""
for letter in s:
	if letter.isalpha():
		word = word + letter
	else:
		number = number + letter
print(word+number)
