import os
import tkinter as tk
import json
import requests
import webbrowser
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO

os.system('cls')
tag = input("Enter a search word: ")
with urlopen(f"https://api.flickr.com/services/feeds/photos_public.gne?tags={tag}&format=json&nojsoncallback=1") as response:
	source = response.read()

#Stores the JSON data
data = json.loads(source)
url_list = []

for picture in data['items']:
	url_list.append(picture['media']['m'])

print(*url_list ,sep="\n")


window = tk.Tk()

window.title("Flickr Photo Search")

window.geometry("800x800")

for address in url_list:
	url = address

u = urlopen(url)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(im)

label = tk.Label(image=photo)
label.image = photo
label.pack()



label.grid()


window.mainloop()