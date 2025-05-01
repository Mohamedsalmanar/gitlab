s = "a1b2c3"
word = ""
number = ""
for letter in s:
	if letter.isalpha():
		word = word + letter
	else:
		number = number + letter
print(word+number)
s = 'a1b2c3'
letters = []
for char in s:
    if char.isalpha():
        letters.append(char)
print(letters)

s='a1b2c3'
letters = [char for char in s if char.isalpha()]
print(letters)
