import sqlite3

lista_strutture_comune = list()
lista_strutture_tipologia = list()

with sqlite3.connect("db_strutture_turistiche_veneto.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT comune, count(*) as numero_strutture FROM strutture AS s INNER JOIN indirizzi AS i ON s.id = i.id_struttura INNER JOIN comuni AS c ON i.id_comune = c.id GROUP BY c.comune ORDER BY comune ASC")
    lista_strutture_comune = cursor.fetchall()
    cursor.execute("SELECT tipologia, count(*) FROM strutture as s INNER JOIN tipologie_strutture as ts ON s.id = ts.id_struttura INNER JOIN tipologie as t ON ts.id_tipologia = t.id GROUP BY tipologia ORDER BY tipologia ASC")
    lista_strutture_tipologia = cursor.fetchall()
    conn.commit()

print("Tutti i comuni con 30 o più strutture:")
for strutture_comune in lista_strutture_comune:
    if strutture_comune[1] >= 30:
        print(f"- {strutture_comune[1]} strutture a {strutture_comune[0].title()}")

print("Numero di strutture per ogni tipologia:")
for struttura_tipologia in lista_strutture_tipologia:
    print(f"{struttura_tipologia[1]} - {struttura_tipologia[0].capitalize()}")