import os
os.system('cls')

wisconsin = "WI"
minnesota = "MN"

wi_tax = 5.5 

#6.875% MN Current Sales Tax
mn_tax = 6.875 


order_amount = int(input("What is the order amount?"))

state = input("What is the state?")

if state == wisconsin:
	print(f"The subtotal is ${float(order_amount):.2f}.")
	
	tax_total = (order_amount * wi_tax) / 100
	print(f"The tax is ${tax_total:.2f}.")
	
	total = order_amount + tax_total
	print(f"The total is ${total:.2f}.")

if state == minnesota:
	print(f"The subtotal is ${float(order_amount):.2f}.")
	
	tax_total = (order_amount * mn_tax) / 100
	print(f"The tax is ${tax_total:.2f}.")
	
	total = order_amount + tax_total
	print(f"The total is ${total:.2f}.")

"""
Tax Calculator
You don’t always need a complex control structure to solve
simple problems. Sometimes a program requires an extra
step in one case, but in all other cases there’s nothing to do.
Write a simple program to compute the tax on an order
amount. The program should prompt for the order amount
and the state. If the state is “WI,” then the order must be
charged 5.5% tax. The program should display the subtotal,
tax, and total for Wisconsin residents but display just the
total for non-residents.

Example Output
What is the order amount? 10
What is the state? WI
The subtotal is $10.00.
The tax is $0.55.
The total is $10.55.
Or
What is the order amount? 10
What is the state? MN
The total is $10.00

Constraints
• Implement this program using only a simple if statement—
don’t use an else clause.
• Ensure that all money is rounded up to the nearest cent.
• Use a single output statement at the end of the program
to display the program results.
"""