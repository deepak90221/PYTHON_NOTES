SIZE = 3  
stack = [None] * SIZE  
top = -1  

def push(element):  
    global top  
    if top < SIZE - 1:  
        top += 1  
        stack[top] = element  
        print(f"Element {element} pushed to stack.")  
    else:  
        print("Stack Overflow")  

def pop():  
    global top  
    if top >= 0:  
        element = stack[top]  
        top -= 1  
        print(f"Element {element} popped from stack.")  
        return element  
    else:  
        print("Stack Underflow")  
        return -1  

while True:  
    print("\n1. Push\n2. Pop\n3. Display Stack\n4. Exit")  
    choice = input("Enter your choice: ")  
    
    if choice == '1':  
        value = input("Enter the value to push: ")  
        push(value)  
    elif choice == '2':  
        pop()  
    elif choice == '3':  
        print("Current Stack:", stack[:top + 1])  
    elif choice == '4':  
        print("Exiting...")  
        break  
    else:  
        print("Invalid choice. Please enter 1, 2, 3, or 4.")  
