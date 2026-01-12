"creare un dizioanrio auto"

"AGGIUNGERE UNA NUOVA CHIAVE"
"modificare un valore"
"rimuovere una chiave"

# creazione del dizionario
auto = {"nome": "audi", "modello": "rs3", "annoprod": "2019"}
# aggiungere una nuova chiave (ps chiave : valore)
auto["alimentazione"] = "benzina"
# modificare un valore
auto["nome"] = "bmw"

# stampo il contenuto
print(auto)


# se volessi aggiungere una nuova chiave tramitre una funzione:
# questa parte è sempre uguakle prima di utilizzare una funzione
def aggchiave(diz, chiave, valore):
    diz[chiave] = valore


aggchiave(auto, "cavalli", "500")


# rimozione chiave tramite funzione
def rimuovichiave(diz, chiave):
    if chiave in diz:
        diz.pop(chiave)


rimuovichiave(auto, "annoprod")

# se volessi stamparlo invece di un print con un for:
for chiave, valore in auto.items():
    print(chiave, valore)
