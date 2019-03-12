import sqlite3
from sqlite3.dbapi2 import Connection, Cursor


class DB:
    __conn: Connection = None
    __cursor: Cursor = None

    def __del__(self):
        if DB.__conn is not None:
            DB.__conn.close()

    @staticmethod
    def start():
        DB.__conn = sqlite3.connect("data.db")
        DB.__cursor = DB.__conn.cursor()

    @staticmethod
    def commit():
        DB.__conn.commit()
        return DB.__cursor.lastrowid

    @staticmethod
    def exec(q: str, args=None):
        if args is None:
            args = []
        DB.__cursor.execute(q, args)

    @staticmethod
    def fetch(q: str, args=None):
        if args is None:
            args = []
        DB.__cursor.execute(q, args)
        return DB.__cursor.fetchall()
