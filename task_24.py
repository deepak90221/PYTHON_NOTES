#OOPS-Concept-2:
class Employee:
    
    
    
    def __init__(self,first,last,pay):
        
        self.first = first
        self.last = last
        self.pay = pay
        
        def fullname(self):
            return '{} {}'.format(self.first, self.last)
        
        def apply_raise(self):
            self.pay = int(self.pay * 1.04)
            
       
            
emp_1 = Employee('Deepak','Chittypolu', 125000)
emp_2 = Employee('Deepak_1','Chittypolu_1', 175000)


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


