vystup = ""
def rozsekaj(text: str, sirka: int) -> str:
    vystup = ""
    for i in range(0, len(text), sirka):
        vystup += text[i : i + sirka]
        vystup += "\n"
    return(vystup)
print(rozsekaj('Anicka dusicka, kde si bola', 10))