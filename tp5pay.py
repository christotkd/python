heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))

# Lire le salaire horaire
salaire_horaire = float(input("Entrez le salaire horaire : "))

# Calculer le salaire brut
if heures_travaillees <= 160:
    salaire_brut = heures_travaillees * salaire_horaire
elif heures_travaillees <= 200:
    salaire_brut = 160 * salaire_horaire + (heures_travaillees - 160) * salaire_horaire * 1.25
else:
    salaire_brut = 160 * salaire_horaire + 40 * salaire_horaire * 1.25 + (heures_travaillees - 200) * salaire_horaire * 1.50

# Afficher le salaire brut
print(f"Le salaire brut est de {salaire_brut} euros")