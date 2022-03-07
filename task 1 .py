# from os import link
# from bs4 import BeautifulSoup 
# import json
# import requests
# def scrape_top_list():
#     url= ("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
#     # print(url.text)
#     a = (requests.get(url))
#     soup=BeautifulSoup(a.text,'html.parser')
#     main_div=soup.find('table',class_='table')
#     trs=main_div.find_all('tr')
#     # main_movie=[]
#     top_movie=[]
#     for tr in trs[1:]:
#         position = tr.find('td',class_="bold").get_text().strip()
#         rank=position
#          # print(main_movie)
#         rating=tr.find('span',class_="tMeterScore").get_text().strip()
#         # print(main_movie)
#         title=tr.find('a',class_="unstyled articleLink").get_text().strip()
#         year=title[-5:-1]
#         name=title[:-7]
#         # main_movie.append(title)
#         # print(main_movie)
#         review=tr.find('td',class_="right hidden-xs").get_text().strip()
#         # main_movie.append(review)
#         list=title.split()
#         name_length=len(list)-1
#         name=''
#         for l in range(name_length):
#             name+=" "
#             name=name+list[l]
#         movieName=name
#         url=tr.find("a",class_="unstyled articleLink")
#         link=url.get_text()
#         # print(url)
#         link=url["href"]
#         # print(link_1)
#         url1="https://editorial.rottentomatoes.com"+link
#         # print(url1)
#     # # print(main_movie)
#         details={"position":" ","rating":" ","title":" ","review":" ","url":" "}
#         details["position"]=(rank)
#         details["rating"]=(rating)
#         details["title"]=str(movieName)
#         details["review"]=(review)
#         details["url"]=(url1)
#         details["year"]=(year)
#         top_movie.append(details)
#         print(top_movie)
#         with open("movie_data.json","w") as c:
#             json.dump(top_movie ,c,indent=4)
#         # return top_movie
# print(scrape_top_list)




# a="12hour"
# print(str(12*2)+"hours")






from Task_1 import  scrap_top_list
from Task_4 import scrape_movie_details
# from Task_1 import scrap_top_list
import requests
import json
from bs4 import BeautifulSoup

with open("movie_data.json","r") as f:
      a=json.load(f)
# print(a)

def get_movie_list_details(all_movie):
    # list=[]
    # movie_details_list=[]
    for i in range(10):
        # for j in a[i]["Movie URL"]:
        # url=(a[i]["Movie URL"])
        # page=requests.get(url)
        page=requests.get(all_movie[i]["Movie URL"])
    # print(page)
        soup=BeautifulSoup(page.content,"html.parser")
        main_title=soup.find('ul',class_="content-meta info")
        # print(main_title)

        main_li=main_title.find_all('li',class_="meta-row clearfix")
        print(main_li)
        b={}
        url=requests.get()
        soup=BeautifulSoup(url.text,"html.parser")
        b["movie name"]=soup.find("h1").text
        main=soup.find("div",class_="panel-body content_body")
        x=main.find('ul',class_="content-meta info")


        y=x.find_all('li',class_="meta-row clearfix")
        
        for i in y:
            b[i.find('div',class_="meta-label subtle").text]=" ".join(i.find('div',class_="meta-value").text.split())
        a.append(b)
        return a
        # dic={}
        # list=[]
        # for i in main_li:
        #     directer=i.find('div',class_="meta-label subtle").get_text().strip().replace("\n",'')
        #     # producer=i.find('div',class_="meta-label subtle")
        #     genre=i.find('div',class_="meta-value").get_text().strip().replace("\n",'')
        #     dic.update({directer:genre})
        # list.append(dic)
        # s=a[i]["Movie_URL"]
        # print(s)
        # detail=scrape_movie_details(s)
        # print(detail)
        # movie_details_list.append(detail)
    with open("task5.json","w") as r:
        json.dump(list,r,indent=4)
