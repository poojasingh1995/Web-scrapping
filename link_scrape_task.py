import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re
def languages():
    url="https://en.wikipedia.org/wiki/India"
    api=requests.get(url)
    soup=BeautifulSoup(api.text,"html.parser")
    # print(soup)
    main_div=soup.find("div",class_="mw-parser-output")
    for index in main_div.find_all('a', attrs={'href': re.compile("^https://")}):
        print(index.get('href'))
        # link=index.get("href")


languages()
