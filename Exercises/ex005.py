# Your Student ID: 240543013
# Your Name and Surname: Kerem Erkut Çiftlikçi

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
length_of_first_name = len(first_name ) + 3

greeting = "Hi"
formatted_output = f"{greeting:<{length_of_first_name}}{last_name}\n  {first_name}"

print("\n" + formatted_output)
