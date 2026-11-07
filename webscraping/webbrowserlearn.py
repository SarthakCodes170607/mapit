import webbrowser

search = "python webbrowser module"

# Format the URL with the search term
url = "https://www.google.com/search?q=" + search.replace(" ", "+")

webbrowser.open(url)