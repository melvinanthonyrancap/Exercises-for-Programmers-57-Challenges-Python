import os
os.system('cls')
class Employees:
  def __init__(self):
    self.names = []
  
  def add(self,name):
    self.names.append(name)
  
  def delete(self,name):
    self.names.remove(name)
    
  def exit(self,user_input):
    exit()
    
  def list_size(self):
    return len(self.names)

  def print_names(self):
     print('\n')
     for name in self.names:
       print(name)

  def user_options(self):
    print('\n')
    print("what is your choice?")
    print("A: to add employee")
    print("B: to delete employee")
    print("C: to exit")
    print("D: to print employee list")

    print('\n')
    user_input = input("Pick an option: ")
    
    return user_input


  def user_choice(self,choice):
    if choice is "A":
      name = input("What's the name? ")
      self.add(name)
    elif choice is "B":
      name = input("What's the name you want to remove? ")
      self.delete(name)
    elif choice is "C":
      print("GoodBye!!!")
      exit()
    elif choice is "D":
      self.print_names()
    else:
      print("Not a valid option")
      self.user_options()

  def run_program(self):
    choice = company.user_options()
    company.user_choice(choice)



company = Employees()

while True:
  company.run_program()


"""
Employee List Removal
Sometimes you have to locate and remove an entry from a
list based on some criteria. You may have a deck of cards
and need to discard one so it’s no longer in play, or you may
need to remove values from a list of valid inputs once they’ve
been used. Storing the values in an array makes this process
easier. Depending on your language, you may find it safer
and more efficient to create a new array instead of modifying
the existing one.
Create a small program that contains a list of employee
names. Print out the list of names when the program runs
the first time. Prompt for an employee name and remove
that specific name from the list of names. Display the
remaining employees, each on its own line.

Example Output
There are 5 employees:
John Smith
Jackie Jackson
Chris Jones
Amanda Cullen
Jeremy Goodwin
Enter an employee name to remove: Chris Jones
There are 4 employees:
John Smith
Jackie Jackson
Amanda Cullen
Jeremy Goodwin

Constraint
• Use an array or list to store the names.
"""