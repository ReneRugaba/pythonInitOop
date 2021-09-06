"""
notion creation dictionnaire
{<cle>:<valeur>} => dictionnaire python
"""

dico = {} # initialisation à vide
dico["chien"] = "meilleur ami de l'homme" #ajout element
print(dico)
dico["chien"] = "meilleur ami des humains"#modification
print(dico)
dico["nombre"] = 13
dico["pays"] = "france"
print(dico)
del dico["pays"] #suppression 1
dico.pop("nombre") #suppression 2
print(dico)
"""
verifier la présence d'une valeur
"""
if "chien" in dico:
    print("trouvé")