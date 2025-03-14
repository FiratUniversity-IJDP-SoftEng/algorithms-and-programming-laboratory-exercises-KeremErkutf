# Your Student ID: 240543013
# Your Name and Surname: Kerem Erkut Çiftlikçi

n = int(input("Enter a number: "))
for i in range(n):
    space = " " * (n - i)
    star = "*" * (2 * i - 1)
    print(space + star)

