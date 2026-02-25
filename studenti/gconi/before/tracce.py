from funzioniAlbum import aggiungiCanzone

traccia1 = {"titolo": "Cristmass", "durata": 300, "voto": 1}
tracce = [traccia1]

decisione = ""
while decisione != 0:  # Inizio del ciclo del menù
    try:  # try exept ti permette di raccogliere gli errori senza mandare tutto in crash
        decisione = int(
            input("0)Exit\n1)aggiungi canzone\n2)Visualizza\n")
        )  # variabile che ti permette di scegliere tra le opzioni(forzata ad intero)
        if decisione == 1:
            titolo = input("inserisci un titolo: \n")
            durata = input("inserisci una durata in secondi: \n")
            voto = input("inserisci un voto da 1 a 5: \n")
            while int(voto) < 1 or int(voto) > 5:  # controlla che Voto sia tra 1 e 5
                voto = input("inserisci un voto da 1 a 5: \n")
            aggiungiCanzone(tracce, titolo, int(durata), int(voto))
        elif decisione == 2:
            print(tracce)
        else:
            print("inserisci un opzione valida")
    except ValueError:
        print("Valore Errato")
        decisione = ""
