def aggiungi_traccia(lista, titolo: str, durata: float, voto: int): 
    traccia = {
        "titolo": titolo,
        "durata": durata,
        "voto": voto
    }
    for pos in range(len(lista)):
        if lista[pos]["nome"] == titolo:

    lista.append(traccia)


def aggiungi_album(lista, titolo: str, autore: str):
    album = {
        "titolo": titolo,
        "autore": autore
    }
    lista.append(album)




album = {
    "titolo": "Album Prova",
    "autore": "Autore Prova",
    "tracce": [{ "titolo": "Prova", "durata": 3.17, "voto":4 }]
}

lista = [album]


#aggiungi_traccia(lista, (input("Inserisci il titolo della traccia: ")), float(input("Inserisci la durata della traccia: ")), int(input("Inserisci il voto della traccia (da 1 a 5): ")))
aggiungi_album(lista, input("Inserisci il titolo dell'album: "), input("Inserisci l'autore dell'album: "))
print(lista)