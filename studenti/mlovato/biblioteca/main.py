from biblioteca import Libro, Editore, Scaffale

active: bool = True

while active:
    print("Benvenuto nella biblioteca Lambda!")
    print("1 - Aggiungi libro")
    print("2 - Noleggia un libro")
    print("3 - Restituisci un libro")
    print("4 - Visualizza tutti gli scaffali")
    print("5 - Brucia un libro")
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
            libro = scaffale.cerca_libro_nome(libro_da_noleggiare)
            if libro and libro.disponibile:
                libro.cambia_disponibilita()
                print("Libro noleggiato!")
                trovato = True
                break # se ho piu libri con lo stesso nome noleggio solo il primo
        # se non trovo il libro stampo un messaggio
        if not trovato:
            print(f"{libro_da_noleggiare} non disponibile")
    elif scelta == 3:
        libro_da_restituire = input("Quale libro vuoi restituire? ")
        trovato = False
        for scaffale in Scaffale.lista_scaffali:
            libro = scaffale.cerca_libro_nome(libro_da_restituire)
            if libro and not libro.disponibile:
                libro.cambia_disponibilita()
                print("Libro restituito!")
                trovato = True
        if not trovato:
            print(f"{libro_da_restituire} non è registrato nei nostri archivi!")
    elif scelta == 4:
        for scaffale in Scaffale.lista_scaffali:
            print(scaffale, "-----------")
    elif scelta == 5:
        print("Non si bruciano libri qui dentro".upper())
    if scelta != 0:
        input("Continua...")
