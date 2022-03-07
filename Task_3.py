from Task_2 import scrap_top_list
import json
with open("movie_year_task_2.json","r") as f:
    decap=json.load(f)
    # print(decap)
def group_by_decade (top_movies):
    movie_dec={}
    list=[]
    for i in top_movies:
        # print(i)
        a = int(i)%10
        decade=int(i)-a
        if decade not in list:
            list.append(decade)
    list.sort()
    print(list)
    for j in list:
        movie_dec[j]=[]
    # print(movie_dec)
    for j in movie_dec:
            r=j+9
            for x in top_movies:
                if int(x)<=r and int(x)>=j:
                    for y in top_movies[x]:
                        movie_dec[j].append(y)
    # print(movie_dec)
    with open("group_decape_task_3.json","w") as file:
            json.dump(movie_dec,file,indent=4)
    return(movie_dec)
print(group_by_decade(decap))



