import os
os.system('cls')

# Website Generator Function
def website_generator():
	#Get Website Information
	site_name = input("Site name: ")
	author = input("Author: ")
	javscript_folder = input("Do you want a folder for JavaScript? ")
	css_folder = input("Do you want a folder for CSS? ")
	path ="./" + site_name
	
	#Created Folder for Website
	print(f"Created ./{site_name}")
	os.mkdir(path, 0o777)
	
	#Created index.html homepage
	print(f"Created ./{site_name}/index.html")
	index_file = open(f"./{site_name}/index.html","w+")

	index_file.write("<!DOCTYPE html>")
	index_file.write("\n")
	index_file.write("<html>")
	index_file.write("\n")
	index_file.write("<head>")
	index_file.write("\n")
	index_file.write(f"\t<title>{site_name}</title>")
	index_file.write("\n")
	index_file.write(f"\t<meta name =\"author\" content = \"{author}\">")
	index_file.write("\n")
	index_file.write("</head>")
	index_file.write("\n")
	index_file.write("<body>")
	index_file.write("\n")
	index_file.write("</body>")
	index_file.write("\n")
	index_file.write("</html>")

	if javscript_folder.lower() == "y".lower() or javscript_folder == "yes".lower():
		print(f"Created ./{site_name}/js/")
		os.mkdir(path + "/js/", 0o777) 

	if css_folder.lower() == "y".lower() or css_folder == "yes".lower():
		print(f"Created ./{site_name}/css/")
		os.mkdir(path + "/css/", 0o777)

#Main Program
website_generator()

"""
Website Generator
Programming languages can create files and folders too.
Create a program that generates a website skeleton with the
following specifications:
• Prompt for the name of the site.
• Prompt for the author of the site.
• Ask if the user wants a folder for JavaScript files.
• Ask if the user wants a folder for CSS files.
• Generate an index.html file that contains the name of the
site inside the <title> tag and the author in a <meta> tag.

Example Output
Site name: awesomeco
Author: Max Power
Do you want a folder for JavaScript? y
Do you want a folder for CSS? y
Created ./awesomeco
Created ./awesomeco/index.html
Created ./awesomeco/js/
Created ./awesomeco/css/
"""