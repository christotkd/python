
somme = int(input("Entrez une somme d'argent en euros : "))

nb_billets_100 = somme // 100
somme = somme % 100

nb_billets_50 = somme // 50
somme = somme % 50

nb_billets_10 = somme // 10
somme = somme % 10

nb_pieces_2 = somme // 2
somme = somme % 2

nb_pieces_1 = somme

print(f"{somme} euros, c'est donc {nb_billets_100} billets de 100, {nb_billets_50} de 50, {nb_billets_10} de 10, {nb_pieces_2} pièces de 2 et {nb_pieces_1} pièce 1.")
