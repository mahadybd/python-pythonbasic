from book import Book
import bookSDK

# book = Book("Learn Python Basic", 80)
# # print(bookSDK.add_book(book))

# print(bookSDK.get_books())

# print(bookSDK.get_book_by_title("Learn Python Basic"))

# Console app--------------
def print_menu():
    print("""Chose an option:
    1. print all books
    2. Add a Book
    3. Update a Book
    4. Delete a Book
    5. Quit
    """)

while True:
    print_menu()
    response = int(input())
    if response == 1:
        for book in bookSDK.get_books():
            print(book)
    elif response == 2:
        print("What is the name of book?")
        title = input()
        print("Pages?")
        pages = int(input())
        bookSDK.add_book(Book(title, pages))
    elif response == 3:       
        print("Current title?")
        current_title = input()
        print("Current pages?")
        current_pages = int(input())
        print("New title (s for same)")
        new_title = input()
        if str.lower(new_title) == 's':
            new_title = current_title
        print("New pages? (s for same)")
        new_pages = int(input())
        if str.lower(new_pages) == 's':
            new_pages = current_pages
        bookSDK.update_book(Book(current_title, current_pages), new_title, new_pages)    
    elif response == 4:
        print("Title of the book that want to delete?")
        title = input()
        print("Pages?")
        pages = int(input())
        bookSDK.delete_book(Book(title, pages))
    else:
        print("Thanks for using our app")
        break