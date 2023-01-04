from random import randint
 
just_price = randint(1, 100)  
 
running = True
 
while running:
         
    user_price = int(input("Entrer un prix"))
 
    if user_price == just_price:
     print("Trouvé !")
     running = False
 
    elif user_price > just_price:
     print("C'est moins")
       
    elif user_price < just_price:
     print("C'est plus")

print("Fin du jeu !")