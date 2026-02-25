# classi


from types import MethodDescriptorType


class Libro:
    def __init__(self, titolo: str, pubblicazione: int):
        self.titolo: str = titolo
        self.pubblicazione: int = pubblicazione


libro = Libro("1948", 1948)
anno = 1948
print(libro.calcolatrice)
print(anno.calcola_eta())

class Misura:
    def__init__(self,metri: int):
    self.mnetri = metri
    def in_chilometri(self):
        return self.metri/1000
    def in_metri(self):
        return self.metri
    def area


    # rappresentazione per descirvere un libro

class Libro:
    def __init__(self, titolo, autore, editore, anno, stato="libero"): # il self serve per salvare limformazione dentro il libro che sto creando
        self.titolo = titolo
        self.autore = autore
        self.editore = editore
        self.anno = anno
        self.stato = stato

    def __str__(self):
        return (
            f"TITOLO: {self.titolo}\n" # lho |n serve per andare a capo new line
            f"AUTORE: {self.autore}\n"
            f"EDITORE: {self.editore}\n"
            f"ANNO: {self.anno}\n"
            f"STATO: {self.stato}"
        )
    def cambiastato(self): #funzione cha cambia lho stato
        if stato.stato == "libero" :
            self.stato = "noleggiato"
        else:
            self.stato="libero"

class Scaffale:
    def __init__(self, codiceidentificativo, sezionetematica, listalibri):
        self.codiceidentificativo = codiceidentificativo
        self.sezionetematica = sezionetematica
        self.listalibri = listalibri
        self.libri = []
# funzione per aggiungere un libro
    def aggiungilibro(self,libro):
        self.libri.append(libro)
# funzione per rimuvere un libro
    def rimuovilibro(self,libro):
        self.libro.remove(libro)
# funzione per creare un libro all'interno dello scaffale
    def cercalibro(self,libro):
