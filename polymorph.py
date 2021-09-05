class Vehicule:
    def __init__(self):
        self._nom = None
        self._marque = None

    def get_nom(self):
        return self._nom

    def set_nom(self,nom):
        self._nom = nom

    nom = property(get_nom, set_nom)

    def get_marque(self):
        return self._marque

    def set_marque(self,marque):
        self._marque = marque

    marque = property(get_marque, set_marque)


class Voiture(Vehicule):
    def __init__(self):
        self._type = None

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    type = property(get_type, set_type)


voiture = Voiture()
voiture.nom = "nomVoiture"
voiture.marque = "marqueVoiture"
voiture.type = "typeVoiture"

print("voiture de type {} , de marque {} et de nom {}".format(voiture.type, voiture.marque, voiture.nom))
