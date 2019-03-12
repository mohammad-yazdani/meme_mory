from model.meme import Meme
from model.tag import Tag
from model.link import Link

from store.db import DB

from PIL import Image

from external.pull import Fetch

DB.start()
Meme.create_table()
Tag.create_table()
Link.create_table()

Meme("meme0.jpeg", ["sad", "bad", "gross"])

Meme.search_by_tags(["sad"])

exit(0)

Fetch(["sad", "bad"])

ctrl = input()
if ctrl == 'put':
    while True:
        my_prompt: str = input()
        params: list = my_prompt.split(" ")
        Meme(params[0], params[1])
elif ctrl == 'get':
    meme_in: str = input()
    meme: str = Meme.search_by_tags(meme_in.split(" "))
    img = Image.open(meme)
    img.show()
