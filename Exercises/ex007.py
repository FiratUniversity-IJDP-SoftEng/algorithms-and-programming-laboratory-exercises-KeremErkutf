# Your Student ID: 240543013
# Your Name and Surname: Kerem Erkut Çiftlikçi

text = input("Enter a text: ")

data = {} # Create an empty dictionary

for char in text:
    data[char] = data.get(char, 0) + 1

for char in sorted(data):
    print(f"{char}: {data[char]}")


