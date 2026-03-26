slovo = "Hello, World!"
brzko =" "
dlzka = len(slovo) -1
for letters in slovo:
    letter = str(slovo[dlzka])
    dlzka -= 1
veta = str(letter * dlzka)
print(veta)