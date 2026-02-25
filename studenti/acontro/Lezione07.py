class Libro:
    def __init__(
        self,
        titolo: str,
        autore: str,
        editore: str,
        anno_pubblicazione: int,
        disponibilità: bool,
    ):
        self.titolo: str = titolo
        self.autore: str = autore
        self.editore: str = editore
        self.anno_pubblicazione: int = anno_pubblicazione
        self.disponibilità: bool = disponibilità

    def disponibile(self) -> str:
        if self.disponibilità:
            return "disponibile"
        else:
            return "non disponibile"

    def noleggio(self):
        if self.disponibilità:
            self.disponibilità = False
        else:
            self.disponibilità = True

    def __add__(self, other):
        scaffale = Scaffale(codice=0, sezione="Generale")
        scaffale.aggiungi_libro(self)
        scaffale.aggiungi_libro(other)
        return scaffale

    def __str__(self) -> str:
        return f"Il libro {self.titolo} ({self.autore}, {self.editore}, {self.anno_pubblicazione}) è {self.disponibile()}"


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
            print("Libro non trovato nella lista.")

    def ricerca(self, libro: Libro):
        return list(filter(lambda x: x.titolo == libro.titolo, self.lista))

    def __add__(self, other):
        nuovo = Scaffale(
            codice=self.codice + other.codice,
            sezione=f"{self.selezione} + {other.selezione}",
        )
        nuovo.lista = self.lista + other.lista
        return nuovo

    def __str__(self) -> str:
        return (
            f"Lo scaffale del genere {self.sezione} contiene i seguenti libri: "
            + ", ".join(list(map(lambda x: x.titolo, self.lista)))
        )


libro = Libro("1984", "Orwell", "ciao", 1948, True)
libro1 = Libro("1", "1", "1", 2015, True)

print(libro)

scaffale = Scaffale(123, "Fantasy")
scaffale.aggiungi_libro(libro)
scaffale1 = Scaffale(456, "bello")
scaffale1.aggiungi_libro(libro1)
print(scaffale, scaffale1)
scaffale2 = scaffale + scaffale1
print(scaffale2)
