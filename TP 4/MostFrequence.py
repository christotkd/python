
def countX(L1, x):
    count = 0
    for ele in L1:
        if (ele == x):
            count = count + 1
    return count
 
 
L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6, 7]
x = int(input("Entrez un nombre "))
print("Le nombre le plus frequent dans la liste est le :".format(x, countX(L1, x)))