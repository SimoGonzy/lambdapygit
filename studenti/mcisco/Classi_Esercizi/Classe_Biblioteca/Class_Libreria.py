#Class Libreria
import os
class Libro: 
    #costruttore
    def __init__(self, titolo:str, autore:str, anno_pubblicazione:int, stato:bool):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione
        self.stato = stato
    
    def __str__(self):
        stampa = f"{self.titolo} - {self.autore} - {self.anno_pubblicazione} - "
        if(self.stato):
            stampa += "Disponibile"
        else:
            stampa += "Non disponibile"
        return stampa
    
    def noleggia(self):
        self.stato = False
    
    def __add__(self, altro_libro):
        sezione_tematica = input("Inserisci la sezione tematica: ")
        os.system('clear')
        S = Scaffale(sezione_tematica, [self,altro_libro])
        return S
    
        



class Scaffale:
    C_ID = 0
    def __init__(self, sezione_tematica: str, lista_libri: list[Libro] = []):
        Scaffale.C_ID += 1
        self.ID = Scaffale.C_ID
        self.sezione_tematica = sezione_tematica
        self.lista_libri = lista_libri[:] # : serve per fare una copia

    def aggiuggi_libro(self, libro):
        self.lista_libri.append(libro)
        print(f"Libro aggiunto allo scaffale {self.ID}")
    
    def rimuovi_libro(self, libro):
        self.lista_libri.remove(libro)
        print(f"Libro rimosso dallo scaffale {self.ID}")

    def __str__(self):
        stampa = f"Scaffale {self.ID} - {self.sezione_tematica} :\n"
        for libro in self.lista_libri:
            stampa += f"{libro}\n"
        return stampa
    
    def cerca (self, titolo):
        for libro in self.lista_libri:
            if(libro.titolo == titolo):
                return f"Libro trovato: \n{libro}"
        return "Libro non trovato"
    
    def __add__(self, altro_scaffale):
        sezione_tematica = input("Inserisci la sezione tematica: ")
        os.system('clear')
        l_l = self.lista_libri + altro_scaffale.lista_libri
        S = Scaffale(sezione_tematica, l_l)
        return S
    
    def libri_sullo_scaffale(self):
        return len(self.lista_libri)
    
    def __gt__(self, altro_scafalle):
        return len(self.lista_libri) > len(altro_scafalle.lista_libri)

    def __eq__(self, altro_scafalle: object) -> bool:
        return type(altro_scafalle) is Scaffale and self.libri_sullo_scaffale() == altro_scafalle.libri_sullo_scaffale()

l1 = Libro("Il signore degli anelli", "Tolkien", 1954, True)
l2 = Libro("Harry Potter", "Rowling", 1997, True)
l3 = Libro("1984", "Orwell", 1949, True)

s1 = Scaffale("Fantasy")
s1.aggiuggi_libro(l1)
s1.aggiuggi_libro(l2)

s2 = Scaffale("Drammatico")
s2.aggiuggi_libro(l3)

if(s1 > s2):
    print("s1 ha piu libri")
else:
    print("s2 ha piu libri")


input()
if(s1 == s2):
    print("s1 e rr hanno lo stesso numero di libri")
else:
    print("s1 e rr non hanno lo stesso numero di libri")
