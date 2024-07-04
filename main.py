import random
import string
print("Welcome to the 'Random Password Generator'")
length = int(input("Enter length of Password: "))
print('''Choose characters to set a Password:
            1. Alphabets
            2. Numbers
            3. Special characters
            4. Exit''')
characterList = " "
while(True):
    choice = int(input("Select the Number:"))

    if choice == 1:
      characterList += string.ascii_letters
    elif choice == 2:
        characterList += string.digits
    elif choice == 3:
        characterList += string.punctuation
    elif choice == 4:
        break
    else:
      print("please select a valid option!")

password = []

for i in range(length):
    randomchar = random.choice(characterList)

    password.append(randomchar)

print("The random password is " + "".join(password))










