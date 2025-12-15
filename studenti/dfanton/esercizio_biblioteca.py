"""Sei stato contattato da una biblioteca per sviluppare un software
di gestione della loro collezione di libri.
Ogni volume dovrà essere catalogato dal software con titolo,
autore, editore, anno di pubblicazione e stato (libero/noleggiato)
e raggruppato sotto un certo scaffale caratterizzato da un codice
identificativo e una sezione tematica (es. «Narrativa»,
«Saggistica», «Informatica», ecc.)."""
from __future__ import annotations
class Libro:
    def __init__(self, titolo, autore, editore, anno_di_pubblicazione, is_noleggiato, sezione_tematica, n_scaffale):
        self.titolo=titolo
        self.autore= autore
        self.editore = editore
        self.anno_di_pubblicazione = anno_di_pubblicazione
        self.is_noleggiato = is_noleggiato
        self.sezione_tematica = sezione_tematica
        self.n_scaffale = n_scaffale

    def __str__(self):
        stringa : str = f"""TITOLO: {self.titolo}\nAUTORE: {self.autore}\nANNO DI PUBBLICAZIONE: {self.anno_di_pubblicazione}\nNOLEGGIATO: 
        {self.is_noleggiato}\n SEZIONE TEMATICA: {self.sezione_tematica}\nNUMERO SCAFFALE: {self.n_scaffale}"""
        return stringa

    def toggle_noleggio(self):
        if self.is_noleggiato:
            self.is_noleggiato = False
        else:
            self.is_noleggiato = True

    def __add__(self, libro2 : Libro):
        sezione_tematica : str = self.sezione_tematica + " " + libro2.sezione_tematica
        n_scaffale = str(self.n_scaffale) + str(libro2.n_scaffale)
        scaffale : Scaffale = Scaffale(n_scaffale, sezione_tematica, [self, libro2])
        return scaffale

"""Gli scaffali dovranno consentire di memorizzare al loro interno più
libri, per cui:
• Trovare una rappresentazione adatta a descrivere uno scaffale
(codice identificativo, sezione tematica, lista di libri);
• Creare metodi che permettano di aggiungere e rimuovere dei
libri;
• Creare un metodo che permetta di cercare un libro per titolo
all’interno dello scaffale."""
class Scaffale:
    def __init__(self, codice_id, sezione_tematica, lista_libri : list):
        self.codice_id = codice_id
        self.sezione_tematica = sezione_tematica
        self.lista_libri= lista_libri
    def aggiungi_libro(self, libro : Libro):
        self.lista_libri.append(Libro)
    def rimuovi_libro(self, tit: str):
        for libro in self.lista_libri:
            if libro.titolo == tit:
                self.lista_libri.remove(libro)
                print("Libro rimosso con successo")
    def cerca_by_titolo(self, tit: str):
        for libro in self.lista_libri:
            if libro.titolo == tit:
                return libro
                print(libro.__str__())

    def __str__(self):
        string : str = f"""CODICE IDENTIFICATIVO DELLO SCAFFALE:{self.codice_id}\n
                            SEZIONE TEMATICA:{self.sezione_tematica}\n
                            LIBRI:"""
        for libro in self.lista_libri:
            string += str(libro)
        return string
    
    def __add__(self,scaff: Scaffale): 
        unione_libri : list[Libro] = []
        unione_libri.extend(self.lista_libri)
        unione_libri.extend(scaff.lista_libri)
        cod_id = str(self.codice_id) + str(scaff.codice_id)
        sez_tem : str= str(self.sezione_tematica) + " " + str(scaff.sezione_tematica)
        unione_scaffali = Scaffale(cod_id, sez_tem, unione_libri)
        return unione_scaffali
    
    def __len__(self):
        return len(self.lista_libri)

    def __eq__(self, scaffale : Scaffale):
        return len(self.lista_libri) == len(scaffale.lista_libri)
    
    def __lt__(self, scaffale : Scaffale):
        return len(self.lista_libri) < len(scaffale.lista_libri)
    def __gt__(self, scaffale : Scaffale):
        return len(self.lista_libri) > len(scaffale.lista_libri)
    
    # --- Generazione Libri ---

# FANTASY (Scaffale 1)
l1 = Libro("Harry Potter e la Pietra Filosofale", "J.K. Rowling", "Salani", 1997, True, "Fantasy", 1)
l2 = Libro("Harry Potter e la Camera dei Segreti", "J.K. Rowling", "Salani", 1998, False, "Fantasy", 1)
l3 = Libro("Il Signore degli Anelli: La Compagnia", "J.R.R. Tolkien", "Bompiani", 1954, True, "Fantasy", 1)
l4 = Libro("Lo Hobbit", "J.R.R. Tolkien", "Adelphi", 1937, False, "Fantasy", 1)
l5 = Libro("Il Trono di Spade", "G.R.R. Martin", "Mondadori", 1996, False, "Fantasy", 1)

# SCI-FI (Scaffale 1)
l6 = Libro("Dune", "Frank Herbert", "Fanucci", 1965, True, "Sci-Fi", 1)
l7 = Libro("Io, Robot", "Isaac Asimov", "Mondadori", 1950, False, "Sci-Fi", 1)
l8 = Libro("Guida Galattica per Autostoppisti", "Douglas Adams", "Mondadori", 1979, True, "Sci-Fi", 1)

# CLASSICI (Scaffale 2)
l9 = Libro("1984", "George Orwell", "Mondadori", 1949, False, "Distopico", 2)
l10 = Libro("Il Grande Gatsby", "F. Scott Fitzgerald", "Marsilio", 1925, True, "Classico", 2)
l11 = Libro("Orgoglio e Pregiudizio", "Jane Austen", "Einaudi", 1813, False, "Classico", 2)
l12 = Libro("I Promessi Sposi", "Alessandro Manzoni", "Rizzoli", 1827, False, "Classico", 2)
l13 = Libro("Il Processo", "Franz Kafka", "Adelphi", 1925, True, "Classico", 2)

# THRILLER & HORROR (Scaffale 3)
l14 = Libro("It", "Stephen King", "Sperling & Kupfer", 1986, True, "Horror", 3)
l15 = Libro("Shining", "Stephen King", "Bompiani", 1977, False, "Horror", 3)
l16 = Libro("Il Codice Da Vinci", "Dan Brown", "Mondadori", 2003, True, "Thriller", 3)
l17 = Libro("Dieci Piccoli Indiani", "Agatha Christie", "Mondadori", 1939, False, "Giallo", 3)

# SAGGISTICA (Da inserire in Scaffale misto o nuovo)
l18 = Libro("Sapiens. Da animali a dèi", "Yuval Noah Harari", "Bompiani", 2011, True, "Saggistica", 4)
l19 = Libro("Breve storia del tempo", "Stephen Hawking", "Rizzoli", 1988, False, "Scienza", 4)
l20 = Libro("L'arte della guerra", "Sun Tzu", "Newton Compton", -500, False, "Filosofia", 4)

scaffale_fantasy = Scaffale(1, "Fantasy", [l1, l2, l3, l4, l5])
scaffale_scifi = Scaffale(1, "Sci-Fi", [l6, l7, l8])
scaffale_classici = Scaffale(2, "Classici", [l9, l10, l11, l12, l13])
scaffale_thriller_horror = Scaffale(3, "Thriller & Horror", [l14, l15, l16, l17])
scaffale_saggistica = Scaffale(4, "Saggistica", [l18, l19, l20])

#print(scaffale_fantasy)
#print(scaffale_scifi > scaffale_fantasy)
#print(scaffale_classici + scaffale_thriller_horror)
#print(len(scaffale_saggistica))
