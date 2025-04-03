#Default Arguments
def login(username, password='test@123'):
    print(username, 'logged in with password', password)

login('admin', 'abcd1234')

login('admin')

#If argument is not given, default value present in function parameter will be considered. 

#Positional Arguments
def login(username, password):
    print(username, 'logged in with password', password)

login('admin', 'abcd1234')

#login('admin') --> Error

#Keyword Arguments
def login(username, password):
    print(username, 'logged in with password', password)

login(password='abcd1234',username='admin')

#login('admin') --> Error

--------
#Variable Length Arguments
def dhoni_score(*no_of_matches):
    print(no_of_matches)
    print(type(no_of_matches))


dhoni_score(32) #Tuple
dhoni_score(32,16)
dhoni_score(32,16, 4)
--------
#Keyword Variable Length Arguments
def dhoni_results(**score):
    print(score)

dhoni_results(mi=30,kkr=32, rr=57) #Dictionary
----------

#How do you find datatype of a variable?
no = 10
print(type(no)) 
#How do you find memory id of a variable?
print(id(no)) 

def add(no1,no2):
    print(no1+no2)

print(add(10,20))
#<function add at 0x7aed6cb63d90> Hexadecimal value

#return datatype: 







