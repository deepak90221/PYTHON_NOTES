#OOPS-Concept-1:

class Employee:
    def __init__(self,firstname,lastname,email,pay):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.pay = pay
    def fullname(self):
        return ('{} {}'.format(self.firstname, self.lastname))
    

emp_1 = Employee('Deepak','Chittypolu','kingdeepak010@gmail.com',200000)

print(emp_1.firstname,emp_1.lastname)

print('{} {}'.format(emp_1.firstname,emp_1.lastname))

print(emp_1.fullname())