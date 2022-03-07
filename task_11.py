import json
# from bs4 import BeautifulSoup
# from Task_5 import get_movies_list_detail
with open("task5.json","r") as f:
    j=json.load(f)
def analyse_movies_genre(j):
    list=[]
    list1=[]
    for i in j:
        a=i["Genre:"].split()
        for l in a:
            if l[-1]==",":
                l=l[:-1]
                # print(l)
                list.append(l)
    # print(list)
    for i in list:
        if i not in list1:
            list1.append(i)
    # print(list1)
    dic={}
    for i in (list1):
        count=0
        k=0
        while k <len(list):
            if i==list[k]:
                count=count+1
            k=k+1
        dic.update({i:count})
        # print(dic)
    with open("task11.json","w")as file:
     json.dump(dic,file,indent=4)
analyse_movies_genre(j)


