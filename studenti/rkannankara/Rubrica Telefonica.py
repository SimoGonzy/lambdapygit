rubrica = {}

while True:
    print("MENU")
    print("1 - Aggiungere un nuovo contatto")
    print("2 - Cercare un contatto per nome")
    print("3 - Cercare un contatto per numero")
    print("4 - Aggiungere un numero a contatto")
    print("5 - Rimuovere un numero a contatto")
    print("6 - Modificare il nome di un contatto")
    print("0 - Esci")

    scelta = input("Scrivi il numero della scelta:    ")

    if scelta == "1":
        nome = input("Inserisci il nome del contatto:   ")
        if nome in rubrica:
            print("Il contatto è gia nella rubrica")
        else:
            numero = input("Inserisci il numero:      ")
            rubrica[nome] = [numero]
            print("Contatto aggiunto con successo")

    elif scelta == "2":
        nome = input("Inserisci il nome del contatto da cercare:    ")
        if nome in rubrica:
            print("Numero:", rubrica[nome])
        else:
            print("Contatto non trovato")

    elif scelta == "3":
        numero = input("Inserisci il numero del contatto da cercare:      ")
        trovato = False
        for nome in rubrica:
            if numero in rubrica[nome]:
                print("Il numero è di:", nome)
                trovato = True
                break
        if not trovato:
            print("Nessun contatto ha il numero inserito")

    elif scelta == "4":
        nome = input("A quale contatto vuoi aggiungere il numero?    ")
        if nome in rubrica:
            numero = input("Inserisci il numero che vuoi aggiungere:    ")
            rubrica[nome].append(numero)
            print("Il numero è aggiunto con successo")
        else:
            print("Contatto non trovato")

    elif scelta == "5":
        nome = input("Da quale contatto vuoi rimuovere il numero?   ")
        if nome in rubrica:
            print("Numero:", rubrica[nome])
            numero = input("Il numero da rimuovere:  ")
            if numero in rubrica[nome]:
                rubrica[nome].remove(numero)
                print("Il numero è stato rimosso con successo")
            else:
                print("Il numero non è stato trovato")
        else:
            print("Il contatto non è stato trovato")

    elif scelta == "6":
        nome = input("Inserisci il nome del contatto:    ")
        if nome in rubrica:
            nuovo_nome = input("Inserisci il nuovo nome:    ")
            rubrica[nuovo_nome] = rubrica[nome]
            del rubrica[nome]
            print("Il nuovo nome è modificato al contatto con successo")
        else:
            print("Il contatto non è stato trovato")

    elif scelta == "0":
        print("Uscita dal programma")
        break
    else:
        print("Scelta non valida")
