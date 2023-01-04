nMax = 3

v1 = []
v2 = []

n = int(input("Entrez la taille effective des vecteurs: "))

while n < 1 or n > nMax:
  print("La taille doit être comprise entre 1 et", nMax)
  n = int(input("Entrez la taille effective des vecteurs: "))


print("Entrez les composantes du vecteur v1:")
for i in range(n):
  v1.append(int(input(f"v1[{i}] = ")))

print("Entrez les composantes du vecteur v2:")
for i in range(n):
  v2.append(int(input(f"v2[{i}] = ")))

produit_scalaire = 0
for i in range(n):
  produit_scalaire += v1[i] * v2[i]

print("Le produit scalaire de v1 et v2 est", produit_scalaire)