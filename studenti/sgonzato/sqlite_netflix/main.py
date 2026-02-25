from pathlib import Path
import sqlite3
import datetime
import os
clear = lambda: os.system('cls')

dbpath = Path(__file__).with_name("netflixdb.sqlite")

#if dbpath.exists():
#   print("\nEsiste")

con = sqlite3.connect(dbpath, isolation_level=None)
cur = con.cursor()

def visualizzaDB(cur, str):
    inp = ""
    offsetvalue = 0
    
    while (inp != 'esci'):
        query = f''' SELECT id, title FROM {str} ORDER BY title LIMIT 10 OFFSET {offsetvalue} '''
        
        cur.execute(query)

        results = cur.fetchall()
        for id, title in results:
            print(f"{id} | {title} ")
            
        id = input(f"\nInserisci l'id del {str} di cui vuoi vedere i dettagli: ")
        if id.isnumeric():
            stampaDettagli(cur, id, str)
        else:
            print("Errore!")
            continue
        
        inp = input("\nVuoi procedere o tornare indietro? (A/I) ").upper()
        
        if(inp == 'A'):
            offsetvalue += 10
        elif(inp == 'I' and offsetvalue >= 10):
            offsetvalue -= 10
        else:
            print("\nStai uscendo...")
            break
        
def motoreRicerca(cur, search):
    if search == "F":
        v = input("\nInserisci cosa vuoi cercare: (T - L - A) ")
        if v == "T":
            titolo = input("\nInserisci il titolo del film: ")
            
            query = f''' SELECT id, title FROM movie WHERE title LIKE '%{titolo}%' ORDER BY title LIMIT 10 '''
            cur.execute(query)

            results = cur.fetchall()
            for id, title in results:
                print(f"{id} | {title} ")

    elif search == "S":
        v = input("\nInserisci cosa vuoi cercare: (T - A) ")
        if v == "T":
            titolo = input("\nInserisci il titolo della stagione")
            query = f''' SELECT id, title FROM season WHERE title = '%{titolo}%' ORDER BY title LIMIT 10 '''
            cur.execute(query)

            results = cur.fetchall()
            for id, title in results:
                print(f"{id} | {title} ")
        
    

def stampaDettagli(cur, id, str):
    query = f''' SELECT release_date, runtime, title FROM {str} WHERE id = {id} '''
        
    cur.execute(query)

    results = cur.fetchall()
    for release_date, runtime, title in results:
        time_millis = release_date
        base = datetime.datetime(1970, 1, 1)
        delta = datetime.timedelta(0, 0, 0, time_millis)
        dt = base + delta
        print(f"Release date: {dt} | Runtime: {runtime}min | Titolo: {title} ")
    
#MAIN
scelta = -1

while scelta != 0:
    print("\n1. Visualizza Film\n2. Visualizza Stagioni\n3. Motore di ricerca\n0. Esci")
    scelta = int(input("\nInserisci la scelta: "))
    
    if scelta == 1:
        clear()
        print("\nLista Film: ")
        visualizzaDB(cur, "movie")
    elif scelta == 2:
        clear()
        print("\nLista Stagioni: ")
        visualizzaDB(cur, "season")
    elif scelta == 3:    
        clear()
        print("\n--- Motore di ricerca ---")
        search = input("\nCosa vuoi cercare? (film - F o stagione - S) ").upper().strip()
        motoreRicerca(cur, search)
    elif scelta == 0:
        clear()
        print("\nArrivederci!")
        exit