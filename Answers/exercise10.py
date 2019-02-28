import os
os.system('cls')

price_of_item1 = int(input("Enter the price of item 1:"))
quantity_of_item1 = int(input("Enter the quantity of item 1:"))

price_of_item2 = int(input("Enter the price of item 2:"))
quantity_of_item2 = int(input("Enter the quantity of item 2:"))

price_of_item3 = int(input("Enter the price of item 3:"))
quantity_of_item3 = int(input("Enter the quantity of item 3:"))

subtotal = (price_of_item1 * quantity_of_item1) \
	+ (price_of_item2 * quantity_of_item2) \
	+ (price_of_item3 * quantity_of_item3)
print(f"Subtotal: ${subtotal:.2f}")

# 5.5% sales tax divide by 100% => .055
tax_rate = .055
tax_total = subtotal * tax_rate
print(f"Tax: ${tax_total:.2f}")

# Total cost with tax
total_cost = subtotal + tax_total
print(f"Total: ${total_cost:.2f}")

"""
Self-Checkout
Working with multiple inputs and currency can introduce
some tricky precision issues.Create a simple self-checkout system. 
Prompt for the prices and quantities of three items. 
Calculate the subtotal of the items. Then calculate the tax using a tax rate of 5.5%. 
Print out the line items with the quantity and total, and then print
out the subtotal, tax amount, and total.

Example Output
Enter the price of item 1: 25
Enter the quantity of item 1: 2
Enter the price of item 2: 10
Enter the quantity of item 2: 1
Enter the price of item 3: 4
Enter the quantity of item 3: 1
Subtotal: $64.00
Tax: $3.52
Total: $67.52

"""