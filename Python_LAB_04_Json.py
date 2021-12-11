import json
file = open("myjson.json","r")
str = ""
for item in file:
    item = item.strip()
    str += item + "\n"
#Convert string to dict
new_dic = json.loads(str)
#print value of token
for key in new_dic:
    if "_token" in key:
        print(f'{key}:{new_dic.get(key)} \n')
file.close()