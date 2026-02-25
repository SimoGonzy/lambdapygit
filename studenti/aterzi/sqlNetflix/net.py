import sqlite3
from pathlib import Path

dbpath = Path(__file__).with_name("netflixdb.sqlite")
con = sqlite3.connect(dbpath, isolation_level=None)
cur = con.cursor()


def visualizzaDB(cur, str):
    offsetvalue = 0
    inp = ""
    while inp != "esci":
        query = f""" SELECT id, title FROM {str} ORDER BY title LIMIT 10 OFFSET {offsetvalue}"""
        cur.execute(query)

        results = cur.fetchall()
        for id, title in results:
            print(f"{id} | {title}")

        inp = input("\nVuoi andare avanti o indietro? (A/I) ").upper()

        if inp == "A":
            offsetvalue += 10
        elif inp == "I" and offsetvalue >= 10:
            offsetvalue -= 10
        else:
            print("Stai uscendo.....")
            break


scelta = ""

while scelta != 0:
    print("\n1. Visualizza film 2. Visualizza stagioni? 0. Esci")
    scelta = int(input("\nInserisci la scelta: "))

    if scelta == 1:
        print("\nLista Movies: ")
        visualizzaDB(cur, "movie")
    elif scelta == 2:
        print("\nLista Seasons: ")
        visualizzaDB(cur, "season")
    elif scelta == 0:
        print("\nArrivederci!")
        exit
