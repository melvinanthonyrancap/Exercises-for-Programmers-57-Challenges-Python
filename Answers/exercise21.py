import os
os.system('cls')

#Python doesn't have a switch-case so a solution is to use a dict either in a function or class
def month(i):
	switcher = {
		1:"January",
		2:"February",
		3:"March",
		4:"April",
		5:"May",
		6:"June",
		7:"July",
		8:"August",
		9:"September",
		10:"October",
		11:"November",
		12:"December"
	}
	return switcher.get(i ,"Invalid Month")

#Testing if the input is valid month input
while True:
	try:
		input = int(input("Please enter the number of the month: "))	
		if input > 12:
			print("Not a valid month")
		else:
			print(f"The name of the month is {month(input)}.")
		break
	except ValueError:
		print("Only intergers")
		continue
	
"""
Numbers to Names
Many programs display information to the end user in one
form but use a different form inside the program. For
example, you may show the word Blue on the screen, but
behind the scenes you’ll have a numerical value for that
color or an internal value because you may need to represent
the textual description in another language for Spanishspeaking
visitors.
Write a program that converts a number from 1 to 12 to the
corresponding month. Prompt for a number and display the
corresponding calendar month, with 1 being January and
12 being December. For any value outside that range, display
an appropriate error message.

Example Output
Please enter the number of the month: 3
The name of the month is March.

Constraints
• Use a switch or case statement for this program.
• Use a single output statement for this program.
"""