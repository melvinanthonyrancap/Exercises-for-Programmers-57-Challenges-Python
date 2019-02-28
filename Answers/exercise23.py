import os
os.system('cls')


user_input = input("Is the car silent when you turn the key? ")

if user_input.lower() == "y" or user_input.lower() == "yes":
	user_input = input("Are the battery terminals corroded? ")
	if user_input.lower() == "y" or user_input.lower() == "yes":
		print("Clean terminals and try starting agian.")
	elif user_input.lower() == "n" or user_input.lower() == "no":
		print("The battery cables maybe by damaged.\nReplace cables and try again.")
elif user_input.lower() == "n" or user_input.lower() == "no":
	user_input = input("Does the car make a clicking noise?")
	if user_input.lower() == "y" or user_input.lower() == "yes":
		print("Replace the battery.")
	elif user_input.lower() == "n" or user_input.lower() == "no":
		user_input = input("Does the crank up but fail to start? ")
		if user_input.lower() == "y" or user_input.lower() == "yes": 
			print("Check spark plug connections.")
		elif user_input.lower() == "n" or user_input.lower() == "no":
			user_input = input("Does the engine start and then die? ")
			if user_input.lower() == "y" or user_input.lower() == "yes":
				user_input = input("Does your car have fuel injection? ")
				if user_input.lower() == "y" or user_input.lower() == "yes":
					print("Get it in for service.")
				elif user_input.lower() == "n" or user_input.lower() == "no":
					print("Check to ensure the choke is opening and closing.")
