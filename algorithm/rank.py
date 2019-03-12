from typing import List
from model.meme import Meme


class Rank:

    def __init__(self, data: List[Meme]):
        self.data = data  # TODO : Expects data sorted by rank

    def match_by_tags(self, tags: list):
        highest_overlap = 0
        match: Meme = None
        for meme in self.data:
            intersection = set(tags) & set(meme.tags)
            overlap = max(highest_overlap, len(intersection))
            if overlap > highest_overlap:
                highest_overlap = overlap
                match = Meme
        if match is not None:
            return match
        else:
            return self.data[0]
