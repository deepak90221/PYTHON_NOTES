#Task 5:  Conditionals and Booleans - If, Else, and Elif Statements

language = 'python'

if language == 'javascript':
    print(' yes, matched!')
elif language == 'python':
    print(' yes, matched! with python')
    
elif language == 'c++':
    print(' yes, matched! with with the language')
else:
    print(' no, matched!')
    
    
#example 2

user = 'Login'
password = False

if user == 'Login' and password:
    print(' yes, matched!')
else:
    print(' no, matched!')