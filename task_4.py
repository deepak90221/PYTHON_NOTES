# Task 4: Working with Directories


students = { 'name': 'Deepak', 'age': 23, 'courses': ['Math', 'Compsci']}

print(students.get('name'))

students['phone'] = '9398176161'

students.update({'name': 'Dharma', 'age':'34'})

print(students.keys())

print(students.values())

print(students.items())

for key,values in students.items():
    print(key, values)

print(students)