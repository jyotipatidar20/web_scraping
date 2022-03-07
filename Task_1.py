from bs4 import BeautifulSoup 
import json
import requests
def scrap_top_list():
    url= ("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
    # print(url.text)
    a = (requests.get(url))
    soup=BeautifulSoup(a.text,'html.parser')
    main_div=soup.find('table',class_='table')
    trs=main_div.find_all('tr')
    # main_movie=[]
    top_movie=[]
    for tr in trs[1:]:
        position = tr.find('td',class_="bold").get_text().strip()
        rank=position
         # print(main_movie)
        rating=tr.find('span',class_="tMeterScore").get_text().strip()
        # print(main_movie)
        title=tr.find('a',class_="unstyled articleLink").get_text().strip()
        year=title[-5:-1]
        name=title[:-7]
        # main_movie.append(title)
        # print(main_movie)
        review=tr.find('td',class_="right hidden-xs").get_text().strip()
        # main_movie.append(review)
        list=title.split()
        name_length=len(list)-1
        name=''
        for l in range(name_length):
            name+=" "
            name=name+list[l]
        # year=[-5:-1]
        movieName=name
        url=tr.find("a",class_="unstyled articleLink")
        link=url.get_text()
        # print(url)
        link=url["href"]
        # print(link)
        url1="https://www.rottentomatoes.com"+link
        # year=tr.find('a',class_="unstyled articleLink")
        # main_year=year.get_text()
        # print(url1)
    # print(main_movie)
        details={"position":" ","rating":" ","title":" ","review":" ","Movie URL":" "}
        details["position"]=(rank)
        details["rating"]=(rating)
        details["title"]=str(movieName)
        details["review"]=(review)
        details["Movie URL"]=(url1)
        details["year"]=(year)
        top_movie.append(details)
        # print(top_movie)
        with open("movie_data_task_1.json","w") as c:
            json.dump(top_movie ,c,indent=4)
    return top_movie
# print(scrap_top_list())
scrap=(scrap_top_list())


