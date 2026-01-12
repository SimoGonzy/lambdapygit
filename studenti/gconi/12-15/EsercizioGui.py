libro1 = {"titolo": "1984", "autore": "George Orwell", "pubblicazione": 1948}


def anni_libro(libro: dict) -> int:
    return 2025 - libro["pubblicazione"]


print(anni_libro(libro1))


class Libro:
    def __init__(self, titolo: str, pubblicazione: int = 2025):
        self.titolo: str = titolo
        self.pubblicazione: int = pubblicazione

    def calcola_eta(self) -> int:
        return 2025 - self.pubblicazione

    def __str__(self) -> str:
        return f"{self.titolo} pubblicato nel {self.pubblicazione}"


def anni_libro_2(libro: Libro):
    return 2025 - libro.pubblicazione


libro = Libro("1984", 1948)

print(anni_libro_2(libro))
print(libro.calcola_eta())
print(libro)


class Misura:
    def __init__(self, metri: int):
        self.metri = metri

    def in_chilometri(self):
        return self.metri / 1000

    def in_metri(self):
        return self.metri


def area_stanza(base: Misura, altezza: Misura) -> int:
    return base.in_metri() * altezza.in_metri()


def calcola_tempo_viaggio(distanza: Misura) -> float:
    distanza_km = distanza.in_chilometri()
    velocità = 130  # km/h
    return distanza_km / velocità


vrsud_valdagno = calcola_tempo_viaggio(Misura(55_000))  # i _ nei numeri sono ignorati
print(vrsud_valdagno)
