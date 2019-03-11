from model.meme import Meme
from store.db import DB

DB.start()

if input() == 'put':
    while True:
        my_prompt: str = input( )
        params: list = my_prompt.split(" ")
        this_meme = Meme(params[0],params[1],params[2],params[3],params[4])
elif input() == 'get':
    pass

