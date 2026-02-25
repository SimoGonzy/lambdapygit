numeri = []

# Inserimento iniziale numeri
while True:
    valori = input("Inserisci numeri separati da virgola: ")
    try:
        numeri = [float(x.strip()) for x in valori.split(",")]
        break
    except ValueError:
        print("Errore: inserisci solo numeri validi!")

# Calcolo valori utili
somma = sum(numeri)
prodotto = 1
for n in numeri:
    prodotto *= n
media = somma / len(numeri)

# Menu
while True:
    print("\n--- MENU ---")
    print("Premi 1 per somma, prodotto e media")
    print("Premi 2 per ordinare la lista (crescente)")
    print("Premi 3 per ordinare la lista (decrescente)")
    print("Premi 4 per vedere il numero più grande")
    print("Premi 5 per vedere il numero più piccolo")
    print("Premi 6 per vedere i numeri sopra la media")
    print("Premi 7 per vedere i numeri sotto la media")
    print("Scrivi 8 per visualizzare la lunghezza della lista")
    print("Scrivi 'stop' per uscire")

    scelta = input("Inserisci la tua scelta: ")

    if scelta == "1":
        print(f"SOMMA: {somma}")
        print(f"PRODOTTO: {prodotto}")
        print(f"MEDIA: {media}")

    elif scelta == "2":
        print("Lista ordinata crescente:", sorted(numeri))

    elif scelta == "3":
        print("Lista ordinata decrescente:", sorted(numeri, reverse=True))

    elif scelta == "4":
        print("Numero massimo:", max(numeri))

    elif scelta == "5":
        print("Numero minimo:", min(numeri))

    elif scelta == "6":  # il sopra la media e sotto si possono fare in due modi 6 e 7
        sopra_media = []

        for x in numeri:
            if x > media:
                sopra_media.append(x)

        print("Numeri sopra la media:", sopra_media)

    elif scelta == "7":
        sotto_media = [x for x in numeri if x < media]
        print("Numeri sotto la media:", sotto_media)

    elif scelta == "8":
        lunghezzalista = len(numeri)
        print(f"la lista è lungha {lunghezzalista}")

    elif (
        scelta.lower() == "stop"
    ):  # il .lower() serve per traformare tutti i caratteri delle sringhe in minuscolo es "CIAO" = "ciao"
        break

    else:
        print("Scelta non valida!")
