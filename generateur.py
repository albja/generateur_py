
from password_generator import generer_mot_de_passe

try:
    longueur = int(input("Longueur du mot de passe : "))

    mot_de_passe = generer_mot_de_passe(longueur)

    if mot_de_passe is None:
        print("La longueur doit être au moins de 4 caractères")
    else:
        print("Mot de passe généré :", mot_de_passe)

except ValueError:
    print("La longueur doit être un nombre entier")