class Vozilo:
    
    def __init__(self, marka, model, godina_proizvodnje, cijena):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.cijena = cijena
    
    def info(self):
        return f"Marka: {self.marka}, Model: {self.model}, Godina: {self.godina_proizvodnje}, Cijena: {self.cijena} EUR"
    
    def promijeni_cijenu(self, nova_cijena):
        stara_cijena = self.cijena
        self.cijena = nova_cijena
        print(f"Cijena vozila {self.marka} {self.model} promijenjena iz {stara_cijena} EUR u {nova_cijena} EUR")


class ElektricnoVozilo(Vozilo):
    
    def __init__(self, marka, model, godina_proizvodnje, cijena, domet_baterije):
        super().__init__(marka, model, godina_proizvodnje, cijena)
        self.domet_baterije = domet_baterije
    
    def info(self):
        osnovni_info = super().info()
        return f"{osnovni_info}, Domet: {self.domet_baterije} km"


def ispisi_izbornik():
    print("--------- AUTOSALON v2.0 ----------")
    print("1. Dodaj novo (obično) vozilo")
    print("2. Dodaj novo (električno) vozilo")
    print("3. Ispiši podatke o određenom vozilu")
    print("4. Promijeni cijenu vozilu")
    print("5. Ispiši sva vozila")
    print("0. Izlaz")
    print("-"*35)


def unosVozila():
    print("\n--- Unos običnog vozila ---")
    marka = input("Unesite marku vozila: ")
    model = input("Unesite model vozila: ")


    while True:
        try:
            godina_proizvodnje = int(input("Unesite godinu proizvodnje: "))
            cijena = float(input("Unesite cijenu vozila (EUR): "))
            break
        except ValueError:
            print("Pogrešan unos! Godina mora biti cijeli broj, a cijena broj.")
    
    return Vozilo(marka, model, godina_proizvodnje, cijena)


def unosElVozila():
    """Funkcija za unos podataka o električnom vozilu"""
    print("\n--- Unos električnog vozila ---")
    marka = input("Unesite marku vozila: ")
    model = input("Unesite model vozila: ")
    
    while True:
        try:
            godina_proizvodnje = int(input("Unesite godinu proizvodnje: "))
            cijena = float(input("Unesite cijenu vozila (EUR): "))
            domet_baterije = int(input("Unesite domet baterije (km): "))
            break
        except ValueError:
            print("Pogrešan unos! Svi numerički podaci moraju biti brojevi.")
    
    return ElektricnoVozilo(marka, model, godina_proizvodnje, cijena, domet_baterije)


def pronadji_vozilo(lista_vozila):
    if not lista_vozila:
        print("Evidencija je prazna!")
        return None
    
    marka = input("Unesite marku vozila: ")
    model = input("Unesite model vozila: ")
    

    print(f"Vozilo {marka} {model} nije pronađeno u evidenciji.")
    return None


def main():
    """Glavna funkcija programa"""
    autosalon = []
    
    print("Dobrodošli u sustav evidencije autosalona!")
    
    while True:
        ispisi_izbornik()
        
        try:
            izbor = int(input("Odaberite opciju: "))
        except ValueError:
            print("Pogrešan unos! Molimo unesite broj između 0 i 5.")
            continue
        
        if izbor == 1:
            novo_vozilo = unosVozila()
            autosalon.append(novo_vozilo)
            print(f"Vozilo {novo_vozilo.marka} {novo_vozilo.model} uspješno dodano!")
            
        elif izbor == 2:
            novo_el_vozilo = unosElVozila()
            autosalon.append(novo_el_vozilo)
            print(f"Električno vozilo {novo_el_vozilo.marka} {novo_el_vozilo.model} uspješno dodano!")
            
        elif izbor == 3:
            vozilo = pronadji_vozilo(autosalon)
            if vozilo:
                print("\n--- Podaci o vozilu ---")
                print(vozilo.info())
                
        elif izbor == 4:
            vozilo = pronadji_vozilo(autosalon)
            if vozilo:
                try:
                    nova_cijena = float(input("Unesite novu cijenu vozila (EUR): "))
                    vozilo.promijeni_cijenu(nova_cijena)
                except ValueError:
                    print("Pogrešan unos! Cijena mora biti broj.")
                    
        elif izbor == 5:
            if not autosalon:
                print("Evidencija je prazna!")
            else:
                print(f"\n--- Sva vozila u evidenciji ({len(autosalon)} komada) ---")
                for i, vozilo in enumerate(autosalon, 1):
                    print(f"{i}. {vozilo.info()}")
                    
        elif izbor == 0:
            print("Hvala što ste koristili sustav evidencije autosalona!")
            break
            
        else:
            print("Pogrešan odabir! Molimo odaberite opciju između 0 i 5.")


    

