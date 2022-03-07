import json
def analyse_movies_language():
    language_list=open("task5.json","r")
    list=json.load(language_list)
    print(list)
    list1=[]
    dict={}
    for i in list:
        if (i["Original Language:"])not in list1:
            list1.append(i["Original Language:"])
            # print(list1)
            dic={}
            list2=[]
            for g in list1:
                i=0
                count=0
                while i<len(list):
                    if g==list[i]["Original Language:"]:
                        count=count+1
                        # print(count)
                    i=i+1
                dic.update({g:count})
                print(dic)
            list2.append(dic)
            print(list2)
    with open("task6.json","w")as file:
        json.dump(list2,file,indent=2)
analyse_movies_language()