class Recept():
    def __init__(self, naziv, sastojci,):
        self.naziv = naziv
        self.sastojci = sastojci
        
    def __str__(self):
        return f"{self.naziv}\nSastojci: {', '.join(self.sastojci)}"
class Kuharica():
    def __init__(self):
        self.recepti = []
    def dodaj_recept(self, recept):
        self.recepti.append(recept)
    def prikazi_recepte(self):
        for recept in self.recepti:
            print(recept)
            print("-" * 40)
Moja_kuharica = Kuharica()
recept1 = Recept("Pasta Carbonara", ["pasta", "jaja", "slanina", "parmezan"])
recept2 = Recept("Palačinke", ["brašno", "jaja", "mlijeko", "šećer"])
Moja_kuharica.dodaj_recept(recept1)
Moja_kuharica.dodaj_recept(recept2)

Moja_kuharica.prikazi_recepte()
def pronadji_recept_po_nazivu(self, naziv):
    for recept in self.recepti:
        if recept.naziv.lower() == naziv.lower():
            return recept
    return None