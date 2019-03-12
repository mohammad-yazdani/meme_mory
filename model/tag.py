from store.table import Table
from store.db import DB


class Tag:
    value: str
    row_id: int

    def __init__(self, value: str):
        self.value = value
        DB.exec("INSERT INTO tags (value) VALUES (?)", [value])
        self.row_id = DB.commit()

    @staticmethod
    def create_table():
        Table("tags", {"value": "TEXT UNIQUE"})
