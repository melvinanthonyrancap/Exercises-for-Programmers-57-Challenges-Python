import os
os.system('cls')

def add_employee():
	employee_list = []
	employee_database = {}
	space = "        "

	while True:
		print("\n")
		print("Employee Records Program: ")
		print("Pick a number option to start program.")
		print("1: Add an employeee \n2: Print employee list \n3: Search/Filter Records\n4: Quit")
		user_input = int(input())
	
		if user_input == 1:
			first_name = input("Enter employee first name: ")
			employee_list.append(first_name)
			last_name = input("Enter employee last name: ")
			employee_list.append(last_name)
			position = input("Position :")
			employee_list.append(position)
			separation_date = input("Separation date : ")
			employee_list.append(separation_date)
			employee_database.update({employee_list[1]:employee_list})
			employee_list = []
			continue
		elif user_input == 2:
			print_employee(employee_database)
			continue
		elif user_input == 3:
			search_records(employee_database)
		elif user_input == 4:
			exit()
			break

def search_records(employee_database):
	user_input = input("Enter a search string: ")

	print("Name               | Position                        | Separation Date")
	print("-------------------|---------------------------------|----------------")
	for k, v in employee_database.items():
		if user_input in v[0] or user_input in v[1]:
			print(f"{v[0]} {v[1]}      | {v[2]}                    | {v[3]}  ")
		else:
			print("No matches.")
	print("\n")

def print_employee(employee_dic):
	os.system('cls')
	sorted_list = sorted(employee_dic.items())
	print("Name            | Position      | Separation Date")
	print("----------------|---------------|----------------")
	for k, v in sorted_list:
		print('{0[0]:<10}{0[1]:<5}|{0[2]:<15}|{0[3]:<15}'.format(v))
	print("\n")
	

add_employee()


"""
Filtering Records
Sorting records is helpful, but sometimes you need to filter
down the results to find or display only what you’re looking
for.
Given the following data set
First Name Last Name Position Separation date
John Johnson Manager 2016-12-31
Tou Xiong Software Engineer 2016-10-05
Michaela Michaelson District Manager 2015-12-19
Jake Jacobson Programmer
Jacquelyn Jackson DBA
Sally Weber Web Developer 2015-12-18
create a program that lets a user locate all records that match
the search string by comparing the search string to the first
or last name field.
Example Output
Enter a search string: Jac
Results:
Name | Position | Separation Date
--------------------|-------------------|----------------
Jacquelyn Jackson | DBA |
Jake Jacobson | Programmer |

Constraint
• Implement the data using an array of maps or an associative
array.
"""