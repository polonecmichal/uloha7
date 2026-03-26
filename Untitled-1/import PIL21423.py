import PIL
from PIL import Image
obr = Image.open(r"C:\Users\misko\Desktop\shhhhhhh\shhh-dog.png")

def krados(bs, obr):
    pixels = obr.load()
    for i in range(len(bs)):
        x = i % obr.size[0]
        y = i // obr.size[0]
        farba = bin(pixels[x,y][2])[2:] #toto by malo brat hodnotu modrej
        if len(farba) < 8:
            farba = '0'*(8-len(farba)) + farba
        result = int(farba, 2)
        print(result)