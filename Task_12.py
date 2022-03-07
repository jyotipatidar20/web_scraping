from bs4 import BeautifulSoup
import json 
import requests
import pprint
def movie_caste_url(link):
    movie_data=link
    # print(movie_data)
    movie_url=requests.get(movie_data)
    # print(movie_url)
    data = movie_url.content
    # print(htmlcontent )
    soup = BeautifulSoup(data,"html.parser")
    # print(soup)
    list=[] 
    cast_div=soup.find("div",class_="castSection")
    a2=cast_div.find_all("div",recursive=False)
    j=0
    for i in a2:
        if j==5:
            break
        a1=i.find("div",class_="media-body")
        if a1.a!=None:

            list.append(a1.a.span.get_text().strip())
        j+=1    
    # print(list)
    with open("task12.json","w") as f:
        json.dump(list,f,indent=2)
    return list
movie_caste_url("https://www.rottentomatoes.com/m/black_panther_2018")