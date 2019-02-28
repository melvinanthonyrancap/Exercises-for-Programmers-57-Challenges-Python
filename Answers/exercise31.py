import os
os.system('cls')

resting_pulse = int(input("Resting Pulse: "))
age = int(input("Age: "))

intensity = 50

print("Intensity           |Rate")
print("--------------------|-----------")
for i in range(9):
	intensity += 5
	target_heart_rate = (((220 - age) - resting_pulse) * (intensity/ 100)) + resting_pulse
	print(f"{intensity}%                 |{target_heart_rate:.0f} bpm  ")


"""
Karvonen Heart Rate
When you loop, you can control how much you increment
the counter; you don’t always have to increment by one.
When getting into a fitness program, you may want to figure
out your target heart rate so you don’t overexert yourself.
The Karvonen heart rate formula is one method you can use
to determine your rate. Create a program that prompts for
your age and your resting heart rate. Use the Karvonen formula
to determine the target heart rate based on a range of
intensities from 55% to 95%. Generate a table with the results
as shown in the example output. The formula is
TargetHeartRate = (((220 − age) − restingHR) × intensity) + restingHR
Example Output
Resting Pulse: 65 Age: 22
Intensity | Rate
-------------|--------
55% | 138 bpm
60% | 145 bpm
65% | 151 bpm
: : (extra lines omitted)
85% | 178 bpm
90% | 185 bpm
95% | 191 bpm

Constraints
• Don’t hard-code the percentages. Use a loop to increment
the percentages from 55 to 95.
• Ensure that the heart rate and age are entered as numbers.
Don’t allow the user to continue without entering
valid inputs.
• Display the results in a tabular format.
"""