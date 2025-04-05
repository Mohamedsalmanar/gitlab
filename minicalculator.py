print("Welcome to mini Calculator")
no1 = int(input("Enter the first number:"))
no2 = int(input("Enter the second number:"))
ops = input("what operation would you like to perform +, -, *, /: ")

if ops == '+':
    print("Result:", no1+no2)
elif ops == '-':
    print("Result:", no1-no2)
elif ops == '*':
    print("Result:", no1*no2)
elif ops == '/':
    print("Result:", no1/no2)
else:
    print("Invalid input")
