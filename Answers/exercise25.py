import os
os.system('cls')

def isAllNumbers(string):
	result = True
	try:
		int(string)
	except ValueError:
		result = False

	return result

def isAllLetters(string):
	result = True
	count = 0
	length = len(string)

	chars_list = [i for i in string]

	while count != length:
		
		if chars_list[count].isalpha() != True:
			result = False
			break
		else:
			result = True

		count +=1

	return result

def isStrongPassword(string):
	result = True
	containsOneNumber = 0
	containsOneSpecialChar = 0
	count = 0
	length = len(string)

	chars_list = [i for i in string]

	while count != length:		
		if chars_list[count].isdigit() == True and length >= 8:
			containsOneNumber += 1
			result = True
			break
		else:
			result = False
		count +=1

	return result

def isVeryStrongPassword(string):
	result = False
	containsOneSpecialChar = 0
	containsOneLetter = 0
	containsOneNumber = 0
	count = 0
	length = len(string)
	specialChars_dict ={0:"@",
						1:"%",
						2:"+",
						3:"\\",
						4:"/",
						5:"\'",
						6:"!",
						7:"#",
						8:"$",
						9:"^",
						10:"?",
						11:":",
						12:",",
						13:"(",
						14:")",
						15:"{",
						16:"}",
						17:"[",
						18:"]",
						19:"~",
						20:"_",
						21:"."
						}

	chars_list = [i for i in string]

	while count != length:		
		if chars_list[count].isdigit() == True:
			containsOneNumber += 1
		elif chars_list[count].isalpha() == True:
			containsOneLetter += 1
		elif chars_list[count] in specialChars_dict.values():
			containsOneSpecialChar +=1

		count +=1

	if containsOneNumber >= 2 and containsOneLetter >= 2 and containsOneSpecialChar >= 1:
		result = True
	
	return result 	

def passwordValidator(password):
	min_length = 8

	if isAllNumbers(password) == True and len(password) < min_length:
		print(f"The password \'{password}\' is a very weak password.")
	elif isAllLetters(password) == True and len(password) < min_length:
		print(f"The password \'{password}\' is a weak password.")
	elif isVeryStrongPassword(password) == True and len(password) >= min_length:
		print(f"The password \'{password}\' is a very strong password.")
	else:
		print(f"The password \'{password}\' is a strong password.")
	

passwordValidator("abc1233#@$xyz")


"""
Password Strength Indicator
Functions help you abstract away complex operations, but
they also help you build reusable components.
Create a program that determines the complexity of a given
password based on these rules:
• A very weak password contains only numbers and is
fewer than eight characters.
• A weak password contains only letters and is fewer than
eight characters.
• A strong password contains letters and at least one
number and is at least eight characters.
• A very strong password contains letters, numbers, and
special characters and is at least eight characters.

Example Output
The password '12345' is a very weak password.
The password 'abcdef' is a weak password.
The password 'abc123xyz' is a strong password.
The password '1337h@xor!' is a very strong password.

Constraints
• Create a passwordValidator function that takes in the
password as its argument and returns a value you can
evaluate to determine the password strength. Do not
have the function return a string—you may need to
support multiple languages in the future.
• Use a single output statement.
"""