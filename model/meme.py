from store.db import DB


class Meme:
    db: list = list()

    def __init__(self, file_path: str, em1: str = "",
                 em2: str = "", em3: str = "", em4: str = ""):
        self.file_path = file_path
        self.em1 = em1
        self.em2 = em2
        self.em3 = em3
        self.em4 = em4

        # DB.exec("INSERT INTO memes (file, tag1, tag2, tag3, tag4) VALUES "
        #        "({file}, {tag1}, {tag2}, {tag3}, {tag4})"
        #        .format(file=self.file_path, tag1=self.em1, tag2=self.em2, tag3=self.em3, tag4=self.em4))

    @staticmethod
    def match_meme_to_tags(tags: list):
        pass  # TODO
