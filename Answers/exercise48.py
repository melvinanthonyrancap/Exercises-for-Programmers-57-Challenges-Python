import os
import json
from urllib.request import urlopen

os.system('cls')

city = input("Where city are you in? ")

with urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=a7c64bcd3a79ce72e2f62695d35b7eed") as response:
	source = response.read()

data = json.loads(source)

#JSON data is in Kelvin
fahrenheit = data['main']['temp']
weather = 9/5 * (fahrenheit - 273) + 32

print(f"{city} weather: {weather:.0f} degrees Fahrenheit")



""""
Is it nice out today? Or should I grab my coat?
Using the OpenWeatherMap API at http://openweathermap.org/
current, create a program that prompts for a city name and
returns the current temperature for the city.

Example Output
Where are you? Chicago IL
Chicago weather:
65 degrees Fahrenheit

Constraint
• Keep the processing of the weather feed separate from
the part of your program that displays the results.
""""