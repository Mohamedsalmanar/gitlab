import random

system_no = random.randint(1,100)

while True:
    num=int(input("Enter number between 1 and 100 : "))
    if num == system_no:
        print("COngratualtions!. You have guessed the Correct NUmber ")
        break
    elif num < system_no:
        print("Too Low ! Try again")
    else:
        
        print("Too High ! Try again")
