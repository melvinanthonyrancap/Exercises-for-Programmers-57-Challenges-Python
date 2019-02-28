import os
import random
os.system('cls')



def magic8_ball():
	response_list = ["Yes.","No.","Maybe.","Ask again later.",]

	return response_list[random.randrange(4)]


question = input("What's your question? ")

print(magic8_ball())


"""
Magic 8 Ball
Arrays are great for storing possible responses from a program.
If you combine that with a random number generator,
you can pick a random entry from this list, which works
great for games.
Create a Magic 8 Ball game that prompts for a question and
then displays either “Yes,” “No,” “Maybe,” or “Ask again
later.”

Example Output
What's your question? Will I be rich and famous?
Ask again later.

Constraint
• The value should be chosen randomly using a pseudo
random number generator. Store the
"""