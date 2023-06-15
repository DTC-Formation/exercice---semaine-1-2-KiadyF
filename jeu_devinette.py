# Générez un nombre aléatoire entre 1 et 100.
# Demandez à l'utilisateur de deviner le nombre.
# Comparez la réponse de l'utilisateur avec le nombre généré.
# Affichez des messages "Trop grand" ou "Trop petit" en fonction de la réponse de l'utilisateur.
# Répétez les étapes 2 à 4 jusqu'à ce que l'utilisateur devine correctement le nombre.

import random

nombre = random.randint(1,100)
la_reponse_est_trouvee = False

while(not la_reponse_est_trouvee):
    reponse = input("Votre reponse: ")
    if reponse.isnumeric():
        if int(reponse) == nombre:
            print("Bien joué, vous avez trouvé le bon nombre.")
            la_reponse_est_trouvee = True
        elif int(reponse) < nombre:
            print("Trop petit")
        else:
            print("Trop grand")
    else:
        print("Il faut entre un nombre.")