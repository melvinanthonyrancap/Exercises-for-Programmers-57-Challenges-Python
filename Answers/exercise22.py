import os
os.system('cls')

first_number = int(input("Enter the first number: "))

# Holds current largest number 
largest_number = first_number

second_number = int(input("Enter the second number: "))

if second_number == first_number:
	exit()
elif largest_number < second_number:
	largest_number = second_number

third_number = int(input("Enter third number: "))

if largest_number < third_number:
	largest_number = third_number

if second_number == third_number or third_number == first_number:
	exit()
else:
	print(f"The largest number is {largest_number}.")


"""
Comparing Numbers
Comparing one input to a known value is common enough,
but you’ll often need to process a collection of inputs.
Write a program that asks for three numbers. Check first to
see that all numbers are different. If they’re not different,
then exit the program. Otherwise, display the largest number
of the three.

Example Output
Enter the first number: 1
Enter the second number: 51
Enter the third number: 2
The largest number is 51.

Constraint
• Write the algorithm manually. Don’t use a built-in
function for finding the largest number in a list.
"""