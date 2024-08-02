# from controllers.book_controller import BookController
# from 1cbyc_library_system.controllers.book_controller import BookController
from library_system.controllers.book_controller import BookController

class BookView:
    def __init__(self):
        self.controller = BookController()

    def display_books(self):
        books = self.controller.get_all_books()
        for book in books:
            print(book)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        genre = input("Enter book genre: ")
        isbn = input("Enter book ISBN: ")
        copies = int(input("Enter number of copies: "))
        self.controller.add_book(title, author, genre, isbn, copies)
