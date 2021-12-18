import requests
import json


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

#Show menu
def show_menu():
    print('''Please select program mode:
        1) Show all books
        2) Add new book
        3) Edit existing book
        4) Delete existing book
        5) Search contact by book id
        6) Search contact by book author
        7) Exit program
          ''')
#Select program mode
def get_choice():
    return input("Please select mode: ")

#Define function to get all books infor
def get_all_books():
    r = requests.get(f'{APIHOST}/api/v1/books?includeISBN=true')
    if r.status_code == 200:
        jsondata = r.json()
        for i in range(len(jsondata)):
            each_book = jsondata[i]
            print(f'Book id: {i}\nBook title: {each_book["title"]}\nBook author: {each_book["author"]}\nISBN: {each_book["isbn"]}')
    else:
        print(f"Status code {r.status_code} and text {r.text}, while trying to get all books information.")


#Define function to search existing book infor by id
def get_existing_book_id(book_id):
    r = requests.get(f'{APIHOST}/api/v1/books/{book_id}')
    if r.status_code == 200:
        jsondata = r.json()
        print(f'Book id: {jsondata["id"]}\nBook title: {jsondata["title"]}\nBook author: {jsondata["author"]}')
    else:
        print(f"Status code {r.status_code} and text {r.text}, while trying to get book information.")

#Define function to search existing book infor by author
def get_existing_book_author(book_author):
    r = requests.get(f'{APIHOST}/api/v1/books?author={book_author}')
    if r.status_code == 200:
        jsondata = r.json()
        print(f'Book id: {jsondata[0]["id"]}\nBook title: {jsondata[0]["title"]}\nBook author: {jsondata[0]["author"]}')
    else:
        print(f"Status code {r.status_code} and text {r.text}, while trying to get book information.")

#Define function to delete book by id
def delete_book(book_id, apiKey):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/{book_id}", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            }
    )
    if r.status_code == 200:
        print(f'Book id {book_id} deleted')
    else:
        print(f"Status code {r.status_code} and text {r.text}, while trying to delete book {book_id}.")

#Define function to get Authen token
def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        print(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

def addBook(book, apiKey):
    r = requests.post(
        f"{APIHOST}/api/v1/books", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Book {book} added.")
    else:
        print(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")

#Define function to edit existing book 
def edit_book(book, apiKey):
    book_id = book["id"]
    r = requests.put(
        f"{APIHOST}/api/v1/books/{book_id}", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Book {book} modified.")
    else:
        print(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")


#main
apiKey = getAuthToken()   # Get the Auth Token Key
while True:
    show_menu()
    user_choice = get_choice()
    print("You select mode: " + user_choice)

    if user_choice == "7":
        break
    elif user_choice == "1":
        all_books = get_all_books()
    elif user_choice == "2":
        book = {"id": int(input("Book ID:")), "title": input("Title:"), "author": input("Author:"), "isbn": input("ISBN:")}
        addBook(book, apiKey)
    elif user_choice == "3":
        book = {"id": int(input("Book ID:")), "title": input("Title:"), "author": input("Author:")}
        edit_book(book, apiKey)
    elif user_choice == "4":
        book_id = input("Please enter book id:")
        delete_book(book_id, apiKey)
    elif user_choice == "5":
        book_id = input("Please enter book id:")
        book_data = get_existing_book_id(book_id)
    elif user_choice == "6":
        book_author = input("Enter book author:")
        get_existing_book_author(book_author)
    else:
        print("Invalid mode! Try again!")