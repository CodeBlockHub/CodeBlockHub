# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

# User Interface
def calculator_interface():
    print("Simple Calculator")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    choice = input("Select an operation (1/2/3/4): ")

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if choice == '1':
        print(f"The sum is {add(a, b)}.")
    elif choice == '2':
        print(f"The difference is {subtract(a, b)}.")
    elif choice == '3':
        print(f"The product is {multiply(a, b)}.")
    elif choice == '4':
        print(f"The quotient is {divide(a, b)}.")
    else:
        print("Invalid choice.")

# Run the interface
calculator_interface()