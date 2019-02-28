import os
import random

os.system('cls')

def enter_contestants():
	player_list = []
	name = input("Enter a name: ")
	
	while True:
		if len(name) == 0 and len(player_list) >= 2:
			print(f"The winner is....  {player_list[random.randrange(len(player_list))]}.")
			break
		elif len(name) == 0 and len(player_list) == 0:
			print("No Contestants to pick.")
			break
		else:
			player_list.append(name)
			name = input("Enter a name: ")
			continue



#Main program
enter_contestants()

"""
Picking a Winner
Arrays don’t have to be hard-coded.You can take user input
and store it in an array and then work with it.
Create a program that picks a winner for a contest or prize
drawing. Prompt for names of contestants until the user
leaves the entry blank. Then randomly select a winner.

Example Output
Enter a name: Homer
Enter a name: Bart
Enter a name: Maggie
Enter a name: Lisa
Enter a name: Moe
Enter a name:
The winner is... Maggie.

Constraints
• Use a loop to capture user input into an array.
• Use a random number generator to pluck a value from
the array.
• Don’t include a blank entry in the array.
• Some languages require that you define the length of
the array ahead of time. You may need to find another
data structure, like an ArrayList.
"""