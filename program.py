def count_of_digits(no):
    count = 0
    while no>0:
        count+=1
        no = no//10 
    return count
