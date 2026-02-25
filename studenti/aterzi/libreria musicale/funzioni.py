"""
def aggiungi_traccia(libreria_musicale, titolo: str, durata: int, voto: int):

    traccia = {
        "titolo": titolo,
        "durata": durata,
        "voto": voto
    }

    libreria_musicale.append(traccia)
"""


def crea_album(titolo: str, autore: str):
    return {"titolo": titolo, "autore": autore, "tracce": []}


def inserisci_traccia(album, titolo: str, durata: int, voto: int):
    traccia = {"titolo": titolo, "durata": durata, "voto": voto}

    album["tracce"].append(traccia)
