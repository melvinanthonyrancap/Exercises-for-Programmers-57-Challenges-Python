import os
os.system('cls')

def isAnagram(input1, input2):
  if len(input1) != len(input2):
    return False
  elif len(input1) == 0 and len(input2) == 0:
    return print("Strings are Empty")
  
  isAnagram = None

  #Spliting the two strings into indivdual letters into a list
  input1 = [i for i in input1]
  input2 = [i for i in input2]
  
  input1.sort()
  input2.sort()
  #Combing our two list into one list

  #Keeps the counts of letters
  input1_dict = {} #empty
  input2_dict = {}
  #Counts ther number of letters of a particular character O(a * b) linear speed
  for char in input1:
      if char in input1_dict:
          input1_dict[char] += 1
      else:
          input1_dict[char] = 1 
  
  for char in input2:
      if char in input2_dict:
          input2_dict[char] += 1
      else:
          input2_dict[char] = 1 
 
  if input1_dict == input2_dict:
    isAnagram = True
  else:
    isAnagram = False

  return isAnagram  

print("Enter two strings and I'll tell you if they are anagrams:")
user_input1 = input("Enter first string: ")
user_input2 = input("Enter Second string: ")


if isAnagram(user_input1,user_input2):
  print(f"{user_input1} and {user_input2} are anagrams")
elif len(user_input1) == 0 and len(user_input2) == 0:
  print()
else:
  print("They aren't anagrams.")


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