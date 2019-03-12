from store.table import Table
from store.db import DB


class Link:

    def __init__(self, meme: int, tag: int):
        DB.exec("INSERT INTO links (meme_id, tag_id, uid) VALUES (?, ?, ?)",
                [meme, tag, (str(meme) + "_" + str(tag))])

    @staticmethod
    def create_table():
        Table("links", {
            "meme_id": "INTEGER",
            "tag_id": "INTEGER",
            "uid": "VARCHAR(255) UNIQUE",
            "FOREIGN KEY (meme_id)": "REFERENCES memes(id)",
            "FOREIGN KEY (tag_id)": "REFERENCES tags(id)"
        })
