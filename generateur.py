import string
import random


try:
    longueur = int(input("Longueur du mot de passe : " ))
    if longueur < 4:
        print("La longueur doit être au moins de 4 caractères")
    else:
        print("Tu as choisi : ", longueur)
except ValueError:
   print("La longueur doit être un nombre entier")
tous_les_caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
tous_les_caracteres = random  
reste = ""
for car in range(longueur -4):
    reste +=  random.choice(tous_les_caracteres)

print(len(reste))