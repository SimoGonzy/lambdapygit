from __future__ import annotations

class Libro:
    def __init__ (self, titolo: str, anno_uscita: int, autore: str, stato: bool, editore: str):
        self.titolo = titolo
        self.anno_uscita = anno_uscita
        self.stato = stato
        self.autore = autore
        self.editore = editore
        
    def cambia_stato (self):
        if (self.stato):
            self.stato = False  #noleggiato
        else:
            self.stato = True   #libero
            
    def __add__(self, other: Libro) -> Scaffale:
        a = Scaffale(Scaffale.num, "")
        a.aggiungi_libro(self)
        a.aggiungi_libro(other)
        return a
    
    def __str__(self) -> str:
        if (self.stato):
            return f"Libro: {self.titolo}\nAnno: {self.anno_uscita}\nAutore: {self.autore}\nStato: Libero\nEditore: {self.editore}"
        else:
            return f"Libro: {self.titolo}\nAnno: {self.anno_uscita}\nAutore: {self.autore}\nStato: Noleggiato\nEditore: {self.editore}"        
         
libro1 = Libro("Ciao", 2025, "Coni", True, "Steve")
libro2 = Libro("Jack", 2000, "Sbronz", False, "Hud")
         
class Scaffale:
    num: int = 1
    
    def __init__ (self, id: int, tema: str = ""):
        self.id = id
        self.tema = tema
        self.lista_libri: list[Libro] = []
        Scaffale.num += 1
        
    def aggiungi_libro (self, libro: Libro):
        self.lista_libri.append(libro)
        return f"{libro.titolo} aggiunto alla lista!"
    
    def rimuovi_libro (self, libro: Libro):
        self.lista_libri.remove(libro)
        return f"{libro.titolo} rimosso dalla lista!"
    
    def cerca_libro (self, titolo: str):
        return list(filter(lambda libro: libro.titolo == titolo, self.lista_libri))[0]
    
    def __add__ (self, other: Scaffale) -> Scaffale:
        a = Scaffale(Scaffale.num)
        for i in range(len(self.listaLibri())):
            a.aggiungi_libro(self.listaLibri()[i])
        for i in range(len(other.listaLibri())):
            a.aggiungi_libro(other.listaLibri()[i])
        return a    
        
    def listaLibri(self) -> list:
        return self.lista_libri
    
    def len_scaffale(self) -> int:
        return len(self.listaLibri())
    
    def __eq__ (self, other: object) -> bool:
        return type(other) is Scaffale and self.listaLibri() == other.listaLibri()
    
    def __str__(self) -> str:
        a = list(map(str, self.lista_libri))
        output = f"Id scaffale: {self.id}\nTematica: {self.tema}\nLista libri: \n["
        
        for i in range(len(a)):
            output += "\n--\n" + a[i]
        output += "\n]"
        return output
        

scaffale1 = Scaffale(100, "Coni")
scaffale1.aggiungi_libro(libro1)
scaffale1.aggiungi_libro(libro2)

scaffale2 = libro1 + libro2

scaffale3 = scaffale1 + scaffale2

print(scaffale3)
print(scaffale3.len_scaffale())
print(scaffale1 == scaffale2)