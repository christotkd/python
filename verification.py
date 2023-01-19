import os
import datetime

path1 = input("Entrer le nom du 1er fichier : ")
path2 = input("Entrer le nom du 2eme fichier : ")

path = os.path.join(__file__.replace("Verification.py", ""), "tp5-exercice7")
print(path)

full1 = os.path.join(path, path1)
full2 = os.path.join(path, path2)

files = [full1, full2]

for file in files:
    if os.path.isfile(file):
        time = os.path.getmtime(file)
        time = datetime.datetime.fromtimestamp(time)
        print(f"Le fichier {os.path.basename(file)} existe, sa taille est de {os.path.getsize(file)} et sa date de modification est le {time}")

latest_file = max(files, key=os.path.getmtime)
print(f"\nLe fichier le plus récent est {os.path.basename(latest_file)}")