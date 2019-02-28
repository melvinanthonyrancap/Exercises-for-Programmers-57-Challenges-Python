import os
import json
from sys import argv
os.system('cls')

#Input from Command Window to load up JSON file
script, filename = argv

#Product Search Function to load JSON file and Search through it 
def product_search(filename):
	#Loads JSON File Data into an Object named 'Data'
	with open(filename) as f:
		data = json.load(f)

	while True:
		user_input = input("What is the product name? ")
		has_item = True

		for product in data['products']:
			if user_input == product['name']:
				print("Name: " + product['name'])
				print(f"Price: ${product['price']:.2f}")
				print("Quanity on hand: " + str(product['quantity']))
				has_item = True
				break
			else:
				has_item = False

		if has_item == False:
			print("Sorry, that product was not found in our inventory.")
			continue
		else:
			break

#Main Program
product_search(filename)

"""
Product Search
Pulling data from a file into a complex data structure makes
parsing much simpler. Many programming languages support
the JSON format, a popular way of representing data.
Create a program that takes a product name as input and
retrieves the current price and quantity for that product. The
product data is in a data file in the JSON format and looks
like this:

{
	"products" : [
		{"name": "Widget", "price": 25.00, "quantity": 5 },
		{"name": "Thing", "price": 15.00, "quantity": 5 },
		{"name": "Doodad", "price": 5.00, "quantity": 10 }
	]
}

Print out the product name, price, and quantity if the product
is found. If no product matches the search, state that no
product was found and start over.

Example Output
What is the product name? iPad
Sorry, that product was not found in our inventory.
What is the product name? Widget
Name: Widget
Price: $25.00
Quantity on hand: 5

Constraints
• The file is in the JSON format. Use a JSON parser to pull
the values out of the file.
• If no record is found, prompt again.
"""