print("Welcome to mini Calculator")
no1 = float(input("Enter the first number:"))
no2 = float(input("Enter the second number:"))
ops = input("what operation would you like to perform +, -, *, /: ")

if ops == '+':
    print("Result:", round(no1+no2,2))
elif ops == '-':
    print("Result:", round((no1-no2),2)
elif ops == '*':
    print("Result:", round((no1*no2),2)
elif ops == '/':
    print("Result:", round(no1/no2,2))
else:
    print("Invalid input")
