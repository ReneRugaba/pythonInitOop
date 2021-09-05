
class Vehicule:
    def __init__(self):
        self._nom= None
        self._marque= None

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def setNom(self,value):
        self._nom = value

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def setMarque(self, value):
        self._marque = value


class Voiture(Vehicule):
    def __init__(self):
        self._type = None

    @property
    def type(self):
        return self._type

    @type.setter
    def setType(self, value):
        self._type = value

voiture = Voiture()
voiture.setNom = "testNom"
voiture.setMarque = "testMarque"
voiture.setType = "testType"

print("voiture de type {}, de marque {} et de nom {}".format(voiture.type, voiture.marque, voiture.nom))
