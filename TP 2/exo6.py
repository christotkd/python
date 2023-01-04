from random import randint
 
just_price = randint(1, 100)  
 

running = True
 

while running:
         
    user_price = int(input("Entrer un prix "))
 
    if user_price == just_price:
     print("Trouvé !")
     running = False
 
    elif user_price > 50:
     print("Face")
       

    elif user_price < 50:
     print("Pile")
 

print("Fin du jeu !")
