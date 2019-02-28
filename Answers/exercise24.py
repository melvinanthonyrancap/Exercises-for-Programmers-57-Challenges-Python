import os
os.system('cls')

def isAnagram(string1, string2):
	#Spliting the two strings into indivdual letters into a list
	string_list1 = [i for i in string1]
	string_list2 = [i for i in string2]
	
	#Boolean value testing to see if the both strings are anagrams
	itsAnagram = True

	#Checks if the two strings are the same length
	if len(string_list1) != len(string_list2):
		print("\nNot the same length")

	merged_list =[*string_list1,*string_list2]
	
	#Empty dictionary to store the merged list of letters
	string_dict = {}

	#Adds each letter into the dictionary and adds 1 to their value if its already in the dictionary
	for letter in merged_list:
		if letter in string_dict:
			string_dict[letter] += 1
		else:
			string_dict[letter] = 1	

	#Iterate through the values checking if all the letters appeared at least twice to be qualify as an anagram
	for value in string_dict.values():
		if value % 2 != 0:
			itsAnagram = False
		else:
			itsAnagram = True

	return itsAnagram

#Prompt user to input two strings.
print("Enter two strings and I\'ll tell you if they are anagrams: ")
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

#Tests if the two strings are anagrams
result = isAnagram(first_string,second_string)

#Prints out results of isAnagram() function call
if result == True:
	print(f"\"{first_string}\" and \"{second_string}\" are anagrams.")
else:
	print(f"\"{first_string}\" and \"{second_string}\" are not anagrams.")


"""
Anagram Checker
Using functions to abstract the logic away from the rest of
your code makes it easier to read and easier to maintain.
Create a program that compares two strings and determines
if the two strings are anagrams. The program should prompt
for both input strings and display the output as shown in
the example that follows.

Example Output
Enter two strings and I'll tell you if they
are anagrams:
Enter the first string: note
Enter the second string: tone
"note" and "tone" are anagrams.

Constraints
• Implement the program using a function called isAnagram,
which takes in two words as its arguments and
returns true or false. Invoke this function from your main
program.
• Check that both words are the same length.
"""