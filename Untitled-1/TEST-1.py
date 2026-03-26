def krados(bs, obr):
    pixels = obr.load()  # Načítame raz
    sirka = obr.size[0]
    
    for i in range(len(bs)):
        x = i % sirka
        y = i // sirka
        
        # Získame binárnu hodnotu modrej (index 2)
        farba = bin(pixels[x, y][2])[2:] 
        
        # Správne doplnenie núl ZĽAVA, aby mal bajt 8 bitov
        if len(farba) < 8:
            farba = ('0' * (8 - len(farba))) + farba
            
        # Prevod z binárnej sústavy na číslo (a prípadne na znak)
        cislo = int(farba, 2)
        znak = chr(cislo)
        
        print(f"Pôvodná hodnota: {cislo} -> Znak: {znak}")

# Ak je bs napríklad text, ktorý hľadáš, alebo len rozsah
# krados(range(10), obr)