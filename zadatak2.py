class BankovniRacun:
    def __init__(self, broj_racuna, vlasnik, stanje=0):
        self.broj_racuna = broj_racuna
        self.vlasnik = vlasnik
        self.stanje = stanje
    def uplatiti(self, iznos):
        if iznos > 0:
            self.stanje += iznos
            print(f'Uplata od {iznos} je uspjela. Novo stanje: {self.stanje}')
        else:
            print('Iznos uplate mora biti pozitivan.')
    def isplatiti(self, iznos):
        if 0 < iznos <= self.stanje:
            self.stanje -= iznos
            print(f'Isplata od {iznos} je uspjela. Novo stanje: {self.stanje}')
        else:
            print('Nedovoljno sredstava ili neispravan iznos isplate.')
    def prikaz_stanja(self):
        print(f'Stanje na računu {self.broj_racuna} vlasnika {self.vlasnik} je {self.stanje}.')

if __name__ == "__main__":
    racun = BankovniRacun('HR52152215125', 'Mark Perković', 67000)
    racun.prikaz_stanja()
    racun.uplatiti(10000)
    racun.isplatiti(2321)
    racun.isplatiti(1224212)
    racun.prikaz_stanja()