
class Libro:
    def __init__(self, titolo: str, autore: str, editore: Editore, pubblicazione: int, genere: str, disponibile: bool=True) -> None:
        self.titolo = titolo
        self.autore = autore
        self.editore = editore
        self.pubblicazione = pubblicazione
        self.disponibile = disponibile
        self.genere = genere

    def titolo_libro(self):
        return self.titolo

    def mostra_disponibilita(self) -> str:
        return "Disponibile" if self.disponibile else "Noleggiato"

    def cambia_disponibilita(self):
        self.disponibile = not self.disponibile

    def __str__(self) -> str:
        return f"{self.titolo.upper()}\ndi {self.autore}\nCasa editrice: {self.editore} pubblicato nel {self.pubblicazione}\nDisponibile: {self.mostra_disponibilita()}"
    
    def __add__(self, other: Libro):
        nuovo_scaffale = Scaffale()
        nuovo_scaffale.aggiungi_libro(self)
        nuovo_scaffale.aggiungi_libro(other)
        Scaffale.lista_scaffali.append(nuovo_scaffale)

class Scaffale:
    lista_scaffali: list[Scaffale] = []
    def __init__(self) -> None:
        self.codice = len(Scaffale.lista_scaffali)
        self.lista_libri: list[Libro] = []
        Scaffale.lista_scaffali.append(self)

    def aggiungi_libro(self, libro: Libro):
        if not self.lista_libri:
            self.tema = libro.genere
        self.lista_libri.append(libro)

    def cerca_libro_nome(self, libro_nome: str):
        for libro in self.lista_libri:
            if libro.titolo_libro().lower() == libro_nome.lower():
                return libro
        return None

    def rimuovi_libro(self, libro_da_rimuovere: Libro):
        for libro in self.lista_libri:
            if libro.titolo_libro() == libro_da_rimuovere:
                self.lista_libri.remove(libro)
                break
    
    def __add__(self, other: Scaffale) -> None:
        for libro in other.lista_libri:
            self.lista_libri.append(libro)
        Scaffale.lista_scaffali.remove(other)
    
    def __len__(self) -> int:
        return len(self.lista_libri)
    
    def __ge__(self, value: Scaffale) -> bool:
        return len(self) >= len(value)

    def __gt__(self, value: Scaffale) -> bool:
        return len(self) > len(value)
    
    def __le__(self, value: Scaffale) -> bool:
        return len(self) <= len(value)

    def __lt__(self, value: Scaffale) -> bool:
        return len(self) < len(value)
    
    def __eq__(self, value: object) -> bool:
        return type(value) is Scaffale and len(self) == len(value)

    def __str__(self) -> str:
        lista_libri: str = ""
        if len(self.lista_libri):
            print(f"{self.codice} Lo scaffale: {self.tema} contiene {len(self.lista_libri)} libri")
            for libro in self.lista_libri:
                lista_libri += "\n" + str(libro) + "\n"
        else:
            lista_libri = f"Lo scaffale {self.codice} è vuoto!"
        return lista_libri

class Editore:
    def __init__(self, nome) -> None:
        self.nome = nome
    def __str__(self) -> str:
        return self.nome
    
mondadori = Editore("Mondadori")
feltrinelli = Editore("Feltrinelli")
bompiani = Editore("Bompiani")
scaffale1, scaffale2, scaffale3, scaffale4, scaffale5 = Scaffale(), Scaffale(), Scaffale(), Scaffale(), Scaffale()
scaffale1.aggiungi_libro(Libro("Cent'anni di solitudine", "Gabriel Garcia Marquez", mondadori, 1967, "Romanzo storico"))
scaffale2.aggiungi_libro(Libro("1984", "George Orwell", mondadori, 1949, "Fantascienza sociale"))
scaffale1.aggiungi_libro(Libro("I promessi sposi", "Alessandro Manzoni", mondadori, 1827, "Romanzo storico"))
scaffale3.aggiungi_libro(Libro("Il ritratto di Dorian Grey", "Oscar Wilde", mondadori, 1890, "Filosofico"))
scaffale4.aggiungi_libro(Libro("Orgoglio e pregiudizio", "Jane Austen", feltrinelli, 1813, "Romantico"))
scaffale1.aggiungi_libro(Libro("Il Gattopardo", "Giuseppe Tomasi", feltrinelli, 1958, "Romanzo storico"))
scaffale5.aggiungi_libro(Libro("Il nome della rosa", "Umberto Eco", bompiani, 1980, "Giallo storico"))
