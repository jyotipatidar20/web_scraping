from bs4 import BeautifulSoup
import requests
import json
import pprint
a=[]
def scrape_movie_details(link):
    b={}
    url=requests.get(link)
    soup=BeautifulSoup(url.text,"html.parser")
    b["title"]="Black panther"
    movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
    b["Bio"]=movie_bio
 
    x=soup.find('ul',class_="content-meta info")

    y=x.find_all('li',class_="meta-row clearfix")
   
    for i in y:
       b[i.find('div',class_="meta-label subtle").text]=" ".join(i.find('div',class_="meta-value").text.split())
    a.append(b)
    return a
pprint.pprint(scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018"))
with open("movie_details_task_4.json","w") as file:
        json.dump(a,file,indent=4)

scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")



