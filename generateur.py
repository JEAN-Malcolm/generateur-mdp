import random
import string
print("=== GENERATEUR DE MOTS DE PASSES POUR ENTRER DANS LE SYSTEME DE DUBAÏ V2 ===")
longueur = int(input("quelle longueur veux-tu pour ton mot de passe : "))
quantite = int(input("combien de mots de passes veux-tu que je genere pour toi : "))
avec_symbole = input("veux-tu des symbole de ce genre !@#$... pour ton ou tes mots de passes ? oui/non : ")
if avec_symbole == "oui":
    caracteres = string.ascii_letters + string.digits + "!@#§$%^&*"
else:
    caracteres = string.ascii_letters + string.digits
for i in range(quantite):
    mdp = ""
    compteur = 0
    while compteur < longueur:
        mdp = mdp + random.choice(caracteres)
        compteur = compteur + 1
    print(f"MOT DE PASSE NUMERO {i+1} : {mdp}")
