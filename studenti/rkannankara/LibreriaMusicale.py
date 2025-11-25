from sys import int_info

traccia = {
    "nome": "Espresso",
    "artista": "Sabrina Carpenter",
    "durata_minuti": 2.55,
    "voto": 4,
}

playlist = []

album = {
    "titolo": "20",
    "autore": "Sabrina Carpenter",
    "tracce": [
        {
            "nome": "Espresso",
            "artista": "Sabrina Carpenter",
            "durata_minuti": 2.55,
            "voto": 4,
        }
    ],
}

discografia = [album]


def aggiungi_playlist(
    playlist: list, titolo: str, artista: str, durata_minuti: float, voto: int
):
    nuovo_canzone = {
        "nome": titolo,
        "artista": artista,
        "durata_minuti": durata_minuti,
        "voto": voto,
    }
    playlist.append(nuovo_canzone)


def crea_nuovo_album(titolo: str, artista: str):
    nuovo_album = {"titolo": titolo, "artista": artista, "tracce": []}
    discografia.append(nuovo_album)


def inserisci_traccia(album: dict, titolo: str, durata_minuti: float, voto: int):
    for pos in range(len(discografia)):
        if discografia[pos]["titolo"] == album:
            discografia[pos]["tracce"].append(
                {
                    "nome": titolo,
                    "artista": discografia[pos]["autore"],
                    "durata_minuti": durata_minuti,
                    "voto": voto,
                }
            )
            break


aggiungi_playlist(playlist, "Call me Baby", "Carly Rae Jepsen", 3.31, 5)
print(playlist)

crea_nuovo_album("21", "Sabrina Carpenter")
print(discografia)

inserisci_traccia("20", "Rageboy", 3.2, 3)
print(album)
