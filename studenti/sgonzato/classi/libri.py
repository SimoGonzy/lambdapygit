def anni_libro(libro: dict) -> int:
    return 2025 - libro["anno_pubblicazione"]

libro = {
    "titolo": "1984",
    "autore": "George Orwell",
    "anno_pubblicazione": 1948
}

print(anni_libro(libro))

class Libro:
    def __init__(self, titolo: str, pubblicazione: int):
        self.titolo: str = titolo
        self.pubblicazione: int = pubblicazione
        
    def calcola_eta(self) -> int:
        return 2025 - self.pubblicazione
    
    def __str__(self) -> str:
        return f'${self.titolo} pubblicato nel {self.pubblicazione}'

libro = Libro("1984", 1948)

anno = 1984
print(libro.calcola_eta())
print(libro)