n = []
val10 = 0
val15 = 0
val20 = 0

for n in range(10):
    while True :
        n = int(input("Entrez une valeur entre 0 et 20 : "))
        if n < 20 or n > 0 :
            break
        else:
            print("Réesayez !")

    if n < 10:
        val10 += 1
        print("Le nombre de valeur inférieur strictement à 10 est :",val10)
    elif n < 15:
        val15 += 1
        print("Le nombre de valeurs supérieur = ou égale à 10 est infétieur strictement à 15 est :", val15)
    else:
        val20 += 1
        print("Le nombre de valeurs supérieur ou égale à 15", val20)




