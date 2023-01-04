prix = [0] * 24
prix1 = 0
prix2 = 0


while True:
    heurelocation = int(input("Donnez l’heure de début de la location  : "))
    if 0 <= heurelocation <= 24:
        break
    else:
        print("Les heures doivent être comprises entre 0 et 24 !")

while True :
    heurefinlocation = int(input("Donnez l’heure de fin de la location (un entier) : "))
    if 0 <= heurefinlocation <= 24 and heurelocation != 24:
        break
    elif heurelocation == heurefinlocation:
        print("Attention ! l’heure de fin est identique à l’heure de début.")

    else:
        print("Les heures doivent être comprises entre 0 et 24 !")


for i in range(heurelocation, heurefinlocation):

    if 7 <= i < 17:
        prix1 += 1
    else:
        prix2 += 1

prixtotal = float(prix1 * 2 + prix2)

heurelocation = heurefinlocation - heurelocation

print("Vous avez loué votre vélo pendant :",i)
if prix2 != 0:
    print(prix1,"heure(s) au tarif horaire de 1.0 euro ")
if prix1 !=0:
    print(prix2,"heure(s) au tarif horaire de 2.0 euros")
print("Le montant total à payer est de {} euro(s).".format(prixtotal))


        
