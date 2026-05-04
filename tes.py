import random
print("Pierre Feuille Ciseaux")
choix_joueur = input("Choisis pierre, feuille ou ciseaux : ").lower()
choix_ordi = random.choice(["pierre", "feuille", "ciseaux"])
print("L'ordinateur a choisi :", choix_ordi)
if choix_joueur == choix_ordi:
    print("Égalité !")
elif (choix_joueur == "pierre" and choix_ordi == "ciseaux") or \
     (choix_joueur == "feuille" and choix_ordi == "pierre") or \
     (choix_joueur == "ciseaux" and choix_ordi == "feuille"):
    print("Tu as gagné ! ")
elif choix_joueur in ["pierre", "feuille", "ciseaux"]:
    print("Tu as perdu ! ")
else:
    print("Erreur : tu n'as pas écrit pierre, feuille ou ciseaux")

