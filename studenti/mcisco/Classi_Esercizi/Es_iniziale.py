#esercizo_Classi_

class Libro:

    #costruttore della classe Libro
    def __init__(self, titolo: str, pubblicazione: int): 
        self.tittolo: str = titolo
        self.pubblicazione: int = pubblicazione

    def calcola_anno(self, anno_corrente: int) -> int:
        return anno_corrente - self.pubblicazione
    
    #magic methods
    def __str__(self) -> str:
        return f"{self.tittolo} - {self.pubblicazione}"
    

class Misura:
    def __init__(self, metri: float):
        self.metri: float = metri

    def in_km(self) -> float:
        return self.metri / 1000

    def in_m(self) -> int:
        return self.metri
    def area_stanza (base, altezza) -> int:
        return base.in_m() * altezza.in_m()


libro = Libro("Il Signore degli Anelli", 1954) #primo campo -> titolo, secondo campo -> pubblicazione
print(libro.calcola_anno(2025))
print(libro)

input()


misura = Misura(100)
print(misura.in_km())
print(misura.in_m())
print(Misura.area_stanza(misura, misura))




