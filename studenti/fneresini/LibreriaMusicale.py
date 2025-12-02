traccia = {"nome": "nome_traccia", "durata": 334, "voto": 2} #forse se inizializziamo le key senza assegnarli un valore riusciamo a risolvere la cosa dell'elemento vuoto
lista_tracce = [traccia]

album = {"titolo": "titolo_album", "autore": "autore_album", "lista_tracce": []}
lista_album = [album]

controllo = True #variabile di controllo per il while
controlloInput = 0 #variabile di controllo per l'input

#funzione per aggiungere traccia alla lista delle tracce
def aggiungi_traccia(nome_traccia: str, durata_traccia: int, voto_traccia: int):
    traccia = { "nome": nome_traccia, "durata": durata_traccia, "voto": voto_traccia}
    lista_tracce.append(traccia)

#funzione per creare un nuovo album con lista_tracce VUOTA
def nuovo_album(titolo_album: str, autore_album: str):
    album = {"titolo": titolo_album, "autore": autore_album, "lista_tracce": []} #l'errore era che creavamo un album SENZA lista_tracce quindi poi l'append non aveva riferimenti
    lista_album.append(album)

#funzione per aggiungere una traccia alla lista_tracce dell'album corrispondente
def add_to_album(titolo_album: str, nome_traccia: str, durata_traccia: int, voto_traccia: int):
    for pos in range(len(lista_album)):
        if lista_album[pos]["titolo"] == titolo_album:
            megatraccia = {"nome": nome_traccia,"durata": durata_traccia,"voto": voto_traccia}#altro errore era qui dove mancavano "nome": ... "durata": ... come ci aveva detto Riccardo ieri
            lista_album[pos]["lista_tracce"].append(megatraccia)
            return

#rimuovo il primo elemento della lista album perchè viene creato vuoto
lista_album.pop(0)

#controllo del programma con input dall'utente
while(controllo == True):
    print("Premi 1 per aggiungere un album vuoto")
    print("Premi 2 per aggiungere una traccia ad un album")
    print("Scrivi 'esci' per uscire")
    controlloInput = input()
    if(controlloInput == "1"):#se l'input è = 1 chiamo la funzione per aggiungere un album senza tracce
        titolo_album_input = input("Scrivi titolo dell'album")
        autore_album_input = input("Scrivi l'autore dell'album")
        nuovo_album(titolo_album_input, autore_album_input)
        print(lista_album)
    elif(controlloInput == "2"):#se l'input è = 2 chiamo la funzione per aggiungere una traccia ad un album
        titolo_album_input = input("Scrivi titolo dell'album")
        nome_tracci_input = input("Scrivi nome traccia")
        durata_traccia_input  = input("Scrivi durata traccia")
        voto_traccia_input = input("Scrivi voto traccia")
        add_to_album(titolo_album_input, nome_tracci_input, durata_traccia_input, voto_traccia_input)
        print(lista_album)
    elif(controlloInput == "esci"):#se l'input è = esci termino il programma
        controllo = False
    else:#qualsiasi altro input dell'utente viene gestito con un print("Errore!") senza terminare il programma
        print("Errore!")