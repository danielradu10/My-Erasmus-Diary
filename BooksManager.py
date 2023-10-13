import sqlite3
import os
from collections import namedtuple

Book = namedtuple("Book", ["id", "nume", "author", "pagina", "total_pagini", "luna"])

class BooksManager:

    CREATE_CMD = '''CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nume VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    pagina INTEGER NOT NULL,
    total_pagini INTEGER NOT NULL,
    luna VARCHAR(100) NOT NULL) '''

    INSERT_CMD = '''INSERT INTO books(nume, author, pagina, total_pagini, luna)
    VALUES (?, ?, ?, ?, ?)'''

    SELECT_BY_ID_CMD = '''SELECT * FROM books WHERE id = ?'''

    SELECT_BY_MONTH_CMD = '''SELECT * FROM books WHERE luna = ?'''


    CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
    DATABASE_PATH = os.path.join(CURRENT_PATH, 'books.db')

    def __init__(self):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.CREATE_CMD)
            cursor.close()

    def insert(self, book):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.INSERT_CMD,
                   (book.nume, book.author, book.pagina, book.total_pagini, book.luna))
            cursor.close()

    def select_by_id(self, book_id):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.SELECT_BY_ID_CMD, (book_id,))
            row = cursor.fetchone()
            cursor.close()
            if row:
                return Book(*row)
            return None

    def select_by_luna(self, luna):
        verses = []
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.SELECT_BY_MONTH_CMD, (luna,))
            rows = cursor.fetchall()
            cursor.close()
            for row in rows:
                verses.append(Book(*row))
            return verses







