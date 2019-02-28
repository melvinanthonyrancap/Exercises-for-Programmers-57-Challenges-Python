import os
from sys import argv
os.system('cls')

script, filename = argv

def name_sorter(filename):
	txt = open(filename)
	names_list = []
	names_list = txt.read().split('\n')
	names_sorted = sorted(names_list)
	number_of_names = len(names_sorted)
	print(f"Total of {number_of_names} names")
	print("-------------------------------")
	print(*names_sorted,sep="\n")

name_sorter(filename)

"""
Name Sorter
Alphabetizing the contents of a file, or sorting its contents,
is a great way to get comfortable manipulating a file in your
program.
Create a program that reads in the following list of names:
Ling, Mai
Johnson, Jim
Zarnecki, Sabrina
Jones, Chris
Jones, Aaron
Swift, Geoffrey
Xiong, Fong
Read this program and sort the list alphabetically. Then print
the sorted list to a file that looks like the following example
output.

Example Output
Total of 7 names
-----------------
Ling, Mai
Johnson, Jim
Jones, Aaron
Jones, Chris
Swift, Geoffrey
Xiong, Fong
Zarnecki, Sabrina

Constraint
• Don’t hard-code the number of names.
"""