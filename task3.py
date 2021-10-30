from bs4 import BeautifulSoup
from task_1 import scrape_movie
from task_2 import group_by_year
import pprint
import json

scrapped=scrape_movie()
decade_arrenge=group_by_year(scrapped)
def group_by_decade(movies):
    list=[]
    dict={}
    for index in movies:           #years
       module=index%10             # years ko 10 se module karne pr reminder
       decade_substract=index-module
       if decade_substract not in list:
           list.append(decade_substract)
    list.sort()
    for index2 in list:
        dict[index2]=[]
    for index3 in dict:
        decade_10=index3+9 # year me 9 ka addion 1950+9=1959
        for index4 in movies:
            if index4<=decade_10 and index4>=index3: #1959 se 1950 tak campair kar append hoga khali dict me.
                for index5 in movies[index4]: #hamari jo year wali key hai wo list ki form he or ham puri list ko append nhi kara sakte he eliye list pr loop chalya he.
                    dict[index3].append(index5)
            
        with open("group_by_decade.json","w") as num:
            json.dump(dict,num,indent=6)

    return dict
group_by_decade(decade_arrenge)
