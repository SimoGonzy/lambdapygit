from datetime import datetime
from termios import ALTWERASE


class Libro:
    def __init__(self, titolo: str, autore:str, pubblicazione: int) -> None:
        self.titolo: str = titolo
        self.autore: str = autore
        self.pubblicazione: int = pubblicazione

    def anni_libro(self) -> int:
        return datetime.now().year - self.pubblicazione

    def __str__(self) -> str:
        return f"Il libro {self.titolo} dell'autore {self.autore} è stato pubblicato nell'anno {self.pubblicazione}"
    
libro = Libro("1984", "George Orwell", 1948)

print(libro.anni_libro())
print(libro)

class Misura:
    def __init__(self, metri: int) -> None:
        self.metri = metri
    def in_chilometri(self) -> float:
        return self.metri / 1000
    def in_metri(self) -> int:
        return self.metri
    
def area_stanza(base: Misura, altezza: Misura) -> int:
    return base.in_metri() * altezza.in_metri()

print(area_stanza(Misura(5), Misura(4)))

def distanza_tempo_viaggio(distanza: Misura) -> float:
    velocita = 130 # km/h
    return distanza.in_chilometri() / velocita

print(distanza_tempo_viaggio(Misura(55_000)))