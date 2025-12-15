class Libro:
    def __init__(self, titolo, autore, editore, pubblicazione, stato):
        self.titolo = titolo
        self.autore = autore
        self.editore = editore
        self.pubblicazione = pubblicazione
        self.stato = stato

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Editore: {self.editore}, Anno di pubblicazione: {self.pubblicazione}, Stato: {self.stato}"

    def cambia_stato(self):
        if self.stato == "libero":
            self.stato = "noleggiato"
        elif self.stato == "noleggiato":
            self.stato = "libero"

    def __add__(self, libro3):
        return Scaffale(10, f"Storia", [self, libro3])


libro1 = Libro("a", "b", "c", 1999, "noleggiato")
libro2 = Libro("z", "b", "c", 1999, "noleggiato")
libro1.cambia_stato()


class Scaffale:
    def __init__(self, id, sezione_tematica, lista_libri):
        self.id = id
        self.sezione_tematica = sezione_tematica
        self.lista_libri = lista_libri

    def aggiungi_libro(self, libro):
        self.lista_libri.append(libro)

    def rimuovi_libro(self, libro):
        self.lista_libri.remove(libro)

    def cerca_libro(self, libro):
        if libro in self.lista_libri:
            print(f"\n{libro}")
        else:
            print("Libro non trovato.\n")

    def __str__(self):

        a = f"Id: {self.id}, Sezione tematica: {self.sezione_tematica}, Libri: "
        for libro in self.lista_libri:
            a += f"\n {str(libro)}"
        return a

    def __add__(self, scaffale):
        return Scaffale(
            self.id + scaffale.id,
            self.sezione_tematica[: len(self.sezione_tematica) // 2]
            + scaffale.sezione_tematica[len(scaffale.sezione_tematica) // 2 :],
            self.lista_libri + scaffale.lista_libri,
        )

    def __len__(self):
        return len(self.lista_libri)

    def __eq__(self, scaffale):
        return len(self.lista_libri) == len(scaffale.lista_libri)


scaffale1 = Scaffale(10, "Storia", [libro1, libro2])
scaffale2 = Scaffale(12, "Religione", [libro1, libro2])
# print(scaffale1)
scaffale3 = scaffale1 + scaffale2
"""print(scaffale3)
print(f"Numero libri: {len(scaffale3)}")
print(scaffale1 == scaffale2)"""

while True:
    print("\nDigita un numero per effettuare un operazione sulla libreria:")
    print(
        "1. Mostra gli scaffali.\n2. Aggiungi un libro ad uno scaffale.\n3. Rimuovi un libro da uno scaffale.\n4. Mostra un libro in uno scaffale.\n0. Exit"
    )
    r = eval(input("\n> "))
    if r == 1:
        print(f"s1: {scaffale1}, \ns2: {scaffale2}, \ns3: {scaffale3}")
        print("\n-----------------------\n")

    elif r == 2:
        s = input("Inserisci lo scaffale (s1, s2, s3): ")
        l = input("Inserisci il libro da aggiungere (l1, l2): ")
        if s == "s1":
            if l == "l1":
                scaffale1.aggiungi_libro(libro1)
            elif l == "l2":
                scaffale1.aggiungi_libro(libro2)
        elif s == "s2":
            if l == "l1":
                scaffale2.aggiungi_libro(libro1)
            elif l == "l2":
                scaffale2.aggiungi_libro(libro2)
        elif s == "s3":
            if l == "l1":
                scaffale3.aggiungi_libro(libro1)
            elif l == "l2":
                scaffale3.aggiungi_libro(libro2)
    elif r == 3:
        s = input("Inserisci lo scaffale (s1, s2, s3): ")
        l = input("Inserisci il libro da rimuovere (l1, l2): ")
        if s == "s1":
            if l == "l1":
                scaffale1.rimuovi_libro(libro1)
            elif l == "l2":
                scaffale1.rimuovi_libro(libro2)
        elif s == "s2":
            if l == "l1":
                scaffale2.rimuovi_libro(libro1)
            elif l == "l2":
                scaffale2.rimuovi_libro(libro2)
        elif s == "s3":
            if l == "l1":
                scaffale3.rimuovi_libro(libro1)
            elif l == "l2":
                scaffale3.rimuovi_libro(libro2)
    elif r == 4:
        s = input("Inserisci lo scaffale (s1, s2, s3): ")
        l = input("Inserisci il libro da mostrare (l1, l2): ")
        if s == "s1":
            if l == "l1":
                scaffale1.cerca_libro(libro1)
            elif l == "l2":
                scaffale1.cerca_libro(libro2)
        elif s == "s2":
            if l == "l1":
                scaffale2.cerca_libro(libro1)
            elif l == "l2":
                scaffale2.cerca_libro(libro2)
        elif s == "s3":
            if l == "l1":
                scaffale3.cerca_libro(libro1)
            elif l == "l2":
                scaffale3.cerca_libro(libro2)
    elif r == 0:
        break
