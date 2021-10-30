import requests
from bs4 import BeautifulSoup
import json

def scrape_movie():
    url="https://www.imdb.com/india/top-rated-indian-movies/"
    api=requests.get(url)
    soup = BeautifulSoup(api.text,"html.parser") 
    main_div=soup.find("div",class_="lister")
    tbody=main_div.find("tbody",class_="lister-list")
    tr=tbody.find_all("tr")


    list=[]
    possition_no=0
    for index in tr:
        possition_no+=1
        movie_name=index.find("td",class_="titleColumn").a.get_text()
        movie_year=index.find("td",class_="titleColumn").span.get_text()[1:5]
        years=int(movie_year)
        movie_rating=index.find("td",class_="ratingColumn").strong.get_text()
        ratings=float(movie_rating)
        movie_link=index.find("td",class_="titleColumn").a["href"]
        link="https://www.imdb.com"+movie_link
        
        dict={"Possition":possition_no,"Movies_Name":movie_name,"Year":years,"rating":ratings,"url":link}
        list.append(dict)
       
    with open("task_1_json_data.json","w")as k:
        json.dump(list,k,indent=3)
    return list
        
scrape_movie()


