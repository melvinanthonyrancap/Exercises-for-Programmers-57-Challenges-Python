import os
from sys import argv
os.system('cls')

script, filename = argv

def word_finder(filename):
	input_file = open(filename)

	search_word = input("Enter the word to find? ")
	replace_word = input("Enter the word to replace with? ")

	read_line = input_file.read().split(" ")
	print("\n[ Original Text File: ]")
	print(" ".join(read_line))

	for word in read_line:
		if search_word in word.replace('"',""):
			read_line[read_line.index(word)] = replace_word

	print("\n")

	output_name = input("Enter the name of the output text file:  ")
	print("\n[ New Text File After the replace the word. ] \n")
	print(" ".join(read_line))
	out_file = open(output_name,'w+')
	out_file.write(" ".join(read_line))

	out_file.close()
	input_file.close()

word_finder(filename)

"""
Word Finder
There will be times when you’ll need to read in one file,
modify it, and then write a modified version of that file to
a new file.
Given an input file, read the file and look for all occurrences
of the word utilize. Replace each occurrence with use. Write
the modified file to a new file.
Example Output
Given the input file of
One should never utilize the word "utilize" in
writing. Use "use" instead.
The program should generate
One should never use the word "use" in
writing. Use "use" instead.

Constraints
• Prompt for the name of the output file.
• Write the output to a new file.
"""