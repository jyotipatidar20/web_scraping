import json
import pprint
with open("task5.json","r") as f:
    data1=json.load(f)
    # print(data1)

def language_and_directores(movies_list):
    Dict={}
    for movies in movies_list:
        # print(movies)
        for Director in movies:
            # print(Director)
            if Director=="Director:":
                Dict[movies[Director]]={}
                # print(Dict)
    for i in range(len(movies_list)):
        # print(i)
        for Director in Dict:
            # print(Director)
            if Director in movies_list[i][ "Director:"]:
                for language in movies_list[i]:
                    if language=="Original Language:":
                        a=movies_list[i]["Original Language:"]
                        Dict[Director][a]=0
    for i in range(len(movies_list)):
        for Director in Dict:
            if Director in movies_list[i][ "Director:"]:
                for language in movies_list[i]:
                    if language=="Original Language:":
                        for l in Dict[Director]:
                            Dict[Director][l]+=1
    return Dict
Director_language=language_and_directores(data1)
with open("task10.json","w") as f:
    json.dump(Director_language,f,indent=4)
(Director_language)

#     with open("task10.json","w") as f:
#         json.dump(dict,f,indent=4)
#     return Dict
# language_and_directores(data1)
