import time
from time import sleep

prompt = "press e to enter book details, r to retrieve book details, d to delete book, m to mark as read, q to exit:  "
books = []

def add_books():
 book_name = input("Enter the book name: ")
 author_name = input("enter the author name: ")
 print("Book has been added")

 books.append({
        "name": book_name,
        "author": author_name,
        "read": False
 })

def retrieve_books():
    bookname = input("Enter the book name: ")
    for book in books:
        if book["name"] == bookname:
           print("Searching...")
           time.sleep(2)
           print("Here it is:-")
           print(book)
        else:
            print("Searching...")
            time.sleep(3)
            print("That book not found")

def markasread():
    readbook = input("Enter the book you want to read as true: ")
    for book in books:
        if book["name"] == readbook:
          book["read"] = True
          print("marking as read...")
          time.sleep(2)
          print("That book marked as read")



def delete_book():
    deletebook = input("Enter the book you want to delete: ")
    for book in books:
        if book == books["name":deletebook]:
            books.remove(book)
            print("Deleting book...")
            time.sleep(2)
            print("Book has been deleted")

user_options = {
    "e" : add_books,
    "r" : retrieve_books,
    "d" : delete_book,
    "m" : markasread
}



def menu():
 selection = input(prompt)
 while selection !="q":
    if selection in user_options:
        selected = user_options[selection]
        selected()
    else:
        print("Unknown command try again!")
    selection = input(prompt)
menu()



