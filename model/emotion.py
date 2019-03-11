class Emotion:
    db: dict = dict()

    def __init__(self, keyword: str, tags: list):
        self.keyword = keyword
        self.tags = tags

        Emotion.db[self.keyword] = self

    @staticmethod
    def query_meme(q: list):
        pass  # TODO

    @staticmethod
    def query_emotion(q: list):
        pass  # TODO
