import string
import random


def generer_mot_de_passe(longueur):
    if longueur < 4:
        return None

    tous_les_caracteres = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + string.punctuation
    )

   
    minuscule = random.choice(string.ascii_lowercase)
    majuscule = random.choice(string.ascii_uppercase)
    chiffre = random.choice(string.digits)
    symbole = random.choice(string.punctuation)

  
    reste = ""
    for _ in range(longueur - 4):
        reste += random.choice(tous_les_caracteres)

   
    mot_de_passe_liste = [minuscule, majuscule, chiffre, symbole] + list(reste)

    random.shuffle(mot_de_passe_liste)

    return "".join(mot_de_passe_liste)