def faktorial(n):

    vysledok = 1
    for i in range(2, n + 1):
        vysledok *= i
    return vysledok

pokus = faktorial(5)
print(pokus)

def combcis(k, n):
    return faktorial(n) // (faktorial(k) * faktorial(n - k))

pokus2 = combcis(2, 5)
print(pokus2)

def pascalov_trojuholnik(velkost):
    for riadok in range (velkost):
        for stlpec in range(riadok + 1):
            print(combcis,(riadok, stlpec), end = "")
            trojuholnik = pascalov_trojuholnik
            print(trojuholnik)