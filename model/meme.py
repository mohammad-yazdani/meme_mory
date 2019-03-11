import sqlite3

from store.db import DB


class Meme:
    db: list = list()

    def __init__(self, file_path: str, em1: str = "null",
                 em2: str = "null", em3: str = "null", em4: str = "null"):
        self.file_path = file_path
        self.em1 = em1
        self.em2 = em2
        self.em3 = em3
        self.em4 = em4
        query = "INSERT INTO memes (file, tag1, tag2, tag3, tag4) VALUES " \
                "('{file}', '{tag1}', '{tag2}', '{tag3}', '{tag4}')" \
            .format(file=self.file_path, tag1=self.em1, tag2=self.em2, tag3=self.em3, tag4=self.em4)
        try:
            DB.exec(query)
            DB.commit()
        except sqlite3.IntegrityError:
            pass

    @staticmethod
    def match_meme_to_tags(tags: list):
        pass  # TODO
