class Nekretnina:
    def __init__(self, adresa, kvadratura, cijena):
        self.adresa = adresa
        self.kvadratura = kvadratura
        self.cijena = cijena
    
    
    def izracunaj_cijenu( self):

        print self.cijena / self.kvadratura
    
    
    def ispisi_informacije(self):
        print(f"Adresa: {self.adresa}")
        print(f"Kvadratura: {self.kvadratura} m2")
        print(f"Cijena: {self.cijena} EUR")

class Stan(Nekretnina):
    def __init__(self, adresa, kvadratura, cijena, kat, lift=False):
        super().__init__(adresa, kvadratura, cijena)
        self.kat = kat
        self.lift = lift
    
    def izracunaj_cijenu(self):   
        print super().izracunaj_cijenu() 
    if self.kat > 3 and not self.lift:
        smanjena_cijena= self.cijena - (self.cijena * 1.05)
    if self.lift:
        povecana_cijena= self.cijena + (self.cijena * 0.05)
    return.cijena
    def ispisi_informacije(self):
        super().ispisi_informacije()
        print(f"Kat: {self.kat}")
        print(f"Lift: {'Da' if self.lift else 'Ne'}")

class Kuca(Nekretnina):
    def __init__(self, adresa, kvadratura,cijena, povrsina_okucnice):
        super().__init__(adresa, kvadratura,cijena)
        self.povrsina_okucnice = povrsina_okucnice

    def izracunaj_cijenu(self):
        cijena = super().izracunaj_cijenu()
        cijena += self.povrsina_okucnice * 100
        return.cijena

    def ispisi_info(self):
        super().ispisi_info()
        print(f"Površina okućnice: {self.povrsina_okucnice} m²")

lista_nekretnina = []
while True:
    print("\n--- IZBORNIK ---")
    print("1. Unos stana")
    print("2. Unos kuće")
    print("3. Ispis svih nekretnina")
    print("4. Prodaja (brisanje) nekretnine")
    print("5. Izlaz")

    if izbor == "1":
        adresa = input("Adresa: ")
        kvadratura = input("Kvadratura (m²): ")
        bazna_cijena = input("Bazna cijena (EUR/m²): ")
        kat = input("Kat: ")
        lift_unos = input("Ima li lift? (da/ne): ").strip().lower()
        ima_lift = lift_unos == "da"

        stan = Stan(adresa, kvadratura, bazna_cijena, kat, ima_lift)
        lista_nekretnina.append(stan)
        print("Stan uspješno dodan!")

    elif izbor == "2":
        adresa = input("Adresa: ")
        kvadratura = input("Kvadratura (m²): ")
        bazna_cijena = input("Bazna cijena (EUR/m²): ")
        povrsina_okucnice = input("Površina okućnice (m²): ")

        kuca = Kuca(adresa, kvadratura, bazna_cijena, povrsina_okucnice)
        lista_nekretnina.append(kuca)
        print("Kuća uspješno dodana!")

    elif izbor == "3":
     def ispisi_nekretnine(nekretnine):
        if not nekretnine:
            print("Nema unesenih nekretnina.")
        for i, nekretnina in enumerate(nekretnine, start=1):
            print(f"\nNekretnina {i}:")
            nekretnina.ispisi_informacije()
            print(f"Cijena po m²: {nekretnina.izracunaj_cijenu()} EUR/m²")
        ispisi_nekretnine(lista_nekretnina)
        ispisi_nekretnine(lista_nekretnina)

    elif izbor == "4":
        if not lista_nekretnina:
            print("Nema unesenih nekretnina za prodaju.")
            
    elif izbor == "5":
        print("Izlaz iz programa.")
        break  
    





        