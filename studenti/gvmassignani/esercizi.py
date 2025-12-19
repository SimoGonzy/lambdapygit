from __future__ import annotations #serve per far leggere tutto il file prima di runnarlo
import random

class Libro:

    def __init__(self, titolo: str, autore: str, editore: str, anno_pubbl: int, stato: bool):
        self.titolo: str = titolo
        self.autore: str = autore
        self.editore: str = editore
        self.anno_pubbl: int = anno_pubbl
        self.stato: bool = stato


    def __str__(self): 
        return f"Il titolo è: {self.titolo}, \nl'autore è: {self.autore}, \nl'editore è: {self.editore}, \nl'anno di pubblicazione è: {self.anno_pubbl}. \nIl libro è {self.stato}"
    
    def noleggio(self, noleggio: bool):
        if (noleggio == True):
            self.stato = True
        else:
            self.stato = False
    
    def __add__(self, altro: Libro) -> Scaffale:
         return Scaffale(codice = random.randint(1000, 9999), sezione = "Patate", lista = (self + altro))
         
         


libro = Libro("Mucca", "Muccaiolo", "Fattore", 2023, True)

libro.noleggio(False)



altra_lista = []
altra_altra_lista = []
altra_altra_altra_lista = []

class Scaffale:

        def __init__(self, codice: str, sezione: str, lista: list[Libro]):
             self.codice: str = codice
             self.sezione: str = sezione
             self.lista: list[Libro] = lista 
             
        def aggiungi_libro(self, libro: Libro):
             self.lista.append(libro)

        def rimuovi_libro(self, libro: Libro):
             self.lista.remove(libro)
             

        def __str__(self):
            lista_libri = ""
            for i in range(len(self.lista)):
                 lista_libri = lista_libri + str(self.lista[i]) + f"\n\n"
                
            return f"Il codice dello scaffale è: {self.codice}, \nla sezione è: {self.sezione}. \nLista dei libri: {lista_libri}"
        
        def cerca_titolo(self):
            richiesta = input("Dimmi il nome del libro che stai cercando: ")
            for i in range(len(self.lista)):
                
                if ((self.lista[i].titolo) == richiesta):
                    return f"Il libro è presente"
            
        def __add__(self, altro: Scaffale) -> Scaffale:
            return Scaffale(codice = random.randint(1000, 9999), sezione = "Altro", lista = self.lista + altro.lista)  
        
        def __len__(self):
             return len(self.lista)
        
        def __gt__(self, altro: Scaffale):
            if (len(self.lista) > len(altro.lista)):
                risultato = True
                print(f"Lo scaffale con più libri è: {self.codice}\n\n")
                return risultato
            elif (len(self.lista) < len(altro.lista)):
                risultato = False
                print(f"Lo scaffale con più libri è: {altro.codice}\n\n") 
                return risultato
            else:
                risultato = False
                print(f"Gli scaffali hanno lo stesso numero di libri\n\n") 
                return risultato
            
            
            
            
                    
               
          
scaffale2 = Scaffale("234fAgb ", "Fantascienza", altra_altra_lista)
scaffale = Scaffale("cfersd", "Narrativa", altra_lista)


libro3 = Libro("fufi", "ninno", "monda", 2020, True)
libro2 = Libro("ciao", "bello", "bimbo", 1421, True)

scaffale.aggiungi_libro(libro)
scaffale.aggiungi_libro(libro2)
scaffale2.aggiungi_libro(libro3) 

scaffale3 = scaffale + scaffale2
risultato = scaffale > scaffale2
n_libri = len(scaffale)
n_libri2 = len(scaffale2)

print(scaffale)
print(scaffale.cerca_titolo())
print(scaffale2)
print(scaffale3)
print(n_libri)




