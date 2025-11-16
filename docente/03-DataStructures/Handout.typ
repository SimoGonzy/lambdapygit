// == Imports ==

#import "../common/typst/cover.typ": handout_cover
#import "../common/typst/utils.typ": slidew, center_url


// == Setup ==

#let title = "Strutture Dati: Liste, Tuple e Dizionari"
#let course = "Python: da Zero a OOP"
#let description = ""
#let author = "Riccardo Sacchetto, B.Sc."
#let email = "riccardo.sacchetto@itsdigitalacademy.com"

// Configurazione delle proprietà base
#set text(font: "New Computer Modern", size: 10pt, fill: black, lang: "it")
#set document(author: author, title: title)

// Definizione look&feel
#set page(numbering: none, number-align: center, fill: none, margin: auto)
#set par(leading: 0.65em)
#set heading(numbering: none)
#set cite(style: "chicago-fullnotes")
#show heading: set block(above: 1.4em, below: 1em)
#show link: set text(fill: rgb("#035a75"))


// == Content ==

#handout_cover(
  title: title, course: course,
  description: description,
  author: author, email: email
)

#set page(numbering: "1")

= Le Strutture Dati

Dopo aver perfezionato la nostra conoscenza dei tipi di dato primitivi e del controllo del flusso di esecuzione, è il momento di esplorare le strutture dati più complesse che Python mette a disposizione: liste, tuple e dizionari.

Questi costrutti si chiamano "strutture" perchè sono in grado di contenere al loro interno più istenze dei tipi di dato primitivi che abbiamo visto finora, fungendo da contenitori organizzati e strutturati.

Le strutture che andremo a trattare in questa dispensa sono le seguenti:

- *Liste*: Come suggerisce il nome, sono delle collezioni ordinate e mutabili di elementi eterogenei. Risultano particolarmente utili per raggruppare una quantità possibilmente variabile di elementi con caratteristiche in comune (e.g., la lista di lettere dell'alfabeto latino, dei numeri da 0 a 9, dei voti di matematica di una certa classe...);
- *Tuple*: Simili alle liste, ma immutabili. Sono utili quando si desidera garantire che una collezione di elementi rimanga costante nel tempo (e.g., le coordinate di un punto nello spazio, i giorni della settimana...);
- *Dizionari*: Collezioni mutabili di elementi eterogenei organizzati in coppie chiave-valore. Sono ideali per rappresentare dati strutturati in cui ogni elemento è associato a una chiave univoca (e.g., una rubrica telefonica, un database di utenti con la loro password...).

Tutte queste strutture dati, incluse direttamente nel linguaggio senza bisogno di librerie aggiuntive, sono fondamentali per la programmazione in Python e ci permetteranno di gestire e manipolare i dati in modo più efficiente e organizzato.

#pagebreak()

= Le Liste

Iniziamo la nostra trattazione partendo dalle liste, che sono probabilmente la struttura dati più utilizzata.

In Python, le liste sono definite racchiudendo gli elementi tra parentesi quadre `[]`, separati da virgole. Ad esempio, un elenco di linguaggi di programmazione può essere salvato in una nuova variabile e stampato a schermo come segue:

```python
langs: list[str] = [ "Python", "Rust", "JavaScript", "C", "GoLang", "Haskell" ]
print(langs)
```

== Accedere a una lista

Nota come, in questo primissimo esempio, l'output è costituito esattamente dalla rappresentazione testuale della lista, completa di parentesi quadre e virgolette:

```
['Python', 'Rust', 'JavaScript', 'C', 'GoLang', 'Haskell']
```

Per quanto utile per il debug, questa rappresentazione non si può certo definire leggibile per l'utente finale. Per provare a stampare gli elementi della lista potremmo innanzitutto estrarli dalla lista uno ad uno, utilizzando gli indici:

```python
print(langs[0])         # "Python"
print(langs[1])         # "Rust"

jspos: int = 2
print(langs[jspos])     # "JavaScript"

print(langs[6])         # IndexError: list index out of range
```

Questa sintassi ci consente, essenzialmente, di accedere a qualsiasi elemento della lista specificandone la posizione (l'indice) tra parentesi quadre dopo il nome della variabile che contiene la lista. Ricordando infatti che gli N elementi di una lista sono ordinati, possiamo identificare ciascuno di essi in maniera univoca tramite la sua posizione nella struttura dati, che parte da 0 per il primo elemento e arriva a N-1 per l'ultimo.

Questo meccanismo di accesso è molto utile, ma diventa rapidamente scomodo quando la lista contiene molti elementi o quando vogliamo eseguire la stessa operazione su tutti i membri della lista.

Un altro tentativo per ottenere un pretty print della lista potrebbe quindi essere quello di utilizzare un ciclo `for` per iterare su tutti i numeri da 0 a N-1 e utilizzarli per recuperare i vari elementi (`len(list)` ci permette di recuperare il numero di elementi contenuti in `list`):

```python
list_length: int = len(langs)
for pos in range(0, list_length):
  print(langs[pos])
```

In effetti, essendo che la funzione `range(a, b)` ci consente di eseguire il corpo del `for` per ogni intero da `a` (incluso) a `b` (escluso!) inserendo man mano nella variabile `pos` il valore corrente, possiamo sfruttare questa tecnica per recuperare gli elementi della lista uno ad uno.

Tuttavia, questa soluzione è ancora un po' macchinosa e non sfrutta appieno le potenzialità di Python. Fortunatamente, infatti, il linguaggio ci mette a disposizione un metodo più semplice e diretto per iterare sugli elementi di una lista senza doverci preoccupare degli indici:

```python
for lang in langs:
  print(lang)
```

Nota come questo pezzettino di codice sia molto più leggibile e conciso rispetto alla versione precedente; in questo caso, infatti, il ciclo `for` itera direttamente sugli elementi della lista `langs`, inserendone uno alla volta nella variabile `lang` prima di eseguire il proprio corpo (in questo caso, una banale `print`).

== Modificare una lista

Le liste in Python sono mutabili, il che significa che possiamo modificare il loro contenuto dopo la creazione; saremo dunque in grado di variare, aggiungere o rimuovere gli elementi di una lista utilizzando vari metodi e operazioni.

Il primo tipo di modifica che possiamo effettuare su una lista è l'aggiornamento di un elemento esistente, possibile semplicemente assegnando un nuovo valore a un indice specifico della lista:

```python
langs[2] = "Ruby"   # "JavaScript" -> "Ruby"
```

Per quanto riguarda l'aggiunta di nuovi elementi, possiamo utilizzare il metodo `append()` per accodare un elemento alla fine della lista:

```python
langs.append("CommonLisp")
```

Infine, per rimuovere un elemento abbiamo diverse possibilità:

- L'istruzione `del` ci consente di rimuovere un elemento presente ad uno specifico indice, come:
  ```python
  del langs[2]                      # Rimuove "Ruby"
  ```

- Il metodo `pop` rimuove l'ultimo elemento della lista, ritornandolo come valore:
  ```python
  last_lang: str = langs.pop()      # Rimuove "CommonLisp"
  print(last_lang)                  # "CommonLisp"
  ```

- Il metodo `remove` consente di cercare uno specifico valore nella lista e di rimuoverlo:
  ```python
  langs.remove("C")                 # Rimuove "C"
  ```

== Operazioni sulle liste

Oltre alle operazioni di modifica, Python offre una serie di metodi utili per lavorare con le liste che il lettore è invitato a esplorare e testare autonomamente nella documentazione ufficiale disponibile all'indirizzo https://docs.python.org/3/tutorial/datastructures.html#more-on-lists (punto 5.1.0).

Molto interessanti per scrivere velocemente codice che fa uso delle liste sono piuttosto l'operatore `in` e la sintassi per la list comprehension.

L'operatore `in` ci consente di verificare se un certo elemento è presente all'interno di una lista, restituendo un valore booleano (`True` o `False`); ad esempio:

```python
if "Python" in langs:
  print("Python è presente nella lista di linguaggi")
else:
  print("Python NON è presente nella lista di linguaggi")
```

La list comprehension, invece, è una sintassi compatta che ci permette di creare nuove liste applicando un'espressione a ciascun elemento di una sequenza esistente, eventualmente filtrando gli elementi in base a una condizione. Ad esempio, possiamo creare una nuova lista contenente solo i numeri pari tra 0 e 9 (l'operatore `%` consente di calcolare il resto della divisione tra due numeri):

```python
numeri_pari: list[int] = [ num for num in range(0, 10) if num % 2 == 0 ]
print(numeri_pari)   # [0, 2, 4, 6, 8]
```

#pagebreak()

= Le Tuple

Estremamente simili alle liste, le tuple sono anch'esse collezioni ordinate di elementi eterogenei; la differenza principale risiede nel fatto che le tuple sono immutabili, il che significa che una volta create non possono essere modificate.

In Python, le tuple sono definite racchiudendo gli elementi tra parentesi tonde `()`, separati da virgole. Ad esempio, una tupla che rappresenta le coordinate di un punto nello spazio tridimensionale può essere definita come segue (nota come la tupla venga annotata con il tipo `tuple[float, float, float]`, indicando fin da subito che andrà a contenere tre elementi di tipo `float`):

```python
point: tuple[float, float, float] = ( 1.0, 2.0, 3.0 )
print(point)
```

Come prima, l'output di questa semplice `print` sarà la rappresentazione testuale della tupla:

```
(1.0, 2.0, 3.0)
```

gli elementi della tupla potranno essere indirizzati tramite il loro indice:

```python
x: float = point[0]    # 1.0
y: float = point[1]    # 2.0
z: float = point[2]    # 3.0
```

e sarà possibile iterare su di essi mediante un ciclo `for`:

```python
for coord in point:
  print(coord)
```

mentre non sarà possibile modificarne il contenuto, pena l'insorgere di un errore di tipo `TypeError`:

```python
point[0] = 4.0         # TypeError: 'tuple' object does not support item assignment
```

#pagebreak()

= I Dizionari

Ultima struttura dati che andremo a trattare in questa dispensa sono i dizionari, che, come suggerisce il nome, ci consentono di mappare delle chiavi univoche a dei valori correlati, esattamente come un vocabolario associa a una parola il suo significato.

In Python, i dizionari sono definiti racchiudendo le coppie chiave-valore tra parentesi graffe `{}`, con ogni coppia separata da una virgola e la chiave e il valore separati da due punti `:`. Ad esempio, un dizionario contenente le regioni del nord italia e i loro abitanti può essere definito come segue:

```python
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
```

Mentre un dizionario eterogeneo potrebbe essere definito come:

```python
persona: dict[str, str | int | bool] = {
  "nome": "Mario Rossi",
  "età": 30,
  "is_student": False
}
```

Anche con i dizionari, l'output della `print` sarà la rappresentazione testuale della struttura dati:

```
{'Piemonte': 4350000, 'Lombardia': 10000000, 'Veneto': 4900000, 'Liguria': 1500000, 'Emilia-Romagna': 4500000, 'Trentino-Alto Adige': 1100000, 'Friuli-Venezia Giulia': 1200000}
```

== Accedere a un dizionario

La prima differenza sostanziale tra i dizionari e le altre strutture dati viste finora risiede nel modo in cui si accede ai loro elementi: mentre liste e tuple utilizzano indici numerici, i dizionari utilizzano infatti le chiavi associate ai valori che si intendono estrarre.

Ad esempio, se volessimo recuperare il numero di abitanti della Lombardia e dell'Emilia-Romagna, potremmo farlo come segue:

```python
print(nord_italia["Lombardia"])
print(nord_italia["Emilia-Romagna"])
```

Ne consegue che Python non fornirà alcuna garanzia sull'ordine degli elementi all'interno di un dizionario, dato che l'accesso avviene tramite chiavi piuttosto che tramite posizioni numeriche.

Questo, ovviamente, non significa che non sia possibile iterare sugli elementi di un dizionario, tanto più che il ciclo `for` ci consente di scorrere chiavi, valori e coppie chiave-valore del dizionario:

```python
# Stampa le chiavi (nomi delle regioni)
for regione in nord_italia:
  print(regione)

# Stampa i valori (numero di abitanti)
for abitanti in nord_italia.values():
  print(abitanti)

# Stampa le coppie chiave-valore
for regione, abitanti in nord_italia.items():
  print(regione + ": " + str(abitanti))
```

Si noti piuttosto che, esattamente come per le liste, tentare di accedere a una chiave non presente nel dizionario genererà un errore (`KeyError`):

```python
print(nord_italia["Sicilia"])    # KeyError: 'Sicilia'
```

Visto però che nell'utilizzare dati semistrutturati può essere comune imbattersi in chiavi mancanti, Python mette a disposizione il metodo `get()`, il quale permette di specificare un valore di default da restituire nel caso in cui la chiave richiesta non sia presente nel dizionario:

```python
print(nord_italia.get("Sicilia", 0))   # Stampa 0 se "Sicilia" non è presente
```

== Modificare un dizionario

Anche i dizionari sono mutabili, il che significa che possiamo aggiungere, modificare o rimuovere coppie chiave-valore anche dopo la sua creazione. Come per le liste, possiamo aggiornare il valore associato a una chiave esistente semplicemente assegnandole un nuovo elemento:

```python
nord_italia["Lombardia"] = 10_050_000
```

Nota tuttavia che a ogni chiave può essere associato un solo valore, il quale andrà sovrascriverà il dato precedente. L'unico modo per associare più valori a una singola chiave è dunque quello di utilizzare una struttura dati più complessa - come una lista o una tupla - in veste di valore associato a quella chiave; ad esempio, potremmo decidere di associare a ogni regione una lista di province:

```python
nord_italia_province: dict[str, list[str]] = {
  "Piemonte": [ "Torino", "Novara", "Cuneo" ],
  "Lombardia": [ "Milano", "Bergamo", "Brescia" ]
}

nord_italia_province["Lombardia"].append("Varese")
```

Per quanto riguarda invece l'aggiunta e la rimozione di coppie chiave-valore, con i dizionari non serve ricorrere a metodi appositi, in quanto possiamo semplicemente assegnare un valore a una nuova chiave per inserirlo nel dizionario:

```python
nord_italia["Valle d'Aosta"] = 125_000
```

e utilizzare l'istruzione `del` per effettuare una rimozione:

```python
del nord_italia["Friuli-Venezia Giulia"]
```

== Operazioni sui dizionari

Anche con i dizionari è possibile utilizzare l'operatore `in` per verificare la presenza di una chiave, di un valore o di una coppia chiave-valore all'interno dello stesso, prestando tuttavia attenzione a comporre lo statement nel modo corretto:

```python
if "Lombardia" in nord_italia:
  print("Lombardia è presente nel dizionario")

if 10_050_000 in nord_italia.values():
  print("Esiste almeno una regione con 10 milioni di abitanti")

if ("Lombardia", 10_050_000) in nord_italia.items():
  print("La coppia Lombardia - 10 milioni è presente nel dizionario")
```

Un dizionario può poi essere costruito partendo da una lista di coppie chiave-valore utilizzando la funzione `dict()`:

```python
sud_italia_list: list[tuple[str, int]] = [
  ("Campania", 5_800_000),
  ("Puglia", 4_000_000),
  ("Sicilia", 5_000_000)
]
sud_italia: dict[str, int] = dict(sud_italia_list)
```

oppure sfruttando la dict comprehension:

```python
quadrati: dict[int, int] = { num: num * num for num in range(1, 6) }
print(quadrati)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#pagebreak()

= Attenzione alla mutabilità!

Un aspetto importante da tenere a mente quando si lavora con le strutture dati in Python è la distinzione tra tipi mutabili e immutabili.

Le liste e i dizionari, infatti, come dicevamo nelle scorse pagine e al contrario di quanto accade con tuple e tipi primitivi (`int`, `float`, `str`, ...), possono essere variati in un momento terzo a quello della loro creazione, con importanti implicazioni qualora si decida di passarli come argomento a una funzione o di assegnarli a una nuova variabile.

Prediamo ad esempio questo frammento di codice:

```python
numeri_dispari: list[int] = [ 1, 3, 5, 7, 9 ]
dispari: list[int] = numeri_dispari
dispari.append(11)
print(dispari)
print(numeri_dispari)
```

Ad un primo sguardo, essendo che l'operazione di aggiunta di un elemento viene eseguita sulla nuova variabile (`dispari`), potrebbe sembrare che la variabile originale (`numeri_dispari`) non venga modificata, con il risultato che l'output del codice proposto sia:

```
[1, 3, 5, 7, 9, 11]
[1, 3, 5, 7, 9]
```

In realtà, andando a immaginare le variabili come etichette che puntano a degli oggetti in memoria

#align(center)[
  #image("./images/01-mutability01.png", width: 40%)
]

possiamo notare che, nella situazione che viene a crearsi nel nostro esempio, la nuova variabile non fa altro che puntare allo stesso oggetto della variabile originale, con il risultato che qualsiasi modifica apportata attraverso il nuovo nome andrà a riflettersi anche sulla variabile originale:

#align(center)[
  #image("./images/02-mutability02.png", width: 40%)
]

Ne consegue banalmente che l'output corretto del frammento di codice proposto sia:

```
[1, 3, 5, 7, 9, 11]
[1, 3, 5, 7, 9, 11]
```
