import os
os.system('cls')

#Helper function
def validate_names(firstName,lastName):
	result = True

	if len(firstName) == 0:
		print("The first name must be filled in.")
		result = False
	elif len(firstName) == 1:
		print(f"\"{firstName}\' is not a valid first name. It is too short.")
		result = False

	if len(lastName) == 0:
		print("The last name must be filled in.")
		result = False
	elif len(lastName) == 1:
		print(f"\"{lastName}\' is not a valid last name. It is too short.")
		result = False
	return result

Helper function
def validate_zip_code(zipCode):
	result = True

	try:
		int(zipCode)
	except ValueError:
		print("The ZIP code must be numeric.")
		result = False

	return result

#Helper function
def validate_id(employeeId):
	result = True
	#Last 4 number digits in an employee ID
	str_id = ""

	#Test if ID is the right length amount
	if len(employeeId) < 7 or len(employeeId) >= 8:
		print(f"{employeeId} is not a valid ID length.")
		result = False

	#ID string converted to a list for individual validation
	id_list = [i for i in employeeId]

	#Testing if the first two Characters are letters
	if id_list[0].isalpha() == False and id_list[1].isalpha() == False:
		print(f"{employeeId} first two characters aren't letters.")
		result = False

	#Hyphen position check
	if id_list[2] != "-":
		print(f"{id_list[2]} is not a hyphen character.")
		result = False

	#Checks last 4 Characters if they are numbers
	for number in id_list[3:]:
  		str_id += number

	try:
		int(str_id)
	except ValueError:
		print(f"{employeeId} is not a numeric values.")
		result = False

	return result	

#Main Function
def validateInput(firstName,lastName,zipCode,employeeId):
	first_name = firstName
	last_name = lastName
	zip_code = zipCode
	employee_id = employeeId
	result = False

	if validate_names(first_name,last_name) == True:
		result = True
	if validate_zip_code(zip_code) == True:
		result = True
	if validate_id(employee_id) == True:
		result = True

	return result



# Main Program
firstName = input("Enter the first name: ")
lastName = input("Enter the last name: ")
zipCode = input("Enter the Zip Code: ")
employeeId = input("Enter an employee ID: ")

if validateInput(firstName,lastName,zipCode,employeeId) == True:
	print("There were no errors found.")


"""
Validating Inputs
Large functions aren’t very usable or maintainable. It makes
a lot of sense to break down the logic of a program into
smaller functions that do one thing each. The program can
then call these functions in sequence to perform the work.
Write a program that prompts for a first name, last name,
employee ID, and ZIP code. Ensure that the input is valid
according to these rules:
• The first name must be filled in.
• The last name must be filled in.
• The first and last names must be at least two characters
long.
• An employee ID is in the format AA-1234. So, two letters,
a hyphen, and four numbers.
• The ZIP code must be a number.
Display appropriate error messages on incorrect data.

Example Output
Enter the first name: J
Enter the last name:
Enter the ZIP code: ABCDE
Enter an employee ID: A12-1234
"J" is not a valid first name. It is too short.
The last name must be filled in.
The ZIP code must be numeric.
A12-1234 is not a valid ID.

//TEST CASE 2

Enter the first name: Jimmy
Enter the last name: James
Enter the ZIP code: 55555
Enter an employee ID: TK-4211
There were no errors found.
"""