import sys
import urllib.request

# url set in run parameters of main.py
# Checking command line argument
url = sys.argv[1]
print("Page url is:", url)

# Get HTTP response and read it
page = urllib.request.urlopen(url)
pageBytes = page.read()

# Get page encoding from the header and decode into string
pageEncoding = page.headers.get_content_charset()
print("Encoding type is:", pageEncoding)
pageString = pageBytes.decode(pageEncoding)
page.close()

# Get unordered list string
unorderedList = "<ul>" + pageString[pageString.find("<ul>")+len("<ul>"):pageString.rfind("</ul>")] + "</ul>"
print("Unordered list is:\n", unorderedList)

# Get last element in the list
lastListElement = "<li>" + unorderedList[unorderedList.rfind("<li>")+len("<li>"):unorderedList.rfind("</li>")] + "</li>"
print("Last element of the unordered list is:\n", lastListElement)