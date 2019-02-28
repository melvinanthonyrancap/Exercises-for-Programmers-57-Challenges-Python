import random
import os
os.system('cls')

def game_difficulty(level):
	number = 0
	while True:	
		try:
			if level == 1:
				number = random.randrange(10 + 1)
				print("I have my number.")
				break
			elif level == 2:
				number = random.randrange(100 + 1)
				print("I have my number.")
				break
			elif level == 3:
				number = random.randrange(1000 + 1)
				print("I have my number.")
				break
			else:
				print("Not a valid nuput")
				continue
		except ValueError:
			print("Numeric Data only.")
			continue
	
	return number

def guess_the_number(number):
	number_of_guesses = 0
	picked_number = number
	
	guess = int(input("What's your Guess? "))
	number_of_guesses += 1
	
	while True:
		try:
			if guess == picked_number:
				print(f"You got it in {number_of_guesses} guesses!")
				
				new_game = input("Play agian? ")
				
				if new_game == "y":
					os.system('cls')
					start_game()
				elif new_game == "n":
					print("Goodbye! ")
					exit()
			elif guess < picked_number:
				guess = int(input("Too Low. Guess again: "))
				number_of_guesses += 1		
				continue
			elif guess > picked_number:
				guess = int(input("Too high. Guess again: "))
				number_of_guesses += 1
				continue
		except ValueError:
			print("Only Numeric data")
			continue

def start_game():
	print("Let's Play Guess the Number.")
	picked_number = game_difficulty(int(input("Pick a difficulty level(1, 2 or 3): ")))
	guess_the_number(picked_number)

start_game()


"""
Guess the Number Game
Write a Guess the Number game that has three levels of
difficulty. The first level of difficulty would be a number
between 1 and 10. The second difficulty set would be
between 1 and 100. The third difficulty set would be between
1 and 1000.
Prompt for the difficulty level, and then start the game. The
computer picks a random number in that range and prompts
the player to guess that number. Each time the player
guesses, the computer should give the player a hint as to
whether the number is too high or too low. The computer
should also keep track of the number of guesses. Once the
player guesses the correct number, the computer should
present the number of guesses and ask if the player would
like to play again.

Example Output
Let's play Guess the Number.
Pick a difficulty level (1, 2, or 3): 1
I have my number. What's your guess? 1
Too low. Guess again: 5
Too high. Guess again: 2
You got it in 3 guesses!
Play again? n
Goodbye!

Constraints
• Don’t allow any non-numeric data entry.
• During the game, count non-numeric entries as wrong
guesses.
"""