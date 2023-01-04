
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0

notes = []

for i in range(nombreEtudiants):
    note = float(input("Donnez la note de l'étudiant {} : ".format(i+1)))
    while note < 0 or note > 20:
        print("La note doit être comprise entre 0 et 20. Veuillez réessayer.")
        note = float(input("Donnez la note de l'étudiant {} : ".format(i+1)))
    notes.append(note)
    moyenne += note

moyenne /= nombreEtudiants


for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print("L'étudiant {} a un écart de {} par rapport à la moyenne de classe.".format(i+1, ecart))