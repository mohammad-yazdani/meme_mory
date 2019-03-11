from model.emotion import Emotion


class Meme:
    db: list = list()

    def __init__(self, file_path: str, text: str, em1: int, em2: int, em3: int, em4: int):
        self.file_path = file_path
        self.text = text
        self.em1 = em1
        self.em2 = em2
        self.em3 = em3
        self.em4 = em4

        Meme.db.append(self)

    @staticmethod
    def match_meme_to_emotion(em: Emotion):
        pass  # TODO
