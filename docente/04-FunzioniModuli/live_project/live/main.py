"""
Questo script, assieme ai moduli contenuti all'interno del package `elezioni`,
è il risultato della sessione di live coding tenuta durante la quarta lezione
del corso.
Lo scopo del programma è consentire la gestione di liste elettorali composte
da partiti e candidati, permettendo di aggiungere partiti, candidati e votare
per i candidati stessi.
Questa versione dello script implementa le funzionalità così come sono state
proposte durante la lezione, utilizzando talvolta un approccio poco ottimizzato.
Per una soluzione più "ideale", si rimanda al package `soluzione`.
"""


from elezioni.comuni import aggiungi_partito, aggiungi_candidato
from elezioni.elettori import vota_candidato


partito1 = {
    "nome": "Partito di Valdagno",
    "candidati": [ { "nome": "Tizio", "voti": 0 } ]
}

partito2 = {
    "nome": "Partito di Recoaro",
    "candidati": [ { "nome": "Caio", "voti": 0 } ]
}

liste = [ partito1, partito2 ]


aggiungi_partito(liste, input("Come si chiama il partito? "))
aggiungi_candidato(liste, "Mario", "Partito di Schio")
vota_candidato(liste, "Partito di Schio", "Mario")
print(liste)
