name = input("enter your password: ")
password = len(name)

if password <=8:
    print("your password is short")
if password >=10:
    print("your password is long")
if password == 9:
    print("your password is valid")
