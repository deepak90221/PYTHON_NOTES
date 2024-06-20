#Task 11: Sorting Lists, Tuples, and Objects


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return ' ({}, {}, ${})'.format(self.name, self.age, self.salary)



e1 = Employee("deepak",19, 70000)     
e2 = Employee("deepak1",15, 65000)        
e3 = Employee("deepak2",16, 100000)  

employee = [e1,e2,e3]

def e_sort(emp):
    return emp.salary

employee_sort = sorted(employee, key=lambda emp: emp.salary)  

#employee_sort = sorted(employee, key=attrgetter('sort'))

#from operator import attregetter  

#attrgetter function is used to sort the values


print(employee_sort)

#Note: Python Lambda Functions are anonymous functions means that the function is without a name.

