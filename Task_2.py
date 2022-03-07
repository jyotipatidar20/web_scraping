from Task_1 import scrap_top_list
import json
# import pprint
with open("movie_data_task_1.json","r") as file:
    data=json.load(file)
def group_by_year(top_movies):
    years=[]
    for i in top_movies:
        year=i["year"] 
        # print(year)
        if i['year'] not in years:
            years.append(i["year"])
            movie_dict={i:[] for i in years }
            for i in top_movies:
                year=i["year"]
                for x in movie_dict:
                    if x==year:
                        movie_dict[x].append(i)
    with open("movie_year_task_2.json","w") as file:
        json.dump(movie_dict,file,indent=4)
        return movie_dict
print(group_by_year(data))