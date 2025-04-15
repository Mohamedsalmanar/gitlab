name = input("What is your name: ")

#Incorrect Name: 
# Welcome to Python 

Actual_Name="Suresh"
while True:
    user_Name=input("Enter Your Name: ")
    if Actual_Name!=user_Name:
        print("Name is not matched. Please Try again")
    else:
        print("Name is matched. Welcome to Python")
        break
