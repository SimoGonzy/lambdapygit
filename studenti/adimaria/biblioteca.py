class Libro:
    def __init__(self, titolo, autore, editore, anno_pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.editore = editore
        self.anno_pubblicazione = anno_pubblicazione
        self.stato = "libero"

    def __str__(self):
        return (f"--- Libro ---\n"
                f"Titolo: {self.titolo}\n"
                f"Autore: {self.autore}\n"
                f"Editore: {self.editore}\n"
                f"Anno: {self.anno_pubblicazione}\n"
                f"Stato: {self.stato}\n"
                f"-------------")

    def cambia_stato(self):
        if self.stato == "libero":
            self.stato = "noleggiato"
        else:
            self.stato = "libero"

    def __add__(self, other):
        if isinstance(other, Libro):
            nuovo_scaffale = Scaffale("New", "Misto")
            nuovo_scaffale.aggiungi_libro(self)
            nuovo_scaffale.aggiungi_libro(other)
            return nuovo_scaffale
        return NotImplemented


class Scaffale:
    def __init__(self, codice_identificativo, sezione_tematica):
        self.codice_identificativo = codice_identificativo
        self.sezione_tematica = sezione_tematica
        self.libri = []

    def aggiungi_libro(self, libro):
        self.libri.append(libro)
        print(f"Libro '{libro.titolo}' aggiunto allo scaffale {self.codice_identificativo}.")

    def rimuovi_libro(self, titolo):
        for libro in self.libri:
            if libro.titolo == titolo:
                self.libri.remove(libro)
                print(f"Libro '{titolo}' rimosso dallo scaffale.")
                return
        print(f"Libro '{titolo}' non trovato.")

    def cerca_libro(self, titolo):
        for libro in self.libri:
            if libro.titolo == titolo:
                return libro
        return None

    def __str__(self):
        s = f"Scaffale: {self.codice_identificativo} ({self.sezione_tematica})\nLibri contenuti:\n"
        for libro in self.libri:
            s += f"- {libro.titolo}\n"
        return s

    def __add__(self, other):
        if isinstance(other, Scaffale):
            nuovo_scaffale = Scaffale(f"{self.codice_identificativo}-{other.codice_identificativo}", "Misto")
            for libro in self.libri:
                nuovo_scaffale.aggiungi_libro(libro)
            for libro in other.libri:
                nuovo_scaffale.aggiungi_libro(libro)
            return nuovo_scaffale
        return NotImplemented

    def __len__(self):
        return len(self.libri)

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __eq__(self, other):
        return len(self) == len(other)

if __name__ == "__main__":
    scaffale1 = Scaffale("S1", "Fantasy")
    libro1 = Libro("1984", "Orwell", "Mondadori", 1949)
    libro1.cambia_stato()
    scaffale1.aggiungi_libro(libro1) 
    print(libro1)