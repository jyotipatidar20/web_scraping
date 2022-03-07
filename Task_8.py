from bs4 import BeautifulSoup
import json
import requests
# from pprint import pprint
from Task_1 import scrap_top_list
import os

scraped=scrap_top_list()

a=[]
def scrape_movie_details(link):
    print(link)
    name=link[33:]
    if os.path.exists(name+".json")==True:
        with open(name+".json", 'r') as file:
            data=file.read()
            print(json.loads(data))   
    else:

        b={}
        url=requests.get(link)
        soup=BeautifulSoup(url.text,"html.parser")
        # print(soup)
        b["movie name"]=soup.find("h1").text
        # main=soup.find("div",class_="panel-body content_body")
        # print(main)
        x=soup.find("ul",class_="content-meta info")
        # print(x)
        y=x.find_all("li",class_="meta-row clearfix")
        # print(y)
        for i in y:
            b[i.find("div",class_="meta-label subtle").text]=" ".join(i.find("div",class_="meta-value").text.split())
            b["name"]=soup.find("h1").text
            movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
            b["Bio"]=movie_bio
        a.append(b)
        print(a)
    with open("task8.json","w")as file:
            json.dump(a,file,indent=4)
            # print(a)
        # return a
# scrape_movie_details("https://www.rottentomatoes.com/m/doctor_strange_2016")
# scrape_movie_details("https://www.rottentomatoes.com/m/princess_bride")
scrape_movie_details("https://www.rottentomatoes.com/m/1000617-aliens")
        
