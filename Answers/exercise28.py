import os
os.system('cls')

def adding_numbers():
	sum = 0
	for i in range(5):
		sum += int(input("Enter a number: "))

	return print(f"The total is {sum}.")


adding_numbers()


"""
Adding Numbers
In previous programs, you asked the user for repeated input
by writing the input statements multiple times. But it’s more
efficient to use loops to deal with repeated input.
Write a program that prompts the user for five numbers and
computes the total of the numbers.
Example Output
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5
The total is 15.

Constraints
• The prompting must use repetition, such as a counted
loop, not three separate prompts.
• Create a flowchart before writing the program
"""