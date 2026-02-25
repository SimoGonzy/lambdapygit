from multiprocessing import Value


class Libro:
    def __init__(
        self,
        titolo: str,
        autore: str,
        editore: str,
        anno_pubblicazione: int,
        disponibile: bool,
    ):
        self.titolo: str = titolo
        self.autore: str = autore
        self.editore: str = editore
        self.anno_pubblicazione: int = anno_pubblicazione
        self.disponibile: bool = disponibile

    def disp(self) -> str:
        if self.disponibile:
            return "disponibile"
        else:
            return "non disponibile"

    def noleggio(self):
        if self.disponibile:
            self.disponibile = False
        else:
            self.disponibile = True

    def __add__(self, other):
        scaffale = Scaffale(codice=15, sezione="Generico")
        scaffale.aggiungi_libro(self)
        scaffale.aggiungi_libro(other)
        return scaffale

    def __str__(self) -> str:
        return f"Il libro {self.titolo} di ({self.autore},{self.editore}, {self.anno_pubblicazione}) è {self.disp()}"


class Scaffale:
    def __init__(self, codice: int, sezione: str):
        self.codice: int = codice
        self.sezione: str = sezione
        self.lista: list[Libro] = []

    def aggiungi_libro(self, libro: Libro):
        self.lista.append(libro)

    def rimuovi_libro(self, libro: Libro):
        try:
            self.lista.remove(libro)
        except ValueError:
            print("LIbro non trovato nella lista. ")

    def ricerca(self):
        return list(filter(lambda x: x.titolo == libro.titolo, self.lista))

    def __str__(self) -> str:
        return (
            f"Lo scaffale del genere {self.sezione} contiene i seguenti libri "
            + ", ".join(list(map(lambda x: x.titolo, self.lista)))
        )

    def __add__(self, other):
        nuovo = Scaffale(
            codice=self.codice + other.codice,
            sezione=f"{self.sezione} + {other.sezione}",
        )

        nuovo.lista = self.lista + other.lista
        return nuovo


libro = Libro("1984", "Orwell", "ciccio", 1948, True)
libro2 = Libro("Il Signore degli Anelli", "Tolkien", "Bompiani", 1954, True)

nuovo_scaffale = libro + libro2
print(nuovo_scaffale)
print(libro)
scaffale1 = Scaffale(1, "Fantascienza")
scaffale2 = Scaffale(2, "Classici")

scaffale1.aggiungi_libro(libro)
scaffale2.aggiungi_libro(libro2)

scaffale3 = scaffale1 + scaffale2
print(scaffale3)

scaffale = Scaffale(123, "Fantasy")
scaffale.aggiungi_libro(libro)
print(scaffale)
scaffale.rimuovi_libro(libro)
print(scaffale)
