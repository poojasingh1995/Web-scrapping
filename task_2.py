from task_1 import scrape_movie
import json

scraped_data=scrape_movie()

def group_by_year(movies):
    years=[]
    for index in movies:
        if index["Year"] not in years:
            years.append(index["Year"])
    movies_dict={i:[] for i in years}
    for index2 in movies:
        year=index2["Year"]
        for update_year in movies_dict:
            # for loop eliye hamne dict me lagya he kyuki hame jo year ke movies h wo list me chahiye in dict me to ek ke years ke movle ko leta rahega
            # print(update_year,year)
            if (update_year)==(year):
                movies_dict[update_year].append(index2)
    with open("task_2.json","w") as file1:
        json.dump(movies_dict,file1,indent=5)
    return movies_dict

group_by_year(scraped_data)


        
    

