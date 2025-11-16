# 03 - Strutture Dati: Liste, Tuple e Dizionari
# Esempi tratti dalla dispensa


# Esempio 1: Dichiarazione di una lista
# In questo esempio dichiariamo una lista di stringhe che rappresentano
# diversi linguaggi di programmazione.

langs: list[str] = [ "Python", "Rust", "JavaScript", "C", "GoLang", "Haskell" ]
print(langs)


# Esempio 2: Accesso agli elementi di una lista
# Qui mostriamo come accedere agli elementi di una lista utilizzando gli indici.
# Gli indici in Python partono da 0, quindi langs[0] restituisce il primo
# elemento della lista, langs[1] il secondo, e così via.

print(langs[0])
print(langs[1])

jspos: int = 2
print(langs[jspos])


# Esempio 3: Iterazione su una lista
# In questo esempio mostriamo due modi per iterare su una lista.
# Il primo utilizza un ciclo for con un indice per accedere a ciascun elemento.
# Il secondo utilizza un ciclo for diretto per iterare rapidamente sugli elementi della lista.

list_length: int = len(langs)
for pos in range(0, list_length):
    print(langs[pos])

for lang in langs:
    print(lang)


# Esempio 4: Modifica di una lista
# Qui mostriamo come modificare una lista in vari modi:
# - Variazione un elemento esistente
# - Aggiunta di un nuovo elemento alla fine della lista
# - Rimuozione un elemento specifico dalla lista

langs[2] = "Ruby"

langs.append("CommonLisp")

del langs[2]

last_lang: str = langs.pop()
print(last_lang)

langs.remove("C")


# Esempio 5: Verifica di appartenenza in una lista
# In questo esempio verifichiamo se un elemento specifico è presente
# all'interno della lista utilizzando l'operatore 'in'.

if "Python" in langs:
    print("Python è presente nella lista di linguaggi")
else:
    print("Python NON è presente nella lista di linguaggi")


# Esempio 6: List Comprehension
# Qui mostriamo come creare una nuova lista utilizzando una list comprehension.

numeri_pari: list[int] = [ num for num in range(0, 10) if num % 2 == 0 ]
print(numeri_pari)


# Esempio 7: Dichiarazione di una tupla
# In questo esempio dichiariamo una tupla che rappresenta un punto
# nello spazio tridimensionale con coordinate x, y e z.

point: tuple[float, float, float] = ( 1.0, 2.0, 3.0 )
print(point)


# Esempio 8: Accesso agli elementi di una tupla
# Qui mostriamo come accedere agli elementi di una tupla utilizzando gli indici.

x: float = point[0]
y: float = point[1]
z: float = point[2]


# Esempio 9: Iterazione su una tupla
# In questo esempio mostriamo come iterare su una tupla utilizzando un ciclo for.

for coord in point:
  print(coord)


# Esempio 10: Dichiarazione di un dizionario
# In questo esempio dichiariamo due dizionari:
# - nord_italia: un dizionario omogeneo che mappa le regioni del nord Italia
#   al loro numero di abitanti
# - persona: un dizionario eterogeneo che rappresenta le informazioni di una persona

nord_italia: dict[str, int] = {
  "Piemonte": 4_350_000,
  "Lombardia": 10_000_000,
  "Veneto": 4_900_000,
  "Liguria": 1_500_000,
  "Emilia-Romagna": 4_500_000,
  "Trentino-Alto Adige": 1_100_000,
  "Friuli-Venezia Giulia": 1_200_000
}
print(nord_italia)

persona: dict[str, str | int | float | bool] = {
  "nome": "Mario Rossi",
  "età": 30,
  "altezza": 1.75,
  "is_student": False
}
print(persona)


# Esempio 11: Accesso ai valori di un dizionario
# Qui mostriamo come accedere ai valori di un dizionario utilizzando le sue chiavi.

print(nord_italia["Lombardia"])
print(nord_italia["Emilia-Romagna"])


# Esempio 12: Iterazione su un dizionario
# In questo esempio mostriamo tre modi per iterare su un dizionario:
# - Iterare sulle chiavi
# - Iterare sui valori
# - Iterare su coppie chiave-valore

for regione in nord_italia:
  print(regione)

for abitanti in nord_italia.values():
  print(abitanti)

for regione, abitanti in nord_italia.items():
  print(regione + ": " + str(abitanti))


# Esempio 13: Utilizzo del metodo get() di un dizionario
# Qui mostriamo come utilizzare il metodo get() per accedere ai valori di un dizionario.
# Il metodo get() consente di specificare un valore di default nel caso in cui
# la chiave non sia presente nel dizionario, evitando KeyErrors quando si lavora con dati semistrutturati.

print(nord_italia.get("Sicilia", 0))


# Esempio 14: Modifica di un dizionario
# In questo esempio mostriamo come modificare un dizionario in vari modi:
# - Aggiornamento del valore associato a una chiave esistente
# - Aggiunta di una nuova coppia chiave-valore
# - Rimozione di una coppia chiave-valore

nord_italia["Lombardia"] = 10_050_000

nord_italia_province: dict[str, list[str]] = {
  "Piemonte": [ "Torino", "Novara", "Cuneo" ],
  "Lombardia": [ "Milano", "Bergamo", "Brescia" ]
}
nord_italia_province["Lombardia"].append("Varese")

nord_italia["Valle d'Aosta"] = 125_000

del nord_italia["Friuli-Venezia Giulia"]


# Esempio 15: Verifica di appartenenza in un dizionario
# In questo esempio verifichiamo se una chiave, un valore o una coppia chiave-valore
# sono presenti nel dizionario utilizzando l'operatore 'in'.

if "Lombardia" in nord_italia:
  print("Lombardia è presente nel dizionario")

if 10_050_000 in nord_italia.values():
  print("Esiste almeno una regione con 10.05 milioni di abitanti")

if ("Lombardia", 10_050_000) in nord_italia.items():
  print("La coppia Lombardia - 10.05 milioni è presente nel dizionario")


# Esempio 16: Creazione di un dizionario da una lista di tuple
# Qui mostriamo come creare un dizionario a partire da una lista di tuple,
# dove ogni tupla rappresenta una coppia chiave-valore.

sud_italia_list: list[tuple[str, int]] = [
  ("Campania", 5_800_000),
  ("Puglia", 4_000_000),
  ("Sicilia", 5_000_000)
]
sud_italia: dict[str, int] = dict(sud_italia_list)


# Esempio 17: Dict Comprehension
# In questo esempio, mostriamo come creare un dizionario utilizzando una dict comprehension.

quadrati: dict[int, int] = { num: num * num for num in range(1, 6) }
print(quadrati)


# Esempio 18: Mutabilità
# Qui mostriamo come la creazione di un alias per una lista non crei una copia indipendente,
# ma un riferimento allo stesso oggetto in memoria.

numeri_dispari: list[int] = [ 1, 3, 5, 7, 9 ]
dispari: list[int] = numeri_dispari
dispari.append(11)
print(dispari)
print(numeri_dispari)
