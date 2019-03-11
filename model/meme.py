import sqlite3

from store.db import DB


class Meme:
    db: list = list()

    def __init__(self, file_path: str, em1: str = "null",
                 em2: str = "null", em3: str = "null", em4: str = "null"):
        with open(file_path, "rb") as meme_file:
            self.file_binary = meme_file.read()
            self.em1 = em1
            self.em2 = em2
            self.em3 = em3
            self.em4 = em4

            blob = sqlite3.Binary(self.file_binary)
            query = "INSERT INTO memes (file, tag1, tag2, tag3, tag4) VALUES (?, ?, ?, ?, ?)"
            try:
                DB.exec(query, [blob, self.em1, self.em2, self.em3, self.em4])
                DB.commit()
            except sqlite3.IntegrityError:
                pass

    @staticmethod
    def match_meme_to_tags(tags: list):
        DB.exec("SELECT file FROM memes WHERE tag1=? OR tag2=? OR tag3=? OR tag4=?", tags[0:4])
        file = DB.cursor.fetchone()
        with open("test.jpeg", "wb") as meme_out:
            meme_out.write(file[0])
        return "test.jpeg"
