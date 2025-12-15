traccia1 = {
    "titolo": "ABC",
    "durata": 2.5,
    "voto": 5
}

traccia2 = {
    "titolo": "DEF",
    "durata": 1.8,
    "voto": 1
}

tracce: list[str] = [traccia1, traccia2]

album1 = {
    "titolo": "Pop",
    "autore": "gianni",
    "tracce": [ traccia1 ]
}

album2 = {
    "titolo": "Rock",
    "autore": "Mario",
    "tracce": [ traccia2 ]
}


album: list[str] = [album1, album2]

def aggiungi_traccia(titolo: str, durata: float, voto: float):
    nuova_traccia = {
        "titolo": titolo,
        "durata": durata,
        "voto": voto
    }
    tracce.append(nuova_traccia)

def aggiungi_traccia_album(titolo: str, durata: float, voto: float, album1: str):
    nuova_traccia = {
        "titolo": titolo,
        "durata": durata,
        "voto": voto
    }
    for i in range(len(album)):
        if album[i]["titolo"] == album1:
            album[i]["tracce"].append(nuova_traccia)
            return
   

def aggiungi_album(titolo_album: str, autore: str):
    nuovo_album = {
        "titolo": titolo_album,
        "autore": autore,
        "tracce": []
    }

    album.append(nuovo_album)

def mostra_album():
    for alb in album:
        print(f"Album: {alb['titolo']} - Autore: {alb['autore']}")
        if alb["tracce"]:
            print("  Tracce:")
            for traccia in alb["tracce"]:
                print(f"    - Titolo: {traccia['titolo']}, Durata: {traccia['durata']} min, Voto: {traccia['voto']}")
        else:
            print("  Nessuna traccia presente.")
        print()  # Riga vuota per separare gli album

#aggiungi_traccia("mario", 2.3, 5)
#print(tracce)
aggiungi_album("album1", "pippo")
aggiungi_traccia_album("titolo", 2, 4, "album1")
mostra_album()
