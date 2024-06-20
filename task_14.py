import random

#prints random numbers with point values
values = random.uniform(1,10)

#prints random integers
values_1 = random.randint(1,10)

print(values)

print(values_1)

#example 2:

value_strings = ['deepak','vedas','pawan','prem','jathin','neeraj']

output_strings_values = random.choice(value_strings)

print('hi!',output_strings_values)

#example 3:

value =  list(range(1,100))

random.shuffle(value)

#prints three 3 random set values 
handles = random.sample(value, k=3)

print(handles)
print(value)

