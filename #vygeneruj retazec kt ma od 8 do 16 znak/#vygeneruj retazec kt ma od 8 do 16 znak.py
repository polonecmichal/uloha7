#vygeneruj retazec kt ma od 8 do 16 znakov tak aby sa striedala spoluhlaska a samohlaska
import random
string = " "
samo = "aeiouy"
spolu ="bcdfghjklmnopqrstvwxyz"
random.randrange(8, 17)
for i in range(random.randrange(8, 17)):
    if i % 2 == 0:
        temp = random.choice(samo)
        string += temp
    else:
        temp = random.choice(spolu)
        string += temp
print(string)