#1 2 3 4 5 6 7 8 9 10
#RED BLUE

no=1
while no<=10:
    if no%2==0:
        print("Blue")
    else:
        print("Red")
    no=no+1

count = 1
while count<=10:
    if count%2==0 and count%4==0:
        print("GREEN")
    elif count%2==0:
        print("BLUE")
    else:
        print("RED")
    count+= 1



