from funzioni import *

album = []

singola_traccia = {
    "titolo": "",
    "durata": "",
    "voto": "",
}

print("Benvenuto nella tua libreria musicale! ")
scelta = int(input("\nCosa vuoi fare?\n"))


while scelta != 0:
    match scelta:
        case 1:
            crea_album(input("\n Titolo album"), input("\nAutore album"))
            break
        case 2:
            titolo = input("Aggiungi una nuova traccia ")
            durata = int(input("aggiungi durata "))
            voto = int(input("aggiungi voto "))
            inserisci_traccia(album,titolo,durata,voto)
            print("\nTraccia aggiunta con successo")
            print(album)
            break
        case 0:
