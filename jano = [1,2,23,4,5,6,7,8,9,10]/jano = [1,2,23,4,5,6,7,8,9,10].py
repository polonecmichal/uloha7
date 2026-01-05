z = [4, 1, 5, 27, -7,12] 

def ktory_min(z):
    minimum = z[0]
    for cislo in zoznam:
        if cislo < minimum:
            minimum = cislo 
            
    return minimum