#L’elemento base della nostra applicazione sarà il libro, per cui:
#• Trovare una rappresentazione adatta a descrivere un libro
#(titolo, autore, editore, anno di pubblicazione, stato);
#• Fare sì che la print di un libro mostri tutte le sue informazioni
#in modo leggibile;
#• Creare un metodo che cambi lo stato del libro da «libero» a
#«noleggiato» e viceversa.

class Libro:

    def __init__(self, titolo, autore, editore, anno):
        
        self.titolo = titolo
        self.autore = autore
        self.editore = editore
        self.anno_pubblicazione = anno
        self.stato = "libero" 

    def __str__(self):
        
        return (f"Titolo: {self.titolo} | Autore: {self.autore} "
                f"| Anno: {self.anno_pubblicazione} | STATO: **{self.stato}**")

    def cambia_stato(self):
        
        if self.stato == "libero":
            self.stato = "noleggiato"
            print(f"-> '{self.titolo}' è ora **noleggiato**.")
        else:
            self.stato = "libero"
            print(f"-> '{self.titolo}' è ora **libero**.")


mio_libro = Libro("Guerra e Pace", "Lev Tolstoj", "Einaudi", 1869)
altro_libro = Libro("Orgoglio e Pregiudizio", "Jane Austen", "Newton", 1813)

print("--- Stato Iniziale ---")
print(mio_libro)
print(altro_libro)

print("\n--- Cambio di Stato ---")

mio_libro.cambia_stato()
altro_libro.cambia_stato()


print("\n--- Stato Finale ---")
print(mio_libro)
print(altro_libro)
