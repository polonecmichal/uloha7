import random
def generuj(n:int) -> list:
    zoznam = []
    for i in range(n):
        cislo = random.randint(1, 100)
        zoznam.append(cislo)
    return zoznam

zoznam = generuj(10)
print(zoznam)   

def vkladanie(zoznam:list) -> list:
    for i in range(1, len(zoznam)):
        kluc = zoznam[i]
        final = max(i - 1, 0)
        while final >= 0 and kluc < zoznam[final]:
            zoznam[final + 1] = zoznam[final]
            final -= 1
        zoznam[final + 1] = kluc
    return zoznam
print(vkladanie(zoznam))