# Parse the ITM Department website to find the people (faculty, grads, lecturers)
import urllib.request
from bs4 import BeautifulSoup

itm_url = "https://shidler.hawaii.edu/itm/people"

itm_html = urllib.request.urlopen(itm_url) 
html_to_parse = BeautifulSoup(itm_html, "html.parser")

print(html_to_parse.prettify())

# Find and print just the names of the faculty members
list_of_faculty = html_to_parse.find_all("h2", class_="title")

itm_faculty = []
for person in list_of_faculty:
   itm_faculty.append(person.text.strip())
   print(person.text.strip())

print("\nTotal faculty members found:", len(itm_faculty))
unique_faculty = list(set(itm_faculty))
print("\nUnique faculty members found:", len(unique_faculty))