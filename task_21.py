#OOPS-Concept-2:
class Employee:
    
    
    number_of_emp = 0
    def __init__(self,first,last,pay):
        
        self.first = first
        self.last = last
        self.pay = pay
        Employee.number_of_emp += 1
    def fullname(self):
            return '{} {}'.format(self.first, self.last)
        
    def apply_raise(self):
        
        self.pay = int(self.pay * 1.04)
            #an increase of 4% of the pay amount
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
            
#before the employee count
print(Employee.number_of_emp)

emp_1 = Employee('Deepak','Chittypolu', 125000)
emp_2 = Employee('Deepak_1','Chittypolu_1', 155000)

print(emp_1 + emp_2)

print(len(emp_1))


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)


#counts and prints the number of employees
print(Employee.number_of_emp)