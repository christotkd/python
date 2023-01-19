T = input("Entrez une chaîne de caractères : ")
taille = len(T)
print(f"La taille de la chaîne de caractères T est de {taille}.")

voyelles = 'aeiouyAEIOUY'
nb_voyelles = sum(T.count(v) for v in voyelles)
pourcentage = (nb_voyelles/taille)*100
print(f"Le pourcentage de voyelles dans la chaîne de caractères T est de {pourcentage}%.")

sous_chaine = "wagon"
occurrence = T.find(sous_chaine)
if occurrence != -1:
    print(f"La chaîne 'wagon' est une sous-chaîne de T, débutant à l'indice {occurrence}.")
else:
    print("La chaîne 'wagon' n'est pas une sous-chaîne de T.")

occurrences = T.count(sous_chaine)
print(f"La chaîne 'wagon' est présente {occurrences} fois dans T.")
