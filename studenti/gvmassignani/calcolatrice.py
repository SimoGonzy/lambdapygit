b = 1

while True:
    x = input(
        "'Che operazione vuoi fare? indica 1 per addizione, 2 per sottrazione, 3 per moltiplicazione e 4 per divisione': "
    )

    if x == "1":
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("Il risultato dell'operazione è: ", str(a + b))
    elif x == "2":
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("Il risultato dell'operazione è: ", str(a - b))
    elif x == "3":
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        print("Il risultato dell'operazione è: ", str(a * b))
    elif x == "4":
        a = float(input("Inserisci il primo numero: "))
        b = float(input("Inserisci il secondo numero: "))
        if b == 0:
            print("Errore, operazione non valida!")
            continue
        print("Il risultato dell'operazione è: ", str(a / b))
        break

    nuova_azione = input("Vuoi continuare ad utilizzare la calcolatrice? S/N: ")
    if nuova_azione == "S":
        continue
    else:
        print("A presto!")

    riparti = input("Premi invio per ricominciare: ")
    if riparti == " ":
        continue
