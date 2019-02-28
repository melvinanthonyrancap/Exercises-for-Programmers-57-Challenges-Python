import math
import os
os.system('cls')

length = int(input("What is the length of the room in feet?"))
width = int(input("What is the width of the room in feet?"))

print(f"You entered dimensions of {length} feet by {width} feet")
area = length * width
print(f"The area is {area} square feet")
conversion_factor = 0.09290304

square_meters = area * conversion_factor
print(f"{square_meters:.3f} square meters")


"""
Area of a Rectangular Room
When working in a global environment, you’ll have to
present information in both metric and Imperial units. And
you’ll need to know when to do the conversion to ensure
the most accurate results.
Create a program that calculates the area of a room. Prompt
the user for the length and width of the room in feet. Then
display the area in both square feet and square meters.

Example Output
What is the length of the room in feet? 15
What is the width of the room in feet? 20
You entered dimensions of 15 feet by 20 feet.
The area is
300 square feet
27.871 square meters
The formula for this conversion is
m2 = f2 × 0.09290304

Constraints
• Keep the calculations separate from the output.
• Use a constant to hold the conversion factor.
"""