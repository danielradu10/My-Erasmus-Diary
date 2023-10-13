import sqlite3
import os
from collections import namedtuple

Verse = namedtuple("Verse", ["id", "verse", "author", "chapter", "numbers", "category", "ziua"])

class DataBaseManager:

    CREATE_CMD = '''CREATE TABLE IF NOT EXISTS verses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    verse VARCHAR(600) NOT NULL,
    author VARCHAR(100) NOT NULL,
    chapter INTEGER NOT NULL,
    numbers VARCHAR(10) NOT NULL,
    category VARCHAR(100) NOT NULL,
    ziua VARCHAR(100) NOT NULL) '''

    INSERT_CMD = '''INSERT INTO verses(verse, author, chapter, numbers, category, ziua)
    VALUES (?, ?, ?, ?, ?, ?)'''

    SELECT_BY_ID_CMD = '''SELECT * FROM verses WHERE id = ?'''

    SELECT_BY_CATEGORY_CMD = '''SELECT * FROM verses WHERE category = ?'''


    CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
    DATABASE_PATH = os.path.join(CURRENT_PATH, 'verses.db')

    def __init__(self):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.CREATE_CMD)
            cursor.close()

    def insert(self, verset):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.INSERT_CMD,
                   (verset.verse, verset.author, verset.chapter, verset.numbers, verset.category, verset.ziua))
            cursor.close()

    def select_by_id(self, verse_id):
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.SELECT_BY_ID_CMD, (verse_id,))
            row = cursor.fetchone()
            cursor.close()
            if row:
                return Verse(*row)
            return None

    def select_by_category(self, verse_category):
        verses = []
        with sqlite3.connect(self.DATABASE_PATH) as db:
            cursor = db.cursor()
            cursor.execute(self.SELECT_BY_CATEGORY_CMD, (verse_category,))
            rows = cursor.fetchall()
            cursor.close()
            for row in rows:
                verses.append(Verse(*row))
            return verses






