# Créez une liste nombres contenant les nombres de 1 à 10.
# Utilisez une boucle for pour afficher uniquement les nombres pairs de la liste.

nombres = range(1,11)
for n in nombres:
    if n%2 == 0:
        print(n)