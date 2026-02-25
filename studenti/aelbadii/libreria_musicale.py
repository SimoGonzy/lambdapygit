#elemento base di ogni collezione musicale sono le singole tracce,
#quindi il nostro programma non potrà prescindere dal gestirle:
#• Trovare una rappresentazione adatta a descrivere una singola
#traccia con i suoi dati annessi (titolo, durata, voto da 1 a 5);
#• Creare una funzione che, data una lista e questi tre dati,
#aggiunga in coda alla lista la rappresentazione della traccia.



lista=[]

def aggiungi_traccia(titolo: str,traccia: str, durata: int,voto: int):
    nuova_traccia={
        "traccia":traccia,
        "durata":durata,
        "voto":voto
    }
    for pos in range(len(lista)):
        if(lista[pos]["titolo"]==titolo):
            lista[pos]["traccia"].append(nuova_traccia)
            break

def aggiungi_album(titolo: str,autore: str):
   album={
    "titolo" :titolo,
    "autore":autore,
    "traccia":[]
   }
   lista.append(album)



aggiungi_album(input("Inserisci il nome dell'album\t"),input("Inserisci il nome dell'autore dell'album\t"))
aggiungi_traccia("ciao",input("Inserisci il titolo della traccia\t"),int(input("Inserisci la durata\t")),int(input("Inserisci il voto (da 1 a 5)\t")))


print(lista)

