#Definicija klase Knjiga
class Knjiga:
    """
    Nacrt (klasa) za stvaranje objekata koji predstavljaju knjige.
    Svaka Knjiga ima autora, naslov i godinu izdanja.
    """
    # Konstruktor - posebna metoda koja se poziva pri stvaranju novog objekta
    def __init__(self, naslov, autor, godina_izdanja):
        """Inicijalizira novi objekt Učenik s početnim podacima."""
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja= godina_izdanja
    def _str_(self):
        return f"{self.naslov} by {self.autor} ({self.godina_izdanja})"

knjiga1 = Knjiga("Gospodar prstenova", "J.R.R. Tolkien", 1954)
knjiga2 = Knjiga("Posljednji Stipančići", "Vjenceslav Novak", 1899)
#prikaz podataka o knjigama
print(f"Knjiga: {knjiga1.naslov}, Autor: {knjiga1.autor}, Godina izdanja: {knjiga1.godina_izdanja}.")
print(f"Knjiga: {knjiga2.naslov}, Autor: {knjiga2.autor}, Godina izdanja: {knjiga2.godina_izdanja}.")
