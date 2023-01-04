dico = {
    "firstname": "Christopher",
    "name": "ANTONIO",
    "promo": 2022,
    "group": "RT112"
}

print("Votre nom est",dico['name'],"et votre prenom est ",dico['firstname'], "vous faites partie de la promo", dico['promo'], "et votre groupe est",dico ['group'] )


dic = {
    "name": "toto",
    "firstname": "titi",
    "promo": 2022,
    "group": 202
}

print("Les clés du dictionnaire sont :")
for i in dic.keys():
    print(f"-{i}")

print("Les valeurs du dictionnaire sont :")
for i in dic.values():
    print(f"-{i}")

print("Les tuplets du dictionnaire sont :")
for i in dic.items():
    print(f"-{i}")

binome = {
    1: dico,
    2: dic
}

print("Les étudiants formants le binôme sont :")
for i in binome.values():
    print(f"- L'étudiant {i['name']} {i['firstname']} du groupe {i['group']}")