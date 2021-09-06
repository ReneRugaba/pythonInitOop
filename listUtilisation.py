

maliste = [] # pouvant être écrit également ainsi => maliste = List()
maliste.append("teste") # ajoute un element
print(maliste)
maliste2 = ["test2", "test3", "test4", "test5"]
phrase = " ".join(maliste2) #cree une phrase avec element list
print(phrase)
print(maliste2[:]) # affiche toute la liste

if "test3" in maliste2: #chercher occurrence
    print("trouvé")

print(maliste2[2:]) # lire à partir de occurrence
print(maliste2[1:3]) # lire entre deux index list
maliste.extend(maliste2) # ajout des element de la maliste2 dans maliste
# on peut eglement ecrire maliste = maliste + maliste2
print(maliste)
print(maliste.index("test3")) #recuperer index element list
for k,v in enumerate(maliste): # parcourrire list et recuperer valeur et indexe
    print("index: {} => value: {}".format(k,v))


