def factorial(num): 
    if num < 0: 
        print("Une factorielle négative n'existe pas")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

num = int(input("Entrez une valeur ")) 

print("La factorielle de ",num,"est", factorial(num))