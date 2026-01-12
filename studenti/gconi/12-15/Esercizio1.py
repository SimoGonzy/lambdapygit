class Libro:
    def __init__(
        self,
        titolo: str,
        anno_uscità: int,
        stato: bool,
        autore: str,
        editore: str,
    ):
        self.titolo = titolo
        self.anno_uscità = anno_uscità
        self.stato = stato
        self.autore = autore
        self.editore = editore

    def cambia_stato(self):
        if self.stato:
            self.stato = False  # noleggiato
        else:
            self.stato = True  # libero

    def __str__(self) -> str:
        if self.stato:
            return f"Libro : {self.titolo}\nanno : {self.anno_uscità}\nstato : libero\nautore : {self.autore}\neditore : {self.editore}"
        else:
            return f"Libro : {self.titolo}\nanno : {self.anno_uscità}\nstato : preso\nautore : {self.autore}\neditore : {self.editore}"


libro1 = Libro("ciao", 1880, True, "steve", "prova")
print(libro1)
libro1.cambia_stato()
print("\n", libro1)
