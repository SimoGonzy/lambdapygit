import sqlite3
from pathlib import Path

dir = Path(__file__).parent
dir_db = dir / 'db_musica.db'

with sqlite3.connect(dir_db) as conn:
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM songs WHERE genre='Jazz' and duration > (5*60)")
    jazz_songs_5_mins = cursor.fetchall()
    print(f"There are: {len(jazz_songs_5_mins)} jazz songs that are at least 5 mins long")
    '''for song in jazz_songs_5_mins:
        print(song)'''
    cursor.execute("SELECT songs.title, count(*) FROM songs inner join logs on songs.id=logs.id_song inner join users on logs.id_user=users.id where country='France' group by songs.title order by count(*) desc limit 5")
    best_5_france = cursor.fetchall()
    print("\n","-"*10,"Top 5 France","-"*10)
    for song in best_5_france:
        print(f"{song[0]} - {song[1]} ascolti")

    cursor.execute("SELECT genre, avg(duration) from songs group by genre")
    avg_duration_per_genre = cursor.fetchall()
    print("\n","-"*10,"Durata media per genere","-"*10)
    for genre in avg_duration_per_genre:
        print(f"{genre[0]} durata media: {genre[1]:.2f}")
    
    cursor.execute("SELECT users.email, count(*) from users inner join logs on users.id=logs.id_user inner join songs on logs.id_song=songs.id inner join autors_songs on songs.id=autors_songs.id_song group by users.id, logs.timestamp, autors_songs.id_autor having count(logs.id)>=2 ")
    who_listen_at_least_10 = cursor.fetchall()
    print(who_listen_at_least_10)