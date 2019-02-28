import os
import json

from urllib.request import urlopen

os.system('cls')

#Pulls the data from the API
with urlopen("http://api.open-notify.org/astros.json") as response:
	source = response.read()

#Stores the JSON data
data = json.loads(source)

#Prints the JSON data to Screen
print(f"There are {len(data['people'])} people in space right now:\n")
print("Name                   | Craft")
print("-----------------------|---------")
for person in data['people']:
	print(f"{person['name']:<20}   | {person['craft']}")


"""
Who’s in Space?
Did you know you can find out exactly who’s in space right
now? The Open Notify API provides that information. Visit
http://api.open-notify.org/astros.json to see not only how many
people are currently in space but also their names and which
spacecraft they’re on.
Create a program that pulls in this data and displays the
information from this API in a tabular format.

Example Output
There are 3 people in space right now:
Name 				| Craft
--------------------|------
Gennady Padalka 	| ISS
Mikhail Kornienko 	| ISS
Scott Kelly 		| ISS

Constraint
• Read the data directly from the API and parse the results
each time the program is run. Don’t download the data
as text and read it in.
"""