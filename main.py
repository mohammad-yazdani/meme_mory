from model.meme import Meme
from store.db import DB
from PIL import Image

DB.start()

ctrl = input()
if ctrl == 'put':
    while True:
        my_prompt: str = input()
        params: list = my_prompt.split(" ")
        Meme(params[0], params[1], params[2], params[3], params[4])
elif ctrl == 'get':
    meme_in: str = input()
    meme: str = Meme.match_meme_to_tags(meme_in.split(" "))
    img = Image.open(meme)
    img.show()
