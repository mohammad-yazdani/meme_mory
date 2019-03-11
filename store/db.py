import sqlite3


class DB:
    conn: sqlite3.dbapi2 = None
    cursor = None

    @staticmethod
    def start():
        DB.conn = sqlite3.connect("data.db")
        DB.cursor = DB.conn.cursor()
        DB.cursor.execute("CREATE TABLE IF NOT EXISTS memes ("
                          "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                          "file BLOB UNIQUE, "
                          "tag1 TEXT, "
                          "tag2 TEXT, "
                          "tag3 TEXT, "
                          "tag4 TEXT)")

    @staticmethod
    def commit():
        DB.conn.commit()

    @staticmethod
    def __del__(self):
        DB.conn.close()

    @staticmethod
    def exec(q: str, args: list):
        DB.cursor.execute(q, args)
