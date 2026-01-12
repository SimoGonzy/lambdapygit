rubricatelefonica = {}

rubricatelefonica["Mario Rossi"] = ["3662711135"]
rubricatelefonica["Giulia Bianchi"] = ["3201112222"]

while True:
    print("\nRUBRICA TELEFONICA")
    print("1 Aggiungere un nuovo contatto")
    print("2 Cercare un contatto per nome")
    print("3 Aggiungere o rimuovere un numero da un contatto")
    print("4 Modificare il nome di un contatto")
    print("5 Modificare il numero di un contatto")
    print("6 Cercare a chi appartiene un numero")
    print("7 Visualizzare tutta la rubrica")
    print("stop Uscire dal programma")

    scelta = input("Scegli un'opzione: ")

    if scelta.lower() == "stop":
        print("Uscita dal programma")
        break

    # 1 - Aggiungi contatto
    if scelta == "1":
        nome = input("Inserisci il nome: ")
        numero = input("Inserisci il numero: ")

        if nome not in rubricatelefonica:
            rubricatelefonica[nome] = [numero]
            print(f"Nuovo contatto aggiunto: {nome} -> {numero}")
        else:
            print("Il contatto è già presente")

    # 2 - Cerca per nome
    elif scelta == "2":
        nomedacercare = input("Inserisci il nome da cercare: ")
        if nomedacercare in rubricatelefonica:
            print(f"Numeri associati: {rubricatelefonica[nomedacercare]}")
        else:
            print("Il contatto non esiste")

    # 3 - Aggiungi o rimuovi numero
    elif scelta == "3":
        opt = input("1 per aggiungere numero, 2 per rimuovere numero: ")

        if opt == "1":
            nome = input("Inserisci il nome: ")
            numero = input("Inserisci il numero: ")
            if nome in rubricatelefonica:
                rubricatelefonica[nome].append(numero)
            else:
                rubricatelefonica[nome] = [numero]
            print(f"Contatto aggiornato: {nome} -> {rubricatelefonica[nome]}")

        elif opt == "2":
            nome = input("Inserisci il nome: ")
            numero = input("Numero da rimuovere: ")
            if nome in rubricatelefonica and numero in rubricatelefonica[nome]:
                rubricatelefonica[nome].remove(numero)
                print("Numero rimosso.")
            else:
                print("Nome o numero non trovato.")

    # 4 - Modifica nome contatto
    elif scelta == "4":
        nomevecchio = input("Nome da modificare: ")
        if nomevecchio in rubricatelefonica:
            nomenuovo = input("Nuovo nome: ")
            rubricatelefonica[nomenuovo] = rubricatelefonica.pop(nomevecchio)
            print("Nome modificato.")
        else:
            print("Contatto non trovato.")

    # 5 - Modifica numero (corretto)
    elif scelta == "5":
        nome = input("Inserisci il nome del contatto: ")

        if nome in rubricatelefonica:
            print(f"Numeri attuali: {rubricatelefonica[nome]}")
            numerovecchio = input("Inserisci il numero da sostituire: ")
            if numerovecchio in rubricatelefonica[nome]:
                numeronuovo = input("Inserisci il nuovo numero: ")
                idx = rubricatelefonica[nome].index(numerovecchio)
                rubricatelefonica[nome][idx] = numeronuovo
                print("Numero aggiornato.")
            else:
                print("Numero non trovato.")
        else:
            print("Contatto non trovato.")

    # 6 - Cerca numero per trovare il proprietario
    elif scelta == "6":
        numerodacercare = input("Inserisci il numero da cercare: ")
        trovato = False
        for nome, numeri in rubricatelefonica.items():
            if numerodacercare in numeri:
                print(f"Il numero appartiene a: {nome}")
                trovato = True
        if not trovato:
            print("Numero non trovato.")

    # 7 - Stampa tutta la rubrica
    elif scelta == "7":
        print("\n--- RUBRICA COMPLETA ---")
        for nome, numeri in rubricatelefonica.items():
            print(f"{nome}: {numeri}")

    else:
        print("Scelta non valida.")
