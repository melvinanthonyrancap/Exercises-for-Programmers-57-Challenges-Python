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
		print("1: Add an employeee \n2: Print employee list \n3: Quit")
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
			exit()
			break

def print_employee(employee_dic):
	os.system('cls')
	sorted_list = sorted(employee_dic.items())

	print("Name               | Position                        | Separation Date")
	print("-------------------|---------------------------------|----------------")
	for k, v in sorted_list:
		print(f"{v[0]} {v[1]}      | {v[2]}                | {v[3]}  ")
	print("\n")

add_employee()