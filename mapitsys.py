import webbrowser
import sys
import pyperclip 

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])

else:
    choice = input("Use clipboard? (y/n): ").lower()
    
    if choice == 'y':
        address = pyperclip.paste()
    else:
        address = input("Enter location: ")

url = "https://www.google.com/maps/search/" + address.replace(" ", "+")
webbrowser.open(url)