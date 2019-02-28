import os
os.system('cls')


print("Press C to convert from Fahrenheit to Celsius." \
	"\nPress F to convert from Celsius to Fahrenheit.")

user_input = input("Your choice: ")


if user_input.lower() == "c":
	temperature = int(input("Please enter the temperature in Fahrenheit: "))
	celsius = (temperature - 32) * (5/9)
	print(f"The temperature is Celsius is {celsius}.")
elif user_input.lower() == "f":
	temperature = int(input("Please enter the temperature in Celsius: "))
	fahrenheit = ((temperature * (9/5)) + 32)
	print(f"The temperature in Fahrenheit is {fahrenheit}")
else:
	print("Not a Valid Choice.")

"""
Temperature Converter
You’ll often need to determine which part of a program is
run based on user input or other events.
Create a program that converts temperatures from Fahrenheit
to Celsius or from Celsius to Fahrenheit. Prompt for the
starting temperature. The program should prompt for the
type of conversion and then perform the conversion.

The formulas are
C = (F − 32) × 5 / 9
and
F = (C × 9 / 5) + 32

Example Output
Press C to convert from Fahrenheit to Celsius.
Press F to convert from Celsius to Fahrenheit.
Your choice: C
Please enter the temperature in Fahrenheit: 32
The temperature in Celsius is 0.

Constraints
• Ensure that you allow upper or lowercase values for C
and F.
• Use as few output statements as possible and avoid
repeating output strings.
"""