#1)
s = 'a1b2c3'
letters = []
for char in s:
    if char.isalpha():
        letters.append(char)
print(letters)
s='a1b2c3'
letters = [char for char in s if char.isalpha()]
print(letters)

#2)
#input: a4k3b2
#output: aeknbd

s='a4k3b2'
output = ''
for letter in s:
    if letter.isalpha():
        output = output + letter
        previous = letter 	
    else:
        no = int(letter)
        alpha = chr(ord(previous)+no)
        output+=alpha
print(output)

print(ord('a'))

print(ord('b'))

print(chr(ord('a')+1))
