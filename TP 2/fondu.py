BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400.0

nbConvives = int(input(" Entrez le nombre de convives "))
quantiteDeBase = fromage + eau + ail + pain

nouvelleQuantite = quantiteDeBase * nbConvives / BASE

user = nbConvives / BASE

fromage1 = 800.0 * user
eau1 = 2 * user
ail1 = 2 * user
pain1 = 400.0 * user

print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :"
,fromage1, "gr de fromage",ail1,"gousse(s) d'ail", pain1,"gr de pain")