import os
import random
from random import shuffle

os.system('cls')

def password(size,specialChars,numbers):
	speical_chars_list = ["!","@","#","$","%","^","&","*","-","+","_","="]
	number_digis = ["0","1","2","3","4","5","6","7","8","9"]
	letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
				"p","q","r","s","t","u","v","w","x","y","z"]
	password = []
	password_size = size - specialChars - numbers
	
	for i in range(specialChars):
		password.append(speical_chars_list[random.randrange(len(speical_chars_list))])

	for i in range(numbers):
		password.append(number_digis[random.randrange(len(number_digis))])

	for i in range(password_size):
		password.append(letters[random.randrange(len(letters))])

	return password

#Main Program
size = int(input("What's the minium length? "))
speical_chars = int(input("How many special characters? "))
numbers = int(input("How many numbers? "))
password = password(size,speical_chars,numbers)
random.shuffle(password)
print(f"Your password is ", *password,sep ="")


"""
Password Generator
Coming up with a password that meets specific requirements
is something your computer can do. And it will give you
practice using random number generators in conjunction
with a list of known values.
Create a program that generates a secure password. Prompt
the user for the minimum length, the number of special
characters, and the number of numbers. Then generate a
password for the user using those inputs.

Example Output
What's the minimum length? 8
How many special characters? 2
How many numbers? 2
Your password is
aurn2$1s#

Constraints
• Use lists to store the characters you’ll use to generate
the passwords.
• Add some randomness to the password generation.
"""