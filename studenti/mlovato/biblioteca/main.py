from biblioteca import Libro, Editore, Scaffale

active: bool = True

while active:
    print("Benvenuto nella biblioteca Lambda!")
    print("1 - Aggiungi libro")
    print("2 - Noleggia un libro")
    print("3 - Visualizza tutti gli scaffali")
    print("0 - Esci")
    print()
    scelta: int = int(input("Cosa vuoi fare? "))

    if scelta == 0:
        active = False
    elif scelta == 1:
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        editore = Editore(input("Editore: "))
        pubblicazione = int(input("Anno di pubblicazione: "))
        genere = input("Genere: ")
        nuovo_libro = Libro(titolo, autore, editore, pubblicazione, genere)
        print()
        for scaffale in Scaffale.lista_scaffali:
            if scaffale.tema.lower() == nuovo_libro.genere.lower():
                print(f"Lo scaffale {scaffale.codice} corrisponde al genere {nuovo_libro.genere}")
                aggiunta_a_scaffale = input("Aggiungo a questo scaffale? (y/n)")
                if aggiunta_a_scaffale == "y":
                    scaffale.aggiungi_libro(nuovo_libro)
                else:
                    Scaffale().aggiungi_libro(nuovo_libro)
    elif scelta == 2:
        libro_da_noleggiare = input("Quale libro vuoi noleggiare? ")
        trovato = False
        for scaffale in Scaffale.lista_scaffali:
            for libro in scaffale.lista_libri:
                if libro.titolo_libro().lower() == libro_da_noleggiare.lower():
                    if libro.disponibile:
                        libro.cambia_disponibilita()
                        print("Libro noleggiato!")
                        input("Continua...")
                        trovato = True
                    break # se ho piu libri con lo stesso nome noleggio solo il primo
        # se non trovo il libro stampo un messaggio
        if not trovato:
            print("Libro non disponibile")
    elif scelta == 3:
        for scaffale in Scaffale.lista_scaffali:
            print(scaffale, "-----------")