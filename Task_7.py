import json 
# from bs4 import BeautifulSoup
# from task__5 import get_movies_list_details
with open("task5.json","r") as a:
    h=json.load(a)
    # print(h)
def analyse_movies_directors(h):
    list=[]
    list2=[]
    for i in h:
        # if i["Director:"]not in list:
        list.append(i["Director:"])
    # print(list)
    for j in list:
        if j not in list2:
            list2.append(j)
    # print(list2)
    list3=[]
    for k in list2:
        c=0
        for l in list:
            if k==l:
                c=c+1
        list3.append(c)
    # print(list3)
    dic={}
    for i in range(len(list2)):
        dic[list2[i]]=list3[i]
    # print(dic)
    with open("task7.json","w")as file:
     json.dump(dic,file,indent=4)
analyse_movies_directors(h)