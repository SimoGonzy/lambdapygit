# CLASSE LIBRO (Ripresa dal Livello 1)
class Libro:
    def __init__(self, titolo, autore, editore, anno):
        self.titolo = titolo
        self.autore = autore
        self.editore = editore
        self.anno = anno
        self.stato = "libero"  # Default

    def __str__(self):
        return (f"   [L] Titolo: {self.titolo}, Autore: {self.autore}, Stato: {self.stato.upper()}")
    
    # Metodo per cambiare lo stato (semplificato)
    def cambia_stato(self):
        if self.stato == "libero":
            self.stato = "noleggiato"
        else:
            self.stato = "libero"
           
# ----------------------------------------------------------------------

# CLASSE SCAFFALE (Livello 2)
class Scaffale:
    def __init__(self, codice, sezione):
        """
        Costruttore della classe Scaffale.
        Inizializza il codice, la sezione e una lista vuota per i libri.
        """
        self.codice = codice
        self.sezione = sezione
        self.lista_libri = [] # Qui verranno memorizzati gli oggetti Libro

    def __str__(self):
        """
        Mostra le informazioni dello scaffale e i libri che contiene.
        """
        libri_presenti = len(self.lista_libri)
        output = f"SCAFFALE {self.codice} - SEZIONE: **{self.sezione.upper()}**\n"
        output += f"  (Contiene {libri_presenti} libri.)\n"
        
        if libri_presenti > 0:
            for libro in self.lista_libri:
                output += str(libro) + "\n"
        else:
             output += "  Nessun libro presente su questo scaffale.\n"
        return output

    # ---------------------------------------------
    # Metodi di Gestione Libri
    # ---------------------------------------------

    def aggiungi_libro(self, libro_oggetto):
        """
        Aggiunge un oggetto Libro alla lista.
        """
        self.lista_libri.append(libro_oggetto)
        print(f"Libro '{libro_oggetto.titolo}' aggiunto allo Scaffale {self.codice} ({self.sezione}).")

    def rimuovi_libro(self, titolo_da_rimuovere):
        """
        Rimuove un libro cercandolo per titolo.
        """
        # Usiamo il metodo cerca_libro per trovare l'oggetto
        libro_trovato = self.cerca_libro(titolo_da_rimuovere)
        
        if libro_trovato:
            self.lista_libri.remove(libro_trovato)
            print(f"Libro '{titolo_da_rimuovere}' rimosso con successo dallo scaffale.")
            return True
        else:
            print(f"Errore: Libro '{titolo_da_rimuovere}' non trovato sullo scaffale {self.codice}.")
            return False

    def cerca_libro(self, titolo_cercato):
        """
        Cerca un libro per titolo all'interno della lista dello scaffale.
        Restituisce l'oggetto Libro se trovato, altrimenti None.
        """
        for libro in self.lista_libri:
            if libro.titolo.lower() == titolo_cercato.lower():
                return libro # Restituisce l'OGGETTO Libro trovato
        return None


# 1. Creiamo alcuni oggetti Libro
l1 = Libro("Introduzione a Python", "Guido V. R.", "Tech Edizioni", 2022)
l2 = Libro("Guerra Digitale", "K. Smith", "Editore X", 2023)
l3 = Libro("Il Mago di Oz", "L. Frank Baum", "Classici", 1900)

# 2. Creiamo un oggetto Scaffale per la sezione Informatica
scaffale_info = Scaffale("S001", "Informatica")
print(scaffale_info)
print("---")

# 3. Aggiungiamo i libri allo scaffale
scaffale_info.aggiungi_libro(l1)
scaffale_info.aggiungi_libro(l2)
# Lasciamo l3 fuori per ora

print("\n--- STATO SCAFFALE AGGIORNATO ---")
print(scaffale_info)
print("---")

# 4. Cerchiamo un libro per titolo (Requisito: cerca_libro)
titolo_da_cercare = "guerra digitale"
risultato_ricerca = scaffale_info.cerca_libro(titolo_da_cercare)

if risultato_ricerca:
    print(f"Trovato: {risultato_ricerca.titolo}!")
    # Possiamo ora interagire con l'oggetto trovato, ad esempio cambiarne lo stato
    risultato_ricerca.cambia_stato()
    print(f"Nuovo stato di '{risultato_ricerca.titolo}': {risultato_ricerca.stato.upper()}")
else:
    print(f"Il libro '{titolo_da_cercare}' non è stato trovato.")

print("\n--- RIMOZIONE LIBRO (Requisito: rimuovi) ---")
scaffale_info.rimuovi_libro("Introduzione a Python")
scaffale_info.rimuovi_libro("Libro Inesistente") # Test errore

print("\n--- STATO FINALE DELLO SCAFFALE ---")
print(scaffale_info)


        