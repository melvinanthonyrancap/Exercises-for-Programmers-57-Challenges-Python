import os
os.system('cls')


while True:
	try:
		height = int(input("Whats your height in inches? "))
		weight = int(input("Whats yoru weight in pounds? "))
	except ValueError:
		print("\nOnly numeric data input.")
		continue
	else:
		break


bmi = (weight/ (height * height)) * 703

if bmi >= 18.5 and bmi <= 25:
	print(f"\nYour BMI is {bmi:.1f}.")
	print("You are within the ideal weight range.")
else:
	print(f"\nYour BMI is {bmi:.1f}.")
	print("You are overweight. You should see your doctor.")

"""
BMI Calculator
You’ll often need to see if one value is within a certain range
and alter the flow of a program as a result.
Create a program to calculate the body mass index (BMI)
for a person using the person’s height in inches and weight
in pounds. The program should prompt the user for weight
and height.
Calculate the BMI by using the following formula:
bmi = (weight / (height × height)) * 703
If the BMI is between 18.5 and 25, display that the person is
at a normal weight. If they are out of that range, tell them if
they are underweight or overweight and tell them to consult
their doctor.

Example Output
Your BMI is 19.5.
You are within the ideal weight range.
or
Your BMI is 32.5.
You are overweight. You should see your doctor.

Constraint
• Ensure your program takes only numeric data. Don’t
let the user continue unless the data is valid.
"""