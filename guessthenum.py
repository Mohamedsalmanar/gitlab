import random
system_no=random.randint(1,10)

while True: # 11 is less than 10 True / False
    num=int(input("Enter number between 1 to 10: "))
    if num==system_no:
        print("You guessed the right number")
        break
    else:
        print("Please try again")
