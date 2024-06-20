#Day 9: Import Modules and Exploring The Standard Library


import random

courses = ['cp','devops','mp','C++','Aoop']

random_courses = random.choice(courses)

print(random_courses)


#example 2

import math
rads  = math.radians(90)
print(math.sin(90))

print(math.sqrt(144))

#example 3

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2024))

#example 4

import os 

print(os.getcwd())

print(os.__file__)

# checks where the file is located

#print current directory

