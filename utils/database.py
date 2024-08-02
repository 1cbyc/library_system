import sqlite3
from models.book import Book
from models.member import Member
from models.borrowing_record import BorrowingRecord


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS books (
                                    id INTEGER PRIMARY KEY,
                                    title TEXT,
                                    author TEXT,
                                    genre TEXT,
                                    isbn TEXT,
                                    copies INTEGER
                                )''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS members (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT,
                                    email TEXT,
                                    phone TEXT
                                )''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS borrowing_records (
                                    id INTEGER PRIMARY KEY,
                                    book_id INTEGER,
                                    member_id INTEGER,
                                    borrow_date TEXT,
                                    due_date TEXT,
                                    return_date TEXT,
                                    FOREIGN KEY(book_id) REFERENCES books(id),
                                    FOREIGN KEY(member_id) REFERENCES members(id)
                                )''')

    def add_book(self, book):
        with self.conn:
            self.conn.execute('INSERT INTO books (title, author, genre, isbn, copies) VALUES (?, ?, ?, ?, ?)',
                              (book.title, book.author, book.genre, book.isbn, book.copies))

    def get_all_books(self):
        cursor = self.conn.execute('SELECT * FROM books')
        books = [Book(*row[1:]) for row in cursor.fetchall()]
        return books

    def search_books(self, query):
        cursor = self.conn.execute('SELECT * FROM books WHERE title LIKE ? OR author LIKE ?',
                                   ('%' + query + '%', '%' + query + '%'))
        books = [Book(*row[1:]) for row in cursor.fetchall()]
        return books

    def update_book(self, book_id, **kwargs):
        columns = ', '.join(f"{k} = ?" for k in kwargs.keys())
        values = list(kwargs.values()) + [book_id]
        with self.conn:
            self.conn.execute(f'UPDATE books SET {columns} WHERE id = ?', values)

    def delete_book(self, book_id):
        with self.conn:
            self.conn.execute('DELETE FROM books WHERE id = ?', (book_id,))

    def add_member(self, member):
        with self.conn:
            self.conn.execute('INSERT INTO members (name, email, phone) VALUES (?, ?, ?)',
                              (member.name, member.email, member.phone))

    def get_all_members(self):
        cursor = self.conn.execute('SELECT * FROM members')
        members = [Member(*row[1:]) for row in cursor.fetchall()]
        return members

    def add_borrowing_record(self, borrowing_record):
        with self.conn:
            self.conn.execute(
                'INSERT INTO borrowing_records (book_id, member_id, borrow_date, due_date, return_date) VALUES (?, ?, ?, ?, ?)',
                (borrowing_record.book_id, borrowing_record.member_id, borrowing_record.borrow_date,
                 borrowing_record.due_date, borrowing_record.return_date))

    def get_all_borrowing_records(self):
        cursor = self.conn.execute('SELECT * FROM borrowing_records')
        borrowing_records = [BorrowingRecord(*row[1:]) for row in cursor.fetchall()]
        return borrowing_records
