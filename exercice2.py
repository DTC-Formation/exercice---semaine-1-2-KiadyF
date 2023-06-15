# Créez une variable phrase contenant une phrase de votre choix.
# Vérifiez si la phrase contient le mot "Python" en utilisant une condition if. Affichez un message approprié en fonction du résultat.

phrase = "Actuellement, je suis la formation Python à DTC"

if phrase.rfind("Python") != -1:
    print("Oui, la phrase contient le mot Python")
else:
    print("Non, la phrase ne contient pas le mot Python")
