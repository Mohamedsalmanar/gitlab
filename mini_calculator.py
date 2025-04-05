#Mini Calculator: 

print("Simple Calculator")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    print("Result:", round(a / b,2))
else:
    print("Invalid operation")
