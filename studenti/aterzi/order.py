import sqlite3
from pathlib import Path

conn = sqlite3.connect("C:\\Users\\Admin\\Desktop\\sqlite\\songsconi.db")
c = conn.cursor()


file: Path = Path("C:\\Users\\Admin\\Desktop\\sqlite\\legacy_stream_logs.csv")
listaTot = []
with file.open("r", encoding="utf-8") as carica:
    if file.stat().st_size != 0:
        next(carica)
        for x in carica:
            lista = x.strip().split(",")
            listaTot.append(lista)

listaArtisti = []
listaGeneri = []
listaTipoAccount = []
listaAlbum: list[dict] = []
listaCanzoni: list[dict] = []
listaUsers: list[dict] = []
for row in listaTot:
    if row[5] not in listaArtisti:
        listaArtisti.append(row[5])
    if row[10] not in listaGeneri:
        listaGeneri.append(row[10])
    album = {"Name": row[8], "releaseYear": row[9]}
    if album not in listaAlbum:
        listaAlbum.append(album)
    canzone = {"Name": row[6], "Time": row[7], "Genere": row[10]}
    if canzone not in listaCanzoni:
        listaCanzoni.append(canzone)
    if row[4] not in listaTipoAccount:
        listaTipoAccount.append(row[4])
    user = {"Email": row[2], "Country": row[3]}
    if user not in listaUsers:
        listaUsers.append(user)


print(listaTipoAccount)
print(listaUsers)

# for row in listaGeneri:
#    c.execute(f"Insert into Genere ('Tipo') values ('{row}')")
# for row in listaArtisti:
#    c.execute(f"Insert into Artista ('Name') values ('{row}')")
# for row in listaTipoAccount:
#    c.execute(f"Insert into SubType ('Plan') values ('{row}')")
# for row in listaUsers:
#    c.execute(
#        f"Insert into User ('Email','Country') values ('{row['Email']}','{row['Country']}')"
#    )

for row in listaAlbum:
    c.execute(
        f"Insert into Album ('Name','ReleaseYear') values ('{row['Name']}','{row['releaseYear']}')"
    )


conn.commit()
conn.close()
