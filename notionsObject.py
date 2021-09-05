# comprendre les notions object en python
"""
help(str) => permet de voir la class str et ses methodes
"""
machaine = "masuper chaine"
print(machaine.find("ma")) # donne index de départ de la chaine de carractère
print(machaine.upper()) # met toute les lettre en majiscule
print(machaine.lower()) # met en miniscule
print(machaine.capitalize()) # met la premier lettre en majiscule
print(machaine.title()) # met majiscule en debut de chaque mot
print(machaine.center(50, '-')) # centre selon la width
machaine = "              masuper chaine             "
print(machaine.strip()) #enleve les espaces avant et à la fin de la chaine de caractère
print(machaine.replace("a","A")) # remplace les occurrences
machaine = "masuper chaine"
print(machaine.split(" "))