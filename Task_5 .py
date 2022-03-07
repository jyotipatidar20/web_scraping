from Task_1 import scrap_top_list
import requests
import json
from bs4 import BeautifulSoup

with open("movie_data_task_1.json","r") as f:
    a=json.load(f)
num=scrap_top_list()
def get_movies_list_details(movies):
    c=[]
    # b={}
    for j in range(100):
        # print(i)
        year=movies[j]["Movie URL"]
        k=str(year)
        # print(k)
        p=requests.get(k)
        # print(p)
        soup=BeautifulSoup(p.text,"html.parser")
    # print(soup)
        # movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp")
        # print(movie_bio)
        x=soup.find('ul',class_="content-meta info")
        # print(x)
        y=x.find_all('li',class_="meta-row clearfix")
        # print(y)
        b={}
        for i in y:
            b[i.find('div',class_="meta-label subtle").text]=" ".join(i.find('div',class_="meta-value").text.split())
            b["name"]=soup.find("h1").text
            movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
            b["Bio"]=movie_bio
    #         print(b)
        c.append(b)
            
         # print(c)
    with open("task5.json","a") as e:
            json.dump(c,e,indent=4)
    # print(a)
get_movies_list_details(num)









# scrape=scrap_top_list()

# def main_fun(scrape):
#     def scrap(link,Mname):
#         b={}
#         url=requests.get(link)
#         soup=BeautifulSoup(url.text,"html.parser")
#         b["name"]=Mname
#         movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
#         b["Bio"]=movie_bio
    
#         x=soup.find('ul',class_="content-meta info")

#         y=x.find_all('li',class_="meta-row clearfix")
    
#         for i in y:
#             b[i.find('div',class_="meta-label subtle").text]=" ".join(i.find('div',class_="meta-value").text.split())
#             a.append(b)
#         # return a
#     movie_details=[]
#     for i in scrape:
#         for j in i:
#             Mname=i['title']
#             print(Mname)
#             # if j=="Movie URL":
#             #     print(j)
#     #             age=scrap(i[j],Mname)
#     #             movie_details.append(age)
#     # with open("task5.json","w") as e:
#     #     json.dump(movie_details,e,indent=4)
#     # return movie_details
# var=main_fun(scrape)
