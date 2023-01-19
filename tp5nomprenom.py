names = []

for i in range(2):
    first_name = input("Entrez votre prenom ")
    last_name = input("Entrez votr nom ")
    names.append((first_name.capitalize(), last_name.upper()))


names.sort()

for first_name, last_name in names:
    print(f"{last_name} {first_name}")
