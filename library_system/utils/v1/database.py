import sqlite3


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
