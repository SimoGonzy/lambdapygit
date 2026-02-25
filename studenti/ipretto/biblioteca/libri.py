class Libro:
    # 1. Definizione della Scheda (Cosa sappiamo)
    def __init__(self, titolo, autore, editore, anno):
        self.titolo = titolo
        self.autore = autore
        self.editore = editore
        self.anno = anno
        self.stato = "libero"  # Inizia sempre da libero

    # 2. Azione: Stampa Scheda
    def __str__(self):
        return (f"Titolo: {self.titolo}, Autore: {self.autore}, Stato: **{self.stato.upper()}**")

    # 3. Azione: Cambia Stato
    def cambia_stato(self):
        if self.stato == "libero":
            self.stato = "noleggiato"
            print(f"'{self.titolo}' è stato noleggiato.")
        else:
            self.stato = "libero"
            print(f"'{self.titolo}' è stato restituito.")

# Esempio pratico:
mio_libro = Libro("Guerra e Pace", "Tolstoy", "Einaudi", 1869)

print("--- STATO INIZIALE ---")
print(mio_libro)

print("\n--- NOLEGGIO IL LIBRO ---")
mio_libro.cambia_stato()
print(mio_libro)

print("\n--- RESTITUISCO IL LIBRO ---")
mio_libro.cambia_stato()
print(mio_libro)