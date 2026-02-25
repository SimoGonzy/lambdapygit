from funzioniAlbum import aggiungiAlbum, aggiungiTraccia

traccia1 = {"titolo": "Cristmass", "durata": 300, "voto": 1}
tracce = [traccia1]
album = {"titoloAlbum": "LeCse", "Autore": "Kanye", "tracce": [tracce]}
albums = [album]  # lista di dizionari

decisione = ""
while decisione != 0:  # Inizio del ciclo del menù
    try:  # try exept ti permette di raccogliere gli errori senza mandare tutto in crash
        decisione = int(
            input("0)Exit\n1)aggiungi album\n2)aggiungi traccia\n3)Visualizza\n")
        )  # variabile che ti permette di scegliere tra le opzioni(forzata ad intero)
        if decisione == 1:  # inserisce l'album vuoto
            titolo = input("inserisci il titolo dell'album\n")
            autore = input("Inserisci l'autore\n")
            aggiungiAlbum(albums, titolo, autore)
        elif decisione == 3:  # visualizza tutto
            print(albums)
        elif decisione == 2:  # inserisce una traccia nell'album
            titoloAlbum = input(
                "inserisci il titolo dell'album: \n"
            )  # raccoglie in titolo dell'album
            i = -1  # dichiara i
            for pos in range(
                len(albums)
            ):  # ciclo per prendere la posizione dell'album in base al titolo
                if albums[pos]["titoloAlbum"] == titoloAlbum:
                    i = pos  # se lo trova imposta i al valore della posizione
            if i >= 0:  # se i ha un valore entra nell'if
                titolo = input("inserisci un titolo: \n")
                durata = input("inserisci una durata in secondi: \n")
                voto = input("inserisci un voto da 1 a 5: \n")
                while int(voto) < 1 or int(voto) > 5:
                    voto = input("inserisci un voto da 1 a 5: \n")
                aggiungiTraccia(albums, i, titoloAlbum, titolo, int(durata), int(voto))
            else:  # se i non ha un valore entra nel print
                print("album non trovato")
        else:
            print("inserisci un opzione valida\n")
    except ValueError:
        print("Valore Errato")
        decisione = ""
