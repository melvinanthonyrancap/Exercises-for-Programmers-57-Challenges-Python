import os
os.system('cls')

order_amount = int(input("What is the order amount? "))
state = input("What state do you live in? ")


if state.lower() == "illinois":
 	tax = (8.0 / 100)
 	tax_amount = order_amount * tax
 	total_amount = order_amount + tax_amount
 	print(f"The tax is ${tax_amount:.2f}.")
 	print(f"The total is ${total_amount:.2f}.")
	

if state.lower() == "wisconsin":
	county = input("What county do you live in? ")
	if county.lower() == "eau claire":
		tax = (5.5 / 100) + 0.005
		tax_amount = order_amount * tax
		total_amount = order_amount + tax_amount
		print(f"The tax is ${tax_amount:.2f}.")
		print(f"The total is ${total_amount:.2f}.")
	elif county.lower() == "dunn":
		tax = (5.5 / 100) + 0.004
		tax_amount = order_amount * tax
		total_amount = order_amount + tax_amount
		print(f"The tax is ${tax_amount:.2f}.")
		print(f"The total is ${total_amount:.2f}.")


"""
Multistate Sales Tax Calculator
More complex programs may have decisions nested in other
decisions, so that when one decision is made, additional
decisions must be made.
Create a tax calculator that handles multiple states and
multiple counties within each state. The program prompts
the user for the order amount and the state where the order
will be shipped.
For Wisconsin residents, prompt for the county of residence.
• For Eau Claire county residents, add an additional 0.005
tax.
• For Dunn county residents, add an additional 0.004 tax.
Illinois residents must be charged 8% sales tax with no
additional county-level charge. All other states are not
charged tax. The program then displays the tax and the total
for Wisconsin and Illinois residents but just the total for
everyone else.

Example Output
What is the order amount? 10
What state do you live in? Wisconsin
The tax is $0.50.
The total is $10.50.

Constraints
• Ensure that all money is rounded up to the nearest cent.
• Use a single output statement at the end of the program
to display the program results.
"""
 		