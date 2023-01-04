import random

just_price = random.randrange(0, 100,1)

user_price = int(input("Entrer un prix "))
 
if user_price <(200/3):
    print("Pile !")
else:
    print("Face !")
 

    