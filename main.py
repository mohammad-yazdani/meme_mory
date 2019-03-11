from model.meme import Meme

while True:
    my_prompt: str=input( )
    params: list=my_prompt.split(" ")
    this_meme=Meme(my_prompt[0],"",my_prompt[1],my_prompt[2],my_prompt[3],my_prompt[4])


