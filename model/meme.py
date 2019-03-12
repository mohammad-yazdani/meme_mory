import sqlite3

from store.db import DB
from store.table import Table

from model.tag import Tag
from model.link import Link

import os.path


class Meme:
    db: list = list()

    def __init__(self, file_path: str, tags: list):
        image_format: str = os.path.splitext(file_path)[1]
        with open(file_path, "rb") as meme_file:
            file_binary = meme_file.read()
            self.tags = tags

            blob = sqlite3.Binary(file_binary)
            query = 'INSERT INTO memes (file, image_format) VALUES (?, ?)'
            meme_id: int = -1
            try:
                DB.exec(query, [blob, image_format])
                meme_id = DB.commit()
            except sqlite3.IntegrityError:
                pass
            for tag in tags:
                tag_obj: Tag = Tag(tag)
                Link(meme_id, tag_obj.row_id)

    @staticmethod
    def create_table():
        Table("memes", {"file": "BLOB", "image_format": "VARCHAR(32)"})

    @staticmethod
    def search_by_tags(tags: list):
        in_clause: str = "("
        for tag in tags:
            in_clause += tag + ", "
        in_clause += "null)"
        res: list = DB.fetch(
            "SELECT * FROM links WHERE (SELECT value FROM tags WHERE tags.id = tag_id) in " + in_clause)
        print(res)
