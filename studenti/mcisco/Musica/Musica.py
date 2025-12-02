#Musica
#Importazione librerie
from Modifiche.lib_modifiche import stampa, crea_album, calcolo_voto_medio, cerca_autore

Album = crea_album()
stampa(Album)

print(f"\nVoto medio dell'album: {calcolo_voto_medio(Album)}")

while True:
    risposta = input("Vuoi cercare l'autore di una traccia? (s/n): ").lower()
    if risposta != 's':
        break

    autore = cerca_autore(Album, input("Inserisci il nome della playlist da cercare: "), input("Inserisci il nome della traccia da cercare: "))
    print(f"L'autore della traccia è: {autore}\n")