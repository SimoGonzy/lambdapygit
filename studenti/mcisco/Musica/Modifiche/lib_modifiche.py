#libreria per la gestione delle tracce musicali

import os


def aggiungi_traccia(P):
    os.system('clear')
    while True:
        risposta2 = input("Vuoi aggiungere una traccia? (s/n): ")
        if risposta2.lower() != 's':
            os.system('clear')
            break

        nome_titolo = input("Inserisci il titolo della traccia: ")
        durata = input("Inserisci la durata della traccia (mm:ss): ")
        voto = float(input("Inserisci il voto della traccia (0.0 - 5.0): "))
        Traccia = {
            "Titolo": nome_titolo,
            "Durata": durata,
            "Voto": voto
        }
        P.append(Traccia)




def crea_Playlist(A):
    #A = Album
    os.system('clear')
    while True:
        risposta = input("Vuoi aggiungere una playlist all'album? (s/n): ")
        if risposta.lower() != 's':
            break

        Titolo_Playlist = input("Inserisci il nome della playlist: ")
        Autore_Playlist = input("Inserisci il nome dell'autore della playlist: ")

        #inizializzazione list Playlist 
        Playlist = {
            "Nome_Playlist": Titolo_Playlist,
            "Autore_Playlist": Autore_Playlist,
            "Playlist": []
        }
        aggiungi_traccia(Playlist["Playlist"])
        A["Album"].append(Playlist)


#stampa della playlist in maniera decente
def stampa(Album):
    os.system('clear')
    for pos_1 in range(len(Album)-1):
        print(f"Nome Album: {Album['Nome_Album']}\n")
        for pos_2 in range(len(Album["Album"])):
            print(f"  Nome Playlist: {Album['Album'][pos_2]['Nome_Playlist']}")
            print(f"  Autore Playlist: {Album['Album'][pos_2]['Autore_Playlist']}\n")
            for pos_3 in range(len(Album["Album"][pos_2]["Playlist"])):
                print(f"    Titolo Traccia: {Album['Album'][pos_2]['Playlist'][pos_3]['Titolo']}")
                print(f"    Durata Traccia: {Album['Album'][pos_2]['Playlist'][pos_3]['Durata']}")
                print(f"    Voto Traccia: {Album['Album'][pos_2]['Playlist'][pos_3]['Voto']}\n")


    
    

def crea_album():
    #richiedo i vari dati per creare l'album
    Nome_Album = input("Inserisci il nome dell'album: ")

    #Inizializzo la lista degli album vuota
    Album = {
        "Nome_Album": Nome_Album,
        "Album": []
    }

    crea_Playlist(Album)
    

    return Album

def calcolo_voto_medio(Album):
    totale_voti = 0
    numero_tracce = 0

    for playlist in Album["Album"]:
        for traccia in playlist["Playlist"]:
            totale_voti += traccia["Voto"]
            numero_tracce += 1

    voto_medio = totale_voti / numero_tracce
    return voto_medio

"""  
def cerca_autore(Album, titolo_Playlist: str, titolo_traccia: str):
    for pos_Play in Album["Album"]:
        if Album["Album"][pos_Play]["Nome_Playlist"].lower() == titolo_Playlist.lower():
            for pos_tra in Album["Album"][pos_Play]["Playlist"]:
                if Album["Album"][pos_Play]["Playlist"][pos_tra]["Titolo"].lower() == titolo_traccia.lower():
                    return Album["Album"][pos_Play]["Autore_Playlist"]
"""
def cerca_autore(Album, titolo_Playlist: str, titolo_traccia: str):
    for playlist in Album["Album"]:
        if playlist["Nome_Playlist"].lower() == titolo_Playlist.lower():
            for traccia in playlist["Playlist"]:
                if traccia["Titolo"].lower() == titolo_traccia.lower():
                    return playlist["Autore_Playlist"]
