# Créez une liste nombres contenant quelques nombres.
# Utilisez une boucle for pour calculer la somme de tous les nombres de la liste.
# Affichez le résultat de la somme.

nombres = [5,24,65,28,34,21,45,25]
somme = 0

for n in nombres:
    somme += n

print(f"Resultat = {somme}")