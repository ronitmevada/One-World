# Simple Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

print("=== Simple Calculator ===")
print("Operations:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
print("5. Exit")

while True:
    choice = input("\nEnter operation (+, -, *, /) or 'q' to quit: ")

    if choice.lower() == 'q':
        print("Calculator closed.")
        break

    if choice not in ('+', '-', '*', '/'):
        print("Invalid input! Please enter +, -, *, / or q.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        continue

    if choice == '+':
        print(f"Result: {add(num1, num2)}")
    elif choice == '-':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '*':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '/':
        print(f"Result: {divide(num1, num2)}")
