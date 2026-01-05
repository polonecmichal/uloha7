vstup = input("zadaj mi co idem heslovat:")
kluc ="abc"
novy_kluc = kluc * (len(vstup)//len(kluc)) + kluc[:len(vstup)%len(kluc):]
print(len(novy_kluc), len(vstup))
vystup = ""

for i in range(len(vstup)):
    znak = ord(vstup[i])
    if ord('a') <= ord(vstup[i]) and ord(vstup[i]) <= ord('z') :
        posun = ord(novy_kluc[i])-ord('a')+1
        ord(vstup[i]) + posun % 26
        vystup += chr((ord(vstup[i]) - ord('a') + posun)%26 + ord('a'))
    else:
        vystup += vstup[i]

print(vystup)