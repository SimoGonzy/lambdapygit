"""
Realizzare un algoritmo di raccomandazione di contenuti che,
dato un database di utenti e di film che hanno gradito:
• Prenda in input il nome dell’utente corrente;
• Trovi quello più simile (cfr. coefficiente di Jaccard);
• Suggerisca i film che l’utente simile ha gradito e che l’utente
corrente non ha ancora visto.

"""

db_utenti: list[dict[str, str | set[str]]] = [
    {
    "utente": "utente1",
    "film_graditi": {"Pirati dei Caraibi", "Harry Potter", "Signore degli anelli"}
    },
    {
    "utente": "utente2",
    "film_graditi": {"Harry Potter", "Film1", "Film2", "Signore degli anelli"}
    },
    {
    "utente": "utente3",
    "film_graditi": {"Pirati dei Caraibi", "Film3", "Film2"}
    },
]

utente_corrente_nome = input("Utente corrente: ")
utente_corrente: dict[str, str | set[str]] = {"nome":"default", "film_graditi": {"default"}}
for utente in db_utenti:
    if utente["utente"] == utente_corrente_nome:
        utente_corrente = utente
        break
utente_simile: dict[str, str | set[str]] = {"nome":"default", "film_graditi": {"default"}}
valore_utente_simile: float = 0.0
for utente in db_utenti:
    if utente["utente"] != utente_corrente_nome:
        temp = float(len(utente["film_graditi"].intersection(utente_corrente["film_graditi"]))/len(utente["film_graditi"].symmetric_difference(utente_corrente["film_graditi"]))) # type: ignore
        if valore_utente_simile < temp:
            valore_utente_simile = temp
            utente_simile = utente

print(f"L'utente più simile è: {utente_simile['utente']}") 

for film in utente_simile["film_graditi"]:
    if film not in utente_corrente["film_graditi"]:
        print(f"Questo film potrebbe piacerti {film}")