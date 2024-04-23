def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def calculator():
    print("Welcome to Simple Calculator!")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Choose operation \n1. +\n2. -\n3. *\n4. /\n ")

            if operation == '+':
                print("Result:", add(num1, num2))
            elif operation == '-':
                print("Result:", subtract(num1, num2))
            elif operation == '*':
                print("Result:", multiply(num1, num2))
            elif operation == '/':
                print("Result:", divide(num1, num2))
            else:
                print("Invalid operation. Please try again.")
            
            repeat = input("Do you want to perform another calculation? (yes/no): ").lower()
            if repeat!= 'yes':
            
                break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

calculator()
