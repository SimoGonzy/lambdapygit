import sqlite3
from pathlib import Path
import csv

dir = Path(__file__).parent
dir_db = dir / 'db_musica.db'
dir_csv = dir / 'legacy_stream_logs.csv'


sql_create_tables = [
    '''CREATE TABLE albums (
    id integer PRIMARY key AUTOINCREMENT,
    name text not null,
    release_date text not null
    );''',
    '''CREATE TABLE songs (
    id integer primary key AUTOINCREMENT,
    title text not null,
    duration integer not null,
    genre text not null,
    id_album integer,
    FOREIGN KEY (id_album) REFERENCES albums (id)
    );''',
    '''CREATE TABLE autors (
    id integer primary key AUTOINCREMENT,
    name text not null
    );''',
    '''CREATE TABLE autors_songs (
    id INTEGER primary key AUTOINCREMENT,
    id_autor INTEGER,
    id_song INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autors (id),
    FOREIGN KEY (id_song) REFERENCES songs (id)
    );''',
    '''CREATE TABLE users (
    id INTEGER,
    email TEXT NOT NULL,
    country text NOT NULL,
    subscription text NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT)
    );''',
    '''CREATE TABLE logs (
    id integer primary key,
    timestamp text not null,
    id_song integer not null,
    id_user integer not null,
    rating integer,
    FOREIGN KEY (id_song) REFERENCES songs (id),
    FOREIGN KEY (id_user) REFERENCES users (id)
    );''',
]

with sqlite3.connect(dir_db) as conn:
    cursor = conn.cursor()
    for create_table in sql_create_tables:
        cursor.execute(create_table)


id_album = 1
id_artist = 1
id_song = 1
id_artists_songs = 1
id_user = 1
dict_albums, dict_songs, dict_artists,dict_artists_songs, dict_users, dict_logs = {}, {}, {}, {}, {}, {}
with dir_csv.open('r', encoding='UTF-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        '''
        cursor.execute("INSERT INTO albums (name, release_date) values (?,?)", (row['AlbumName'], row['AlbumReleaseYear']))
        id_album = cursor.lastrowid
        cursor.execute("INSERT INTO songs (title, duration, genre, id_album) values (?,?,?,?)", (row['SongTitle'], row['SongDuration'], row['Genre'], id_album))
        id_song = cursor.lastrowid
        song_artists_list = row['ArtistName'].split("feat.")
        artist_song = []
        artists = []
        for artist in song_artists_list:
            cursor.execute("INSERT INTO autors (name) values (?)", (artist.strip(),))
            id_artist = cursor.lastrowid
            cursor.execute("INSERT INTO autors_songs (id_autor, id_song) values (?,?)", (id_artist, id_song))
        cursor.execute("INSERT INTO users (email, country, subscription) values (?,?,?)", (row['UserEmail'], row['UserCountry'], row['SubscriptionType']))
        id_user = cursor.lastrowid
        cursor.execute("INSERT INTO logs (id, timestamp, rating, id_song, id_user) values (?,?,?,?,?)", (row['LogID'], row['Timestamp'], row['UserRating'], id_song, id_user))
        '''
        if (row['AlbumName'],row['AlbumReleaseYear']) not in dict_albums.keys():
            dict_albums[(row['AlbumName'],row['AlbumReleaseYear'])] = id_album
            id_album+=1
        if (row['SongTitle'], row['Genre']) not in dict_songs.keys():
            dict_songs[(row['SongTitle'], row['Genre'])] = (row['SongDuration'], dict_albums[(row['AlbumName'],row['AlbumReleaseYear'])], id_song)
            id_song += 1
        song_artists_list = row['ArtistName'].split("feat.")
        for artist in song_artists_list:
            artist = artist.strip()
            if artist not in dict_artists.keys():
                dict_artists[artist] = id_artist
                id_artist += 1
            if (dict_artists[artist], dict_songs[row['SongTitle'], row['Genre']][2]) not in dict_artists_songs.keys():
                dict_artists_songs[(dict_artists[artist], dict_songs[row['SongTitle'], row['Genre']][2])] = id_artists_songs
                id_artists_songs +=1
        usermail = row['UserEmail'].lower()
        if usermail not in dict_users.keys():
            dict_users[usermail] = (row['UserCountry'], row['SubscriptionType'], id_user)
            id_user += 1
        dict_logs[row['LogID']] = (row['Timestamp'], row['UserRating'], dict_songs[row['SongTitle'], row['Genre']][2], dict_users[usermail][2])

with sqlite3.connect(dir_db) as conn:
    cursor = conn.cursor()
    for album, data in dict_albums.items():
        cursor.execute("INSERT INTO albums (name, release_date, id) values (?,?,?)", (album[0], int(album[1]), data))
    for song, data in dict_songs.items():
        cursor.execute("INSERT INTO songs (title, genre, duration, id_album, id) values (?,?,?,?,?)", (song[0],song[1], int(data[0]), data[1], data[2]))
    for autor, data in dict_artists.items():
        cursor.execute("INSERT INTO autors (name, id) values (?,?)", (autor, data))
    for autor_song, data in dict_artists_songs.items():
        cursor.execute("INSERT INTO autors_songs (id_autor, id_song, id) values (?,?,?)", (autor_song[0], autor_song[1], data))
    for mail, data in dict_users.items():
        cursor.execute("INSERT INTO users (email, country, subscription, id) values (?,?,?,?)", (mail, data[0], data[1], data[2]))
    for log, data in dict_logs.items():
        cursor.execute("INSERT INTO logs (id, timestamp, rating, id_song, id_user) values (?,?,?,?,?)", (int(log), data[0], int(data[1]), data[2], data[3]))




