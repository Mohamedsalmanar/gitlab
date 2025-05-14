for k in employee.keys():
    print(k)

for value in employee.values():
    print(value)

for k,v in employee.items():
    print(k, v)

for each_item in employee.items():
    print(type(each_item))

employee = {'name':'raja','dept':'it','city':'chennai'}
empty_dict = {}
empty_dict.update(employee)
print(empty_dict)
