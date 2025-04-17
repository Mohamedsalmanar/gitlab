def find_power(base, power):
    result = 1
    while power>=1:
        result = result * base
        power-=1 #power = power - 1
    return result

print(find_power(5,2))

