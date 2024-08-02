from models.book import Book
from utils.database import Database


class BookController:
    def __init__(self):
        self.db = Database()

    def add_book(self, title, author, genre, isbn, copies):
        new_book = Book(title, author, genre, isbn, copies)
        self.db.add_book(new_book)

    def get_all_books(self):
        return self.db.get_all_books()

    def search_books(self, query):
        return self.db.search_books(query)

    def update_book(self, book_id, **kwargs):
        self.db.update_book(book_id, **kwargs)

    def delete_book(self, book_id):
        self.db.delete_book(book_id)
