import os
from sys import argv
os.system('cls')

script, filename = argv

def word_frequency_finder(filename):
	#Intialize empty dictionary to hold unique words(key) and count(int values) of each word
	unique_word = {}

	#open text file
	txt = open(filename)
	
	#read file
	read_line = txt.read()
	
	#print file
	print(read_line)

	#New Line for Readablity
	print('\n')

	#split line into words into a list
	words_list = read_line.split()
	
	#loop word if word is in dictionary +1 else 1 add new entry
	for word in words_list:
		if word in unique_word:
			unique_word[word] += 1
		else:
			unique_word[word] = 1

	#print output results by sorting most occurrences
	for word in unique_word:
		print(word + ":" + "*" * unique_word[word]) 


word_frequency_finder(filename)

"""
Word Frequency Finder
Knowing how often a word appears in a sentence or block
of text is helpful for creating word clouds and other types
of word analysis. And it’s more useful when running it
against lots of text.
Create a program that reads in a file and counts the frequency
of words in the file. Then construct a histogram displaying
the words and the frequency, and display the histogram to
the screen.
Example Output
Given the text file words.txt with this content
badger badger badger badger mushroom mushroom
snake badger badger badger
the program would produce the following output:
badger: *******
mushroom: **
snake: *

Constraint
• Ensure that the most used word is at the top of the report
and the least used words are at the bottom.
"""