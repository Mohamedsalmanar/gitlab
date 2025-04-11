def eb_reading():
    units = 120
    return units

def calculate_amount(unit):
    if unit<100:
        print('Free')
    elif unit<200:
        print(unit * 1.20)
    elif unit<300:
        print(unit * 2)


consumed_units = eb_reading()

calculate_amount(consumed_units)



