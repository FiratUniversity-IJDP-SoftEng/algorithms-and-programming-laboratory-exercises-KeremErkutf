# Your Student ID: 240543013
# Your Name and Surname: Kerem Erkut Çiftlikçi

def get_choice():
    print("1. C to F: Convert Celsius to Fahrenheit")
    print("2. F to C: Convert Fahrenheit to Celsius")
    return input("Enter your choice: ")

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

choice = get_choice()
if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius} Celsius is {celsius_to_fahrenheit(celsius)} Fahrenheit.")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit} Fahrenheit is {fahrenheit_to_celsius(fahrenheit)} Celsius.")

