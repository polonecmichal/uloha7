#from PIL import Image
#pic = Image.new(mode="RGB", size=(256, 256), color= "white")
#pixels = pic.load()
#for y in range(pic.size[1]):
#    for x in range(pic.size[0]):
#        pixels[x, y] = ((x + y) % 256, (x + y) % 256, 125)
#pic.show()
#pic.save("akosomnasielstarybicyel.png")


from PIL import Image
pic = Image.open(r"C:\Users\misko\Desktop\bs\shhh-dog.png")
pixels = pic.load()
for y in range(pic.size[1]):
    for x in range(pic.size[0]):
        temp = pixels[x, y] 
        pixels[x, y] = pixels[x, pic.size[1] - 1 - y]
pic.show()