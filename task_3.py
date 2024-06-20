#Task 3: Lists, Tuples, and Sets

courses = ['EP','Networks','Mp','Aiml']
courses_1 = ['Cloud', 'Ese']

print(len(courses))

print(courses[0])

print(courses[0:3])

courses.insert(0, 'Mern')

courses.insert(1, courses_1)

courses_1.extend(courses_1)

print(courses)

courses_1.sort(reverse=True)

num = [4,3,1,2,7,9,8]

num.sort(reverse=True)

print(max(num))

print(min(num))

print(courses.index('Mp'))

#checking the existance of that perticular data or not
print('Mp' in courses)

#using loop to display the data 
for item in courses:
    print(item)
    
    
"""using enumaerate
enumaerate : The enumerate function in python is a built-in function that returns an enumerate object, 
which is an iterator that yields pairs of index and value for each item in a sequence.
"""
for index, item in enumerate(courses):
    print(index, item)
    
#(start) : THis is used to start the enumeration from '1'

for index, item in enumerate(courses, start=1):
    print(index, item)
    
manage_courses = ['Django','Devops','Machine Architecture']


manage_str = ' - '.join(manage_courses)

new_list = manage_str.split(' - ')

print(manage_str)
print(new_list)

#Sets : They dont care about the order prints the order randomnly

c_courses = {'EP','Networks','Mp','Aiml'}
cs_courses = {'EP','Networks','Geo', 'Chem'}
print(c_courses)

print(c_courses.intersection(cs_courses)) # A n B

print(c_courses.difference(cs_courses)) # A - B

print(c_courses.union(cs_courses)) #A u B