s = 'a1b2c3'
alpha = ''
numbers = ''
for letter in s:
    if letter.isalpha():
        alpha = alpha+letter
    else:
        numbers = numbers + letter
print(alpha+numbers)

#Comprehensive approach: 
s='a1b2c3'
letters = [char for char in s if char.isalpha()]
nums = [no for no in s if no.isdigit()]
output = ''.join(letters+nums)
print(output)
        
