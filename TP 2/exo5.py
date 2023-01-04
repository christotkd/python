n = int(input("Entrez un nombre: "))
if (n % 2) == 0 and n > 0:
   print(n,"est Paire et positif")
elif (n % 1) == 0 and n > 0:
    print(n,"est Impaire et positif")
elif (n % 2) == 0 and n < 0:
    print(n,"paire et negatif")
elif (n % 1) == 0 and n < 0:
    print(n,"impaire et negatif")
else:
    print(n,"est nul")


