import sqlite3

"""
This class starts the connection with database and closes it
"""


class Database:

    def __enter__(self):
        self.conn = sqlite3.connect('database.db')
        return self.conn

    def __exit__(self, type, value, traceback):
        self.conn.close()
