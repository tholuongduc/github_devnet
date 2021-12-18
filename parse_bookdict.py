import json

with open ('bookdict.json') as json_file:
    book_json = json.load(json_file)
#print(book_json)
for i in range(len(book_json)):
    each_book = book_json[i]
    print(f'The book id: {i}\nBook title: {each_book["title"]}\nBook author: {each_book["author"]}')
    