def main():

    rubrica = {
        "Mario Rossi": ["3331234567", "3479876543"],
        "Giulia Verdi": ["3201234567", "3487654321"],
        "Luca Bianchi": ["3498765432"],
        "Anna Neri": ["3339876543", "3465432109"],
        "Paolo Gialli": ["3327654321"]
    }

    while True:
        print("\nRubrica Telefonica")
        print("1. Aggiungi un nuovo contatto")
        print("2. Cerca un contatto per nome")
        print("3. Aggiungi/rimuovi numero a un contatto")
        print("4. Rimuovi un contatto")
        print("5. Modifica il nome di un contatto")
        print("6. Cerca a chi appartiene un numero")
        print("7. Visualizza l'intera rubrica")
        print("8. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == '1':
            aggiungi_contatto(rubrica)
        elif scelta == '2':
            cerca_contatto_per_nome(rubrica)
        elif scelta == '3':
            aggiungi_rimuovi_numero(rubrica)
        elif scelta == '4':
            rimuovi_contatto_per_nome(rubrica)
        elif scelta == '5':
            modifica_nome_contatto(rubrica)
        elif scelta == '6':
            cerca_a_chi_appartiene(rubrica)
        elif scelta == '7':
            for nome in rubrica:
                print(f"Contatto '{nome}':")
                for numero in rubrica[nome]:
                    print(f"  - {numero}")
        elif scelta == '8':
            print("Uscita dalla rubrica.")
            break
        else:
            print("Opzione non valida. Riprova.")


def aggiungi_contatto(rubrica):
    nome = input("Inserisci il nome del contatto: ")
    numeri_telefono = []
    while True:
        numero = input("Inserisci un numero di telefono (o 'fine' per terminare): ")
        if numero.lower() == 'fine':
            break
        numeri_telefono.append(numero)

    rubrica[nome] = numeri_telefono

    print(f"Contatto '{nome}' aggiunto con successo.")

def rimuovi_contatto_per_nome(rubrica):
    contatto = input("Inserisci il nome o il numero del contatto da rimuovere: ")
    trovato = False
    for nome, numeri in rubrica.items():
        if contatto in numeri:
            rubrica.pop(nome)
            trovato = True
            print(f"Il contatto '{contatto}' è stato rimosso dalla rubrica.")
            break
    if not trovato:
        print(f"Il contatto '{contatto}' non è presente nella rubrica.")

def cerca_contatto_per_nome(rubrica):
    nome = input("Inserisci il nome esatto del contatto da cercare: ")
    if nome in rubrica:
        print(f"Contatto '{nome}':")
        for numero in rubrica[nome]:
            print(f"  - {numero}")
    else:
        print(f"Contatto '{nome}' non trovato nella rubrica.")


def aggiungi_rimuovi_numero(rubrica):
    nome = input("Inserisci il nome esatto del contatto: ")
    if nome in rubrica:
        while True:
            numero = input("Inserisci il numero di telefono da aggiungere/rimuovere (o 'fine' per terminare): ")
            if numero.lower() == 'fine':
                break

            if numero in rubrica[nome]:
                rubrica[nome].remove(numero)
                print(f"Numero '{numero}' rimosso da '{nome}'.")
            else:
                rubrica[nome].append(numero)
                print(f"Numero '{numero}' aggiunto a '{nome}'.")
    else:
        print(f"Contatto '{nome}' non trovato nella rubrica.")


def modifica_nome_contatto(rubrica):

    nome_vecchio = input("Inserisci il nome del contatto da modificare: ")
    if nome_vecchio in rubrica:
        nuovo_nome = input("Inserisci il nuovo nome del contatto: ")
        rubrica[nuovo_nome] = rubrica.pop(nome_vecchio)  # Copia i numeri e rimuovi l'elemento vecchio
        print(f"Nome del contatto modificato da '{nome_vecchio}' a '{nuovo_nome}'.")
    else:
        print(f"Contatto '{nome_vecchio}' non trovato nella rubrica.")


def cerca_a_chi_appartiene(rubrica):
    numero = input("Inserisci il numero di telefono da cercare: ")
    trovato = False
    for nome, numeri in rubrica.items():
        if numero in numeri:
            print(f"Il numero '{numero}' appartiene a: {nome}")
            trovato = True
            break
    if not trovato:
        print(f"Il numero '{numero}' non è presente nella rubrica.")


# Esegui il programma
if __name__ == "__main__":
    main()
