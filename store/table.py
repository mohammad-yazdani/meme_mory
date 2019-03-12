from store.db import DB


class Table:

    def __init__(self, name: str, columns: dict):
        drop: str = "DROP TABLE IF EXISTS " + name
        DB.exec(drop)
        DB.commit()

        decl: str = "CREATE TABLE IF NOT EXISTS " + name
        cols: str = " (id INTEGER PRIMARY KEY AUTOINCREMENT"
        for key in columns.keys():
            cols += (", " + key)
            cols += (" " + columns[key])
        cols += ");"
        DB.exec(decl + cols)
        DB.commit()
