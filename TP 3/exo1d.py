n = 0
valeur = 0
i = 0


n = int(input("Entrez un nombre X, entier supérieur à 1 : "))

while valeur <= n:
    valeur = valeur + i
    i = i + 1


print("Le plus grand nombre N tel que (∑i) de 0 à N ≤ X est ",i)