# Your Student ID: 240543013
# Your Name and Surname: Kerem Erkut Çiftlikçi

numbers = list(range(1, 11))

print("Original list:", numbers)

reversed_numbers = numbers[::-1]
print("Reversed list:", reversed_numbers)

numbers.extend([11, 12, 13])
print("Extended list:", numbers)

print("The length of the list:", len(numbers))

numbers.pop(0)
numbers.pop(-1)
print("Popped list:", numbers)

even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)