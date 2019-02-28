import os
os.system('cls')

# Alcohol distribution ratio for men & women
r_male = 0.73
r_female = 0.66


alcohol_amount = int(input("How ounces(oz) of alcohol you drink? "))
weight = int(input("How much you weight? "))
hours = int(input("How many hours since your last drink? "))
gender = input("Are you male or female? ")

#Blood Alcohol Content formula (BAC) test to see if they can drive or not


bac_male = (alcohol_amount * 5.14/ (weight * r_male)) - .015 * hours
bac_female = (alcohol_amount * 5.14/ (weight * r_female)) - .015 * hours

if gender == "male":
	bac_male = (alcohol_amount * 5.14/ (weight * r_male)) - .015 * hours

	if bac_male >= 0.08:
		print(f"Your BAC is {bac_male:.2f}. It is not legal for you to drive.")
	else:
		print(f"Your BAC is {bac_male:.2f}. You are safe to drive.")
else:
	bac_female = (alcohol_amount * 5.14/ (weight * r_female)) - .015 * hours

	if bac_female >= 0.08:
		print(f"Your BAC is {bac_female:.2f}. It is not legal for you to drive.")
	else:
		print(f"Your BAC is {bac_female:.2f}.You are safe to drive.")