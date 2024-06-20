class Employee:
    
    raise_amt = 1.04
    number_of_emp = 0
    def __init__(self, first, last, pay):
        
        self.first = first
        self.last = last
        self.email_address_of_emp = first + '.' + last + '@email.com'
        self.pay = pay
        
        Employee.number_of_emp += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    
    raise_amt = 1.10
    def __init__(self, first, last, pay,prog_language):
        #super().__init__(first, last, pay)
        Employee.__init__(self, first, last, pay) 
        self.prog_language = prog_language
        
        
class Manager(Employee):
    def __init__(self, first, last, pay,employee=None):
        #super().__init__(first, last, pay)
        Employee.__init__(self, first, last, pay) 
        if employee is None:
            self.employee = []
            #if employee not found then initialize the value to null 
        else:
            #if found make the employee = employee
            self.employee = employee
        
    def add_employee(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)
            #append()-> to add
        
    def remove_employee(self, emp):
        if emp  in self.employee:
            self.employee.remove(emp)
            #remove()-> to remove
    
    def print_emps(self):
        for emp in self.employee:
            print('->', emp.fullname())
            #prints the employee details
            
   
        


dev_1 = Developer('Deepak', 'Vedas', 50000,'Python')
dev_2 = Developer('Deepak_1', 'Vedas_1', 80000,'JS')

manager_1 = Manager('pawan','rakesh', 900000, [dev_1])

print(manager_1.email_address_of_emp)

print(isinstance(manager_1, Developer))

#tells if a class is subclass of another class or not..

print(isinstance(Developer , Manager))


manager_1.add_employee(dev_1)

manager_1.add_employee(dev_2)

manager_1.remove_employee(dev_2)

manager_1.print_emps()

#print(dev_1.email)
#print(dev_2.prog_language)

#print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)



