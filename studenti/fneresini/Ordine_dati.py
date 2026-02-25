from pathlib import Path

file = Path("/home/filippo/Desktop/Databasse/legacy_stream_logs.csv")
User = Path("/home/filippo/Desktop/Databasse/user.csv")
Song = Path("/home/filippo/Desktop/Databasse/song.csv")
Album = Path("/home/filippo/Desktop/Databasse/album.csv")
Artist = Path("/home/filippo/Desktop/Databasse/artist.csv")
Ascolti = Path("/home/filippo/Desktop/Databasse/ascolti.csv")

#funzione per scrivere su file
def scrivi_su_file(percorso_file, ID, i, my_tuple):
    with percorso_file.open("a", encoding="UTF-8") as my_file:
        my_string = ""
        if ID == True:
            for item in my_tuple:
                my_string = my_string + f"{item},"
            my_string = my_string[:-1]
            my_string = f"{i}," + my_string
            my_file.write(f"{my_string}\n")
        else:
            for item in my_tuple:
                my_string = my_string + f"{item},"
            my_string = my_string[:-1]
            my_file.write(f"{my_string}\n")

#dizionari per sapere quale dato è gia presente nel database
album_dict = {}
song_dict = {}
artist_dict = {}
user_dict = {}

#counters per gli ID
counter_album = 1
counter_song = 1
counter_artist = 1
counter_user = 1

with file.open("r", encoding="UTF-8") as l:

    #prima riga album.csv
    scrivi_su_file(Album, False, 0, ("ID", "AlbumName", "AlbumReleaseYear"))
    #prima riga song.csv
    scrivi_su_file(Song, False, 0, ("ID", "SongTitle", "SongDuration", "Genre", "Album_ID"))
    #prima riga artist.csv
    scrivi_su_file(Artist, False, 0, ("ID", "ArtistName", "Song_ID"))
    #prima riga user.csv
    scrivi_su_file(User, False, 0, ("ID", "UserEmail", "UserCountry", "SubscryptionType"))
    #prima riga ascolti.csv
    scrivi_su_file(Ascolti, False, 0, ("LogID", "TimeStamp", "UserRating", "User_ID", "Song_ID"))

    prima_riga = next(l) #salto la prima riga perchè ci i nomi delle colonne scritte sopra

    for riga in l:
        #divido le righe "riga" del file in una lista di elementi su cui applico strip e lower per togliere spazi e possibili duplicati min/maiu
        riga_lista = [item.strip().lower() for item in riga.split(",")]

        #Album
        dati_album = (riga_lista[8], riga_lista[9])
        if dati_album not in album_dict.keys():
            album_dict[dati_album] = counter_album
            scrivi_su_file(Album, True, counter_album, dati_album)
            counter_album += 1
        
        #Song
        dati_song = (riga_lista[6], riga_lista[7], riga_lista[10], album_dict[(dati_album)])
        if dati_song not in song_dict.keys():
            song_dict[dati_song] = counter_song
            scrivi_su_file(Song, True, counter_song, dati_song)
            counter_song += 1
        
        #Artist
        dati_artist = (riga_lista[5])
        if dati_artist not in artist_dict.keys():
            artist_dict[dati_artist] = counter_artist
            scrivi_su_file(Artist, True, counter_artist, (riga_lista[5], song_dict[(dati_song)]))
            counter_artist += 1
        
        #User
        dati_user = (riga_lista[2], riga_lista[3])
        if dati_user not in user_dict.keys():
            user_dict[dati_user] = counter_user
            scrivi_su_file(User, True, counter_user, (riga_lista[2], riga_lista[3], riga_lista[4]))
            counter_user += 1
        
        #Ascolti
        dati_ascolti = (riga_lista[0], riga_lista[1], riga_lista[-1], user_dict[(dati_user)], song_dict[(dati_song)])
        scrivi_su_file(Ascolti, False, 0, dati_ascolti)