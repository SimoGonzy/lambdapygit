from __future__ import annotations


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

    def __add__(self, other: Libro) -> Scaffale:
        a = Scaffale(Scaffale.num)
        a.aggiungi_libro(self)
        a.aggiungi_libro(other)
        return a


class Scaffale:
    num: int = 1

    def __init__(self, id: int, tema: str = ""):
        self.id = id
        self.tema = tema
        self.lista_libri: list[Libro] = []
        Scaffale.num += 1

    def aggiungi_libro(self, libro: Libro):
        self.lista_libri.append(libro)
        return f"{libro.titolo} aggiunto dallo scaffare!"

    def rimuovi_libro(self, libro: Libro):
        self.lista_libri.remove(libro)
        return f"{libro.titolo} rimosso dallo scaffare!"

    def cerca_libro(self, titolo: str):
        return list(filter(lambda libro: libro.titolo == titolo, self.lista_libri))[0]

    def __str__(self) -> str:
        a = list(map(str, self.lista_libri))
        output = f"id : {self.id}\ntema : {self.tema}\nLibri:["
        for i in range(len(a)):
            output += "\n--\n" + a[i]
        output += "]"
        return output

    def listaLibri(self) -> list:
        return self.lista_libri

    def len(self) -> int:
        return len(self.listaLibri())

    def __add__(self, other: Scaffale) -> Scaffale:
        a = Scaffale(Scaffale.num)
        for i in range(len(self.listaLibri())):
            a.aggiungi_libro(self.listaLibri()[i])
        for i in range(len(other.listaLibri())):
            a.aggiungi_libro(other.listaLibri()[i])
        return a

    def __eq__(self, other: object) -> bool:
        return type(other) is Scaffale and self.listaLibri() == other.listaLibri()


libro1 = Libro("ciao", 1880, True, "steve", "prova")
libro2 = Libro("prova", 1900, True, "caio", "formaggio")
scaffale = Scaffale(1, "prova")
scaffale.aggiungi_libro(libro1)
scaffale.aggiungi_libro(libro2)
# print(scaffale.cerca_libro("ciao"))
# print(scaffale)
b = libro1 + libro2
# print(f"_______\n{b}")
c = scaffale + b
print(c)
print(c.len())

print(scaffale == b)
