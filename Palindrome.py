def check_palindrome(v):
    t = ""
    for c in v:
        if c.isalpha():
             t += c

    reverse = t[::-1]  
  
    if (t == reverse): 
        return True
    return False
  
  
var = input(("Entrez une valeur: "))
if(check_palindrome(var)):
    print("L'entrée est un palindrome")
else:
    print("L'entrée n'est pas un palindrome")