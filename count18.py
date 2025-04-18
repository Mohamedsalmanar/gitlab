def count_of_digits(no):
    count = 0
    while no>0:
        count+=1
        no = no//10 #123
    return count

def find_power(base, power):
    result = 1
    while power>=1:
        result = result * base
        power-=1 #power = power - 1
    return result

def find_armstrong(no, power): #153
    armstrong = 0
    while no>0:
        rem = no%10     #3
        armstrong = armstrong + find_power(rem,power)
        no = no//10 #123
    return armstrong
    

no = int(input("Enter no. ")) #153
count = count_of_digits(no)
result = find_armstrong(no, count)

if no == result:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
