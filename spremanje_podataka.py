import csv

# Definicija klase Učenik
class Ucenik:

    def __init__(self, ime, prezime, razred):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.ocjene = [] 


    def dodaj_ocjenu(self, ocjena):
        if isinstance(ocjena, int) and 1 <= ocjena <= 5:
            self.ocjene.append(ocjena)
            print(f"INFO: Učeniku {self.ime} {self.prezime} je upisana ocjena {ocjena}.")
        else:
            print(f"GREŠKA: Ocjena '{ocjena}' nije važeća. Molimo unesite broj od 1 do 5.")


    def izracunaj_prosjek(self):
        if not self.ocjene:
            return 0.0
        
        return sum(self.ocjene) / len(self.ocjene)


    def info(self):
        print("-" * 30)
        print(f"Ime i prezime: {self.ime} {self.prezime}")
        print(f"Razred: {self.razred}")
        
        if self.ocjene:
            print(f"Ocjene: {self.ocjene}")
        else:
            print("Ocjene: (nema upisanih ocjena)")
            
        prosjek = self.izracunaj_prosjek()
        print(f"Prosjek ocjena: {prosjek:.2f}") 
        print("-" * 30)


def ispisi_izbornik():
    print ("-"*50)
    print ("Glavni izbornik")
    print ("-"*50)
    print ("0. Izlaz iz programa")
    print ("1. Unos nove učenice")
    print ("2. Unos ocjena za učenicu")
    print ("3. Ispis podataka o učenici")
    print ("-"*50)


def upisUcenice(ime, prezime, razred):
    ucenik = Ucenik(ime, prezime, razred)
    return ucenik


def upisOcjene(ucenik, ocjena):
    ucenik.dodaj_ocjenu(ocjena)


def ispisPodataka(ucenik):
    ucenik.info()



lista_ucenika = []

try:
    with open("ucenici.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if not row:
                continue  # preskoči prazne redove

            ime = row[0]
            prezime = row[1]
            razred = row[2]

            # Napravi učenika
            ucenik = Ucenik(ime, prezime, razred)

            # Učitaj ocjene ako ih ima
            if len(row) > 3:
                for ocjena in row[3:]:
                    if ocjena.isdigit():
                        ucenik.ocjene.append(int(ocjena))

            lista_ucenika.append(ucenik)

    print("INFO: Učenici su uspješno učitani iz CSV-a.")

except FileNotFoundError:
    print("UPOZORENJE: CSV datoteka nije pronađena. Kreće se s praznom listom učenika.")

provjera = False
while True:
    ispisi_izbornik()
    try:
        izbor = int(input("Unesite izbor (0/1/2/3): "))
        if izbor == 1:
            print ("Unos nove učenice")
            ime = input("Unesite ime učenika: ")
            prezime = input("Unesite prezime učenika: ")
            razred = input("Unesite razred učenika: ")
            ucenik = upisUcenice(ime, prezime, razred)
            lista_ucenika.append(ucenik)
            with open('ucenici.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([ime, prezime, razred])
        elif izbor == 2:
            ime = input("Unesite ime učenika: ")
            for ucenik in lista_ucenika:
                if ucenik.ime == ime:
                    provjera = True
                    break
                else:
                    provjera = False
            if provjera:
                ocjena = int(input("Unesite ocjenu: "))
                upisOcjene(ucenik, ocjena)
                with open('ucenici.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    for row in file:
                        if row == ucenik[:-1] or row == ucenik:
                            writer.writerow(ucenik, [str(ocjena)])
            else:
                print ("Učenik nije pronađen.")
        elif izbor == 3:
            ime = input("Unesite ime učenika: ")
            for ucenik in lista_ucenika:
                if ucenik.ime == ime:
                    ispisPodataka(ucenik)
                    break
                else:
                    print ("Učenik nije pronađen.")
        elif izbor == 0:
            print ("Hvala na korištenju programa.")
            break
        else: 
            print ("Greška")
    except ValueError:
        print ("Molimo unesite ispravan odabir (0/1/2/3).")