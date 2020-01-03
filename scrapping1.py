import requests
from bs4 import BeautifulSoup

page=requests.get("https://www.passiton.com/inspirational-quotes")
soup=BeautifulSoup(page.content)
table=soup.find('div',attrs={'id':'all_quotes'}

for row in table.findAll('img'):
	print(row)
