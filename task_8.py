#Task 8 : functions

'''def hello_func():
    pass

print(hello_func())'''

#example 2

def hello_function():
    print('hello world.')
    
    #instead of using print statements we can use the 
    #hello_function() to print multiple statements
    
hello_function()
hello_function()
hello_function()
hello_function()

print(hello_function())



#example 3:

def learn_function():
    
    return 'hello deepak'

print(learn_function().upper())



#example 4:

def learn_function_1(greeting):
    return '{} Greeting'.format(greeting)

print(learn_function_1('Hello'))


#example 5:

def student_1(*args, **kwargs):
    print(args)
    print(kwargs)
    
student_1('hello','deepak', name='vedas', age='20')

#prints tuple and list of directories

#example 6:

def student_2(*args, **kwargs):
    print(args)
    print(kwargs)
    
courses = ('hello', 'deepak')
info = {'name': 'vedas', 'age': '20'} 

#(* -> to pack and ** -> to unpack)
student_2(*courses, **info)

#example 7:

month_days= [0, 31, 28, 31, 30, 31, 30 , 31, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    
    return year % 4 == 0 

def days_in_month(year, month):
    
    if not 1 <= month <= 12:
        return 'invalid month'
    
    if month == 2 and is_leap_year(year):
        return 29
    
    return month_days[month]

print(is_leap_year(2017))

print(days_in_month(2020, 2))
print(days_in_month(2017, 2))

    

