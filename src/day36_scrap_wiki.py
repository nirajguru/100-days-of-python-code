# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "beautifulsoup4",
#     "requests",
# ]
# ///
from bs4 import BeautifulSoup
import requests

response = requests.get("https://en.wikipedia.org/wiki/OpenText")


soup = BeautifulSoup(response.text)
print(soup.prettify())  ## Niraj notes: prettify() formats the HTML to be more readable
# print the first 4 paragraphs
paragraphs = soup.find_all("p")   ## Niraj notes: find_all() returns a list of all matching elements
for i in range(4):
    print(paragraphs[i].text)
# print the first 4 paragraphs
