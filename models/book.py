# class Book:
#     def __init__(self, title, author, genre, isbn, copies):
#         self.title = title
#         self.author = author
#         self.genre = genre
#         self.isbn = isbn
#         self.copies = copies
#
#     def __repr__(self):
#         return f"<Book(title={self.title}, author={self.author}, genre={self.genre}, isbn={self.isbn}, copies={self.copies})>"

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
