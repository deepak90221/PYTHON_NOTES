def divide(a,b):
    
    try:
        answer = a / b
    except ZeroDivisionError:
        print("Error")
    else:
        print(answer)
    finally:
        print("This is always executed!")
        
divide(6,2)


#example 2:

try:
	x = int(input("Enter a number: "))
	result = 10 / x
except ZeroDivisionError:
	print("You cannot divide by zero.")
except ValueError:
	print("Invalid input. Please enter a valid number.")
except Exception as e:
	print(f"An error occurred: {e}")
