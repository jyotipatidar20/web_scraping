from bs4 import BeautifulSoup
import json
import requests
# import task12
from Task_12 import movie_caste_url
a=[]
def scrape_movie_details(link):
    cast=(movie_caste_url(link))
    b={}
    url=requests.get(link)
    # print(url)
    soup=BeautifulSoup(url.text,"html.parser")
    # print(soup)
    b["movie name"]=soup.find("h1").text
    main=soup.find("div",class_="panel-body content_body")
    # print(main)
    x=main.find("ul",class_="content-meta info")
    # print(x)
    y=x.find_all("li",class_="meta-row clearfix")
    # print(y)
    for i in y:
        b[i.find("div",class_="meta-label subtle").text]=" ".join(i.find("div",class_="meta-value").text.split())
        b["cast"]=cast
        movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
        b["Bio"]=movie_bio
    # print(b)
    with open("task13.json","w") as f:
        json.dump(b,f,indent=2)
    return b
    
        
scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")