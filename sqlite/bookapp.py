from book import Book
import bookSDK

book = Book("Learn Python Basic", 80)
# print(bookSDK.add_book(book))

print(bookSDK.get_books())

print(bookSDK.get_book_by_title("Learn Python Basic"))