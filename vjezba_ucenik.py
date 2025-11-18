# Definicija klase Učenik
class Ucenik:
    """
    Nacrt (klasa) za stvaranje objekata koji predstavljaju učenike.
    Svaki učenik ima ime, prezime, razred i listu ocjena.
    """

    # Konstruktor - posebna metoda koja se poziva pri stvaranju novog objekta
    def __init__(self, ime, prezime, razred):
        """Inicijalizira novi objekt Učenik s početnim podacima."""
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.ocjene = []  # Atribut 'ocjene' se inicijalizira kao prazna lista

    # Metode - funkcije unutar klase koje definiraju što objekt može raditi
    def dodaj_ocjenu(self, ocjena):
        """Dodaje novu ocjenu u listu ocjena učenika."""
        if isinstance(ocjena, int) and 1 <= ocjena <= 5:
            self.ocjene.append(ocjena)
            print(f"INFO: Učeniku {self.ime} {self.prezime} je upisana ocjena {ocjena}.")
        else:
            print(f"GREŠKA: Ocjena '{ocjena}' nije važeća. Molimo unesite broj od 1 do 5.")

    def izracunaj_prosjek(self):
        """Vraća prosjek svih ocjena učenika."""
        # Provjera ako je lista ocjena prazna da se izbjegne dijeljenje s nulom
        if not self.ocjene:
            return 0.0
        else:
            return sum(self.ocjene) / len(self.ocjene)

    def info(self):
        """Ispisuje sve dostupne informacije o učeniku na konzolu."""
        print("-" * 30)
        print(f"Ime i prezime: {self.ime} {self.prezime}")
        print(f"Razred: {self.razred}")
        
        # Ispis ocjena, ili poruka ako nema ocjena
        if self.ocjene:
            print(f"Ocjene: {self.ocjene}")
        else:
            print("Ocjene: (nema upisanih ocjena)")
            
        prosjek = self.izracunaj_prosjek()
        print(f"Prosjek ocjena: {prosjek:.2f}") # Formatiranje na dvije decimale
        print("-" * 30)



# 1. Kreiranje dva objekta (instance) klase Učenik
ucenik1 = Ucenik("Ana", "Anić", "4.b OG")
ucenik2 = Ucenik("Pero", "Perić", "4.c OG")

# 2. Dodavanje ocjena prvom učeniku
ucenik1.dodaj_ocjenu(5)
ucenik1.dodaj_ocjenu(4)
ucenik1.dodaj_ocjenu(5)

# 3. Dodavanje ocjena drugom učeniku
ucenik2.dodaj_ocjenu(3)
ucenik2.dodaj_ocjenu(4)
ucenik2.dodaj_ocjenu(4)

# 4. Pozivanje info metode za oba učenika kako bi se ispisali podaci
print("\n--- Podaci o učenicima ---")
ucenik1.info()
ucenik2.info()