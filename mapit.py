import webbrowser
search = input("pls enter location u wish to open in Gmaps")
url = "https://www.google.com/maps/search/" + search.replace(" ", "+") 
webbrowser.open(url)
 
