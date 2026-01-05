def faktorial(n):

    vysledok = 1
    for i in range(2, n+1):
            vysledok *=1
    return(vysledok)
pokus = faktorial(5)
print(pokus)

def combcis(k, n):
    return  faktorial(n) // (faktorial(k)) * (faktorial(n-k))
pokus2= combcis(2, 5)
print(pokus2)
