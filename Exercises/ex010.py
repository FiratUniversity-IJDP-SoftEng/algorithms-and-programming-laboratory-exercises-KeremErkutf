def get_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a, b

def choice():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    return int(input("Enter your choice: "))

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

a, b = get_numbers()
ch = choice()

if ch == 1:
    print(add(a, b))
elif ch == 2:
    print(subtract(a, b))
elif ch == 3:
    print(multiply(a, b))
elif ch == 4:
    print(divide(a, b))
else:
    print("Invalid choice!")
