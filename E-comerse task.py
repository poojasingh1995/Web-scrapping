import requests
from bs4 import BeautifulSoup
import json
import pprint
def e_comerse():
    url="https://webscraper.io/test-sites"
    api=requests.get(url)
    soup=BeautifulSoup(api.text,"html.parser")
    div=soup.find("div",class_="container test-sites")
    main=div.find_all("div",class_="col-md-7 pull-right")
    
    list=[]
    position_no=0
    for index in main:
        position_no+=1
        name1=index.find("h2",class_="site-heading").a.get_text().strip()
       
        comerse_link=index.find("h2",class_="site-heading").a["href"]
        
        link="https://webscraper.io/"+comerse_link
        # print(link)

        dict={"Position":position_no,"Name":name1,"url":link}
        list.append(dict)

        with open("e_comerse_data.json","w")as data:
            json.dump(list,data,indent=4)
    return list

print(e_comerse())



