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


# --- Glavni dio programa ---
# Ovdje testiramo našu klasu
def ispisi_izbornik():
    print("-"*50)
    print("glavni izbornik")
    print("-"*50)
    print("0. izlaz iz programa")
    print("1. unos nove učenice")
    print("2. unos ocjena za učenicu")
    print("3. ispis podataka o učenici")
    print("-"*50)
    def upisUcenice(ime, prezime, razred):
        ucenik=Ucenik (ime, prezime, razred)
        return ucenik
    
    def upisOcjene (ucenik, ocjena):
        ucenik.dodaj_ocjenu(ocjena)

    def ispisPodataka(ucenik):
        ucenik.info()
    
# --- Glavni dio programa ---

lista_ucenika=[]

while True:
    ispisi_izbornik()
    try:
        izbor=int (input("unesite izbor (0/1/2/3):"))
        if izbor ==1:
            print("unos nove učenice")
            ime=input("unestie ime učenika:")
            prezime=input("unesite prezime učenika:")
            razred=input("unesite razred učenika:")
            ucenik=upisUcenice(ime, prezime, razred)
            ucenik.info()
            lista_ucenika.append(ucenik)
        elif izbor == 2:
            ime=input("unestie ime učenika:")
            for ucenik in lista_ucenika:
                if ucenik.ime== ime:
                    provjera=True
                    break
                else:
                    provjera=False
            if provjera:
                    ocjena=int(input("unesite ocjenu:"))
                upisOcjene(ucenik, ocjena)
            else:
                print("učenik nije pronađen")
        elif izbor == 3:
            ime=input ("unesite ime ucenika")
            for ucenik in lista_ucenika:


        else:
            print("greška")
    except ValueError:
            print("molimo unesite ispravan odabir (0/1/2/3).")

    for ucenik in lista_ucenika:
        ucenik.info()


        




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