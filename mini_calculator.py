#Mini Calculator: 

print("Simple Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
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

