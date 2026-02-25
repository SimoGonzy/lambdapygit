# ==============================
# DIZIONARIO PRINCIPALE
# ==============================
prestitilibreria = {
    "Marco": {"libri": ["1984", "Dune"]},
    "Sara": {"libri": ["Harry Potter"]},
}

# ==============================
# FUNZIONI
# ==============================


# Mostra tutti i prestiti
def mostraprestiti():
    for nome, dati in prestitilibreria.items():
        print(f"Nome: {nome}, Libri: {dati['libri']}")


# Aggiunge una nuova persona
def aggiungipersona(nome, libri):
    prestitilibreria[nome] = {"libri": libri}


# Mostra i libri di una persona
def mostranome(nome):
    if nome in prestitilibreria:
        print(prestitilibreria[nome]["libri"])
    else:
        print("Persona non trovata.")


# Aggiunge un libro a una persona
def aggiungilibro(nome, libro):
    if nome in prestitilibreria:
        prestitilibreria[nome]["libri"].append(libro)
    else:
        print("Persona non trovata.")


# Rimuove un libro da una persona
def rimuovilibro(nome, libro):
    if nome in prestitilibreria and libro in prestitilibreria[nome]["libri"]:
        prestitilibreria[nome]["libri"].remove(libro)
    else:
        print("Persona o libro non trovato.")


# Modifica il nome di una persona
def modificanome(vecchio, nuovo):
    if vecchio in prestitilibreria:
        prestitilibreria[nuovo] = prestitilibreria.pop(vecchio)
    else:
        print("Persona non trovata.")


# Cerca chi ha un libro
def cercalibro(libro):
    trovato = False
    for nome, dati in prestitilibreria.items():
        if libro in dati["libri"]:
            print(f"Il libro '{libro}' è con {nome}")
            trovato = True
    if not trovato:
        print("Libro non trovato.")


# ==============================
# MENU
# ==============================

while True:
    print("\n--- MENU PRESTITI ---")
    print("1 - Mostra tutti i prestiti")
    print("2 - Aggiungi una nuova persona")
    print("3 - Mostra i libri di una persona")
    print("4 - Aggiungi un libro a una persona")
    print("5 - Rimuovi un libro da una persona")
    print("6 - Modifica il nome di una persona")
    print("7 - Cerca a chi appartiene un libro")
    print("stop - Uscire")

    scelta = input("Inserisci la tua scelta: ")

    if scelta == "stop":
        print("Programma terminato.")
        break

    elif scelta == "1":
        mostraprestiti()

    elif scelta == "2":
        nome = input("Nome persona: ")
        libri = input("Libri iniziali (separati da virgola): ").split(",")
        aggiungipersona(nome, libri)

    elif scelta == "3":
        nome = input("Nome persona: ")
        mostranome(nome)

    elif scelta == "4":
        nome = input("Nome persona: ")
        libro = input("Libro da aggiungere: ")
        aggiungilibro(nome, libro)

    elif scelta == "5":
        nome = input("Nome persona: ")
        libro = input("Libro da rimuovere: ")
        rimuovilibro(nome, libro)

    elif scelta == "6":
        vecchio = input("Nome attuale: ")
        nuovo = input("Nuovo nome: ")
        modificanome(vecchio, nuovo)

    elif scelta == "7":
        libro = input("Libro da cercare: ")
        cercalibro(libro)

    else:
        print("Scelta non valida!")
