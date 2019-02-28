import os
os.system('cls')

num_of_people = int(input("How many people?"))
num_of_pizza = int(input("How many pizzas do you have?"))
slices_per_pizza = 8
slices_per_person = int((slices_per_pizza * num_of_pizza) / num_of_people)
leftover = (slices_per_pizza * num_of_pizza) % num_of_people

print(f"{num_of_people} people with {num_of_pizza} pizzas")
print(f"Each person gets {slices_per_person} pieces of pizza.")
print(f"There are {leftover} leftover pieces.")


"""
Pizza Party
Division isn’t always exact, and sometimes you’ll write
programs that will need to deal with the leftovers as a whole
number instead of a decimal.
Write a program to evenly divide pizzas. Prompt for the
number of people, the number of pizzas, and the number of
slices per pizza. Ensure that the number of pieces comes out
even. Display the number of pieces of pizza each person
should get. If there are leftovers, show the number of leftover
pieces.

Example Output
How many people? 8
How many pizzas do you have? 2
8 people with 2 pizzas
Each person gets 2 pieces of pizza.
There are 0 leftover pieces.
"""