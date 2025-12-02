"""
def aggiungi_traccia(album, titolo: str, durata: int, voto: int):
    traccia = {
        "titolo": titolo,
        "durata": durata,
        "voto": voto
    }
    album.append(traccia)
"""    
    
def crea_album(catalogo, titolo: str, autore: str):
    album = {
        "titolo": titolo,
        "autore": autore,
        "tracce": [
            
        ]
    }
    catalogo.append(album)
    return catalogo
    
def inserisci_traccia(album, titolo_album: str, titolo: str, durata: int, voto: int):
    traccia = {
        "titolo": titolo,
        "durata": durata,
        "voto": voto
    }
    
    for i in range(len(album)):
        if album[i]["titolo"] == titolo_album:
            album[i]["tracce"].append(traccia)
            break