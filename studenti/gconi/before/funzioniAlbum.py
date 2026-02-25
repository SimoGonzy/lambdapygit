def aggiungiCanzone(lista, titolo: str, durata: int, voto: int = 1):
    tracciaCaso = {"titolo": titolo, "durata": durata, "voto": voto}  # crea una traccia
    lista.append(tracciaCaso)  # inserice nella lista tracce


def aggiungiAlbum(lista, titolo: str, autore: str):
    album = {"titoloAlbum": titolo, "Autore": autore, "tracce": []}  # crea un album
    lista.append(album)  # inserisce nella lista albums


def aggiungiTraccia(
    lista, pos: int, titoloAlbum: str, titolo: str, durata: int, voto: int = 1
):
    tracciaCaso = {"titolo": titolo, "durata": durata, "voto": voto}  # crea una traccia
    lista[pos]["tracce"].append(
        tracciaCaso
    )  # inserisce la traccia nella lista tracce presente nella lista albums
