import requests
#This allows us to manipulate the site from the cloud

from bs4 import BeautifulSoup
#BeautifulSoup is a webscraping tool kit




page = requests.get("https://en.wikipedia.org/wiki/Transhumanism")
page

#Stores the website as a variable, initializes the variable

soup = BeautifulSoup(page.content, 'lxml')
#Pulls the HTML

tag = soup.find('div', id="toc")
#Sorts out the div tags, specifically the toc div tags

link = tag.findAll('a')
#Finds the links inside the toc div tags (The HTML code for making a link is "<a href="url">link text</a>"

for link in link:
    print(link.text)
#Prints the text of the link, subtracts the HTML tags
