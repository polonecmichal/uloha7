#prevod obsahu spravy do inej abecedy pomocou kluca, zaklad je verejny
#sifrovanie ej symetricke 
#stetanografia - ukryvanie spravy v inom subore, napr. obrazku
#hashovanie - vytvorenie otlacku, hash sa pouziva na over


#nech existuje sprava "Ahoj#", zoberem pismeno a priradim mu hodnotu z ASCII tabulky, napr. A=65, h=104, o=111, j=106, #=35
#dohdnem sa ze kolko bitov budem mat pismeno (7bitov), keby je dlzka kodovania mensia ako 7 bitov tak musim doplnit nuly zlava, napr. A=1000001
#na jedno pismeno potrebujeme 7 pixelov, dohoda je ze zaciname od lava, 1 pixle je tuple, kodujeme iba do modrej farby, prevedieme hodnotu do dvojkovej sustavy
# a zmenime poslednu hodnotu 

import PIL
from PIL import Image
obr = Image.open(r"C:\Users\misko\Desktop\shhhhhhh\shhh-dog.png")
sprava = input("Zadaj co idem zakodovat: ")
def sprava_tobin(sprava):
    sprava += '#'
    output = ""
    for char in sprava:
        temp = bin(ord(char))[2:]
        if len(temp) < 7:
            pocet = 7 - len(temp)
            temp = '0' * pocet + temp
        output += temp
    return output

def talian(bs, obr):
    for i in range(len(bs)):
        pixels = obr.load()
        x = i % obr.size[0]
        y = i // obr.size[0]
        bluebin = bin(pixels[x,y][2])[2:-1:] #2 odtrhne 0b, -1 odtrhne posledny symbol
        bluebin = bluebin + bs[i]
        new_blue = int(bluebin, 2)
        pixels[x, y] = (pixels[x,y][0], pixels[x,y][1], new_blue)
obr.save("rodinnepripady.png")

#DU naopak
bin_Sprava = sprava_tobin(sprava)
talian(bin_Sprava, obr)
obr.show()