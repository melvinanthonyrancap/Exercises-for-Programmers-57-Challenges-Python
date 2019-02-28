import os
import math

os.system('cls')

# Prompt user for length and width for area of ceiling
length = int(input("What is the length of the ceiling?"))
width = int(input("What is the width of the ceiling?"))

# One gallon of paint is 350 square feet
gallon_of_paint = 350

# Total area of Ceiling
area = length * width

# Total amount paint needed for the ceiling
amount_of_paint = math.ceil(area / gallon_of_paint)

print(f"You will need to purchase {amount_of_paint} gallons of paint to cover " 
	" {area} square feet")


"""
Paint Calculator
Sometimes you have to round up to the next number rather
than follow standard rounding rules.
Calculate gallons of paint needed to paint the ceiling of a
room. Prompt for the length and width, and assume one
gallon covers 350 square feet. Display the number of gallons
needed to paint the ceiling as a whole number.

Example Output
You will need to purchase 2 gallons of
paint to cover 360 square feet.
Remember, you can’t buy a partial gallon of paint.You must
round up to the next whole gallon.

Constraints
• Use a constant to hold the conversion rate.
• Ensure that you round up to the next whole number.
"""