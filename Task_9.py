from bs4 import BeautifulSoup
import json
from Task_1 import scrap_top_list
import requests
import os
import time
# import pprint
data=scrap_top_list()
url_list=[]
for i in data:
    url_list.append(i["Movie URL"])
def get_movie_list_details(movies_list):
    list4=[]
    for j in range(5):
        #  print(j)   
        if j==2:
            # time.sleep(20)
            print(j)
        for movies in movies_list:
            movie_name=movies[33:]
            if os.path.exists(movie_name+".json"):
                with open(movie_name+".json","r")as file:
                    data=file.read()
                    dic=json.loads(data)
                list4.append(dic)
            else:
                x=requests.get(movies)
                soup=BeautifulSoup(x.text,"html.parser")
                main=soup.find("ul",class_="content-meta info")
                all=main.find_all("li",class_="meta-row clearfix")
                d={}
                for i in all:
                    d[i.find("div",class_="meta-label subtle").text]=" ".join(i.find("div",class_="meta-value").text.split())
                    d["name"]=soup.find("h1").text
                    movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
                    d["Bio"]=movie_bio
                    list4.append(d)
                # with open("task_9.json","w")as f:
                with open(movie_name+"taks_9.json","w") as f:
                    json.dump(d,f,indent=4)
            time.sleep(10)    
        # print(list4)
get_movie_list_details(url_list[:5])
