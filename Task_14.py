import json
from Task_13 import scrape_movie_details

def analyse_co_actors():
    with open("movie_data_task_1.json", 'r') as file:
        data=json.load(file)
        # print(data)
    movie_url_list=[]
    for i in data:
        movie_url_list.append(i['Movie URL'])
    # print(movie_url_list)
    list=[]
    for i in range(20):
        list.append(scrape_movie_details(movie_url_list[i]))
        # print(list)
    dict={}
    for i in list:
        for j in i["cast"]:
            if j  not in dict:
                dict.update({j:[]})
    # print(dict)
    for i in dict:
        for j in list:
            if i in j["cast"]:
                for k in j["cast"]:
                    if i==k:
                        continue
                    dict[i].append(k)
                    # print(dict)
    with open('task14.json',  'w') as file:
        json.dump(dict, file, indent=4)
analyse_co_actors()