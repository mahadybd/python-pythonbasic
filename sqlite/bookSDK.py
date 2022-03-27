import re
import sqlite3
from book import Book

def cursor():
    return sqlite3.connect('books.db').cursor()

c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
c.connection.close()

# def add_book(book):
#     c = cursor()

#     with c.connection:
#         c.execute('INSERT INTO books VALUES (?, ?)', (book.title, book.pages))
#     c.connection.close() 
#     return c.lastrowid

# return all books-----------
# def get_books():
#     c = cursor()

#     with c.connection:
#         c.execute('SELECT * FROM books')

#     return c.fetchall()

# return all books in list in list-----------
def get_books():
    c = cursor()
    books = []

    with c.connection:
        for book in c.execute('SELECT * FROM books'):
            books.append(Book(book[0], book[1]))
    c.connection.close() 
    return books

def get_book_by_title(title):
    c = cursor()
    with c.connection:
        # c.execute('SELECT * FROM books WHERE title=' + title ) # will be a sql injection
        c.execute('SELECT * FROM books WHERE title=?', (title,)) # single tuple used to avoid sql injection
    data = c.fetchone()
    c.connection.close() 
    if not data:
        return None

    return Book(data[0], data[1])

def update_book(book, new_title, new_pages):
    c = cursor()
    with c.connection: #don't forget this part.
        c.execute('UPDATE books SET title=?, pages=? WHERE title=? AND pages=?', 
        (new_title, new_pages, book.title, book.pages))
    book = get_book_by_title(book.title) #after commit
    c.connection.close()
    return book    
