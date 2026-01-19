

'''album = {
    "titolo" : "Album1",
    "autore" : "Autorex", 
    "tracce" : "THE"

}'''

album_lista : list[any] = []

def aggiungi_album( titolo: str, autore: str):
    nuova_album={
        "titolo": titolo,
        "autore": autore,
        "tracce": [],
        
    }

    album_lista.append(nuova_album)


    
def aggiungi_album_tracce(titolo_album: str, titolo_traccia: str, durata_traccia: float, voto: int):
    nuova_traccia = {
                "titolo": titolo_traccia,
                "durata": durata_traccia,
                "voto": voto
            }
    
    for pos in range(len(album_lista)):
        if album_lista[pos]["titolo"] == titolo_album:
            album_lista[pos]["tracce"].append(nuova_traccia)
            return 
        
def mostra_album():
    for pos in range(len(album_lista)):
        print(f"Album: {album_lista[pos]['titolo']} - Autore: {album_lista[pos]['autore']}")
        print("Tracce:")
        for t in album_lista[pos]["tracce"]:
            print(f"  Titolo: {t['titolo']}, Durata: {t['durata']} min, Voto: {t['voto']}")
        print("-" * 30)



aggiungi_album ("A1", "A1")
mostra_album()






