def ajouter_elt(lst=[0,1,2], elt= 3):
    lst.append(elt)
    return lst
print(ajouter_elt())

#lorsqu'on ajoute elt, on a la liste qui s'affiche avec le nombre 3

def ajouter_carac(ch= "abc", elt="d"):
   return ch + elt
print(ajouter_carac())
