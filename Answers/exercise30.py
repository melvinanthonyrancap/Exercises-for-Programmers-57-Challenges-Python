import os
os.system('cls')

for i in range(13):
  for j in range(13):
    product = i * j
    print(f"{i} X {j} = {product}")
  


  #Row X Column Table
  # for i in range(13):
  # print("\n")
  # for j in range(13):
  #   product = i * j
  #   print(f"{product}",end ="\t")


"""
Multiplication Table
Create a program that generates multiplication tables for
the numbers 0 through 12.
Example Output
0 X 0 = 0
0 X 1 = 0
...
12 x 11 = 132
12 x 12 = 144

Constraint
• Use a nested loop to complete this program.
"""