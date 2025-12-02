from funzioni import * 

catalogo: list[dict] = []

print("Benvenuto nella tua libreria musicale!")

scelta = ""

while scelta != 0:
    scelta = int(input("\nCosa vuoi fare?\n1. Crea un nuovo album\n2. Aggiungi una traccia a un album esistente\n0. Esci\n\nScelta: "))
    
    if scelta == 1:
        
        titolo = input("\nTitolo album: ")
        autore = input("\nAutore album: ")
        album = crea_album(catalogo, titolo, autore)
        
    elif scelta == 2:
        
        titolo_album = input("\nInserisci il titolo dell'album a cui vuoi aggiungere una traccia: ")
        titolo = input("Inserisci il titolo della traccia: ")
        durata = int(input("Inserisci la durata della traccia (in secondi): "))
        voto = int(input("Inserisci il tuo voto per questa traccia (1-5): "))
        
        inserisci_traccia(catalogo, titolo_album, titolo, durata, voto)
        print("\nTraccia aggiunta con successo!")
        print(catalogo)
        
    if scelta <= 0:
        
        print("Uscita in corso...")
        exit()
        