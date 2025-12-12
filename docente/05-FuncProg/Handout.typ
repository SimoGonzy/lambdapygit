// == Imports ==

#import "../common/typst/cover.typ": handout_cover
#import "../common/typst/utils.typ": slidew, center_url


// == Setup ==

#let title = "Programmazione Funzionale e Iteratori"
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

= Un nuovo paradigma di programmazione

Negli scorsi laboratori abbiamo iniziato a gettare le fondamenta di quella che si definisce programmazione imperativa, ovvero basata sullo scrivere comandi che modificano lo stato della macchina in modo sequenziale riuscendo così a risolvere problemi di varia natura.

Si pensi ad esempio a come si potrebbe scrivere un programma che prende una lista di interi, calcola il quadrato degli elementi pari e inserisce in una nuova lista solo i risultati maggiori di 20:

```python
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result: list[int] = []
for x in numbers:
    if x % 2 == 0:
        y: int = x * x
        if y > 20:
            result.append(y)
print(result)  # [36, 64, 100]
```

In questo esempio, il nostro programma dovrà inizializzare una lista vuota da usare come output e, mano a mano che itera nella lista numbers, concatenarvi i risulatati delle operazioni di quadrato qualora rispettino le condizioni fissate.

Questo approccio, caratterizzato dallo "spiegare" al computer come svolgere ogni piccolo step di calcolo, è tipico della programmazione imperativa, dove lo stato del programma cambia nel tempo attraverso l'uso di variabili e strutture di controllo.

Essendo Python un linguaggio di programmazione multi-paradigma, tuttavia, possiamo beneficiare anche di altri stili di programmazione, tra cui la programmazione funzionale, che ci consente di esprimere le nostre soluzioni in modo più conciso e dichiarativo, concentrandoci sul "cosa" vogliamo ottenere piuttosto che sul "come" ottenerlo.

Un primissimo esempio di come questo potrebbe apparire sono sicuramente le list comprehensions, già viste in precedenza:

```python
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result: list[int] = [x * x for x in numbers if x % 2 == 0 and (x * x) > 20]

print(result)  # [36, 64, 100]
```

La programmazione funzionale, tuttavia, non si limita alle list comprehensions, ma introduce concetti più ampi come l'uso di funzioni di ordine superiore, l'immutabilità dei dati e l'assenza di effetti collaterali, che ci permettono di scrivere codice con un approccio radicalmente diverso, come vedremo in queste pagine.

#pagebreak()

= Le lambda functions e le funzioni di ordine superiore

== Funzioni anonime

Il primo concetto con cui prendere confidenza per addentrarsi nella programmazione funzionale è quello delle funzioni anonime - o lambda functions - che ci permettono di definire funzioni "al volo" senza doverle nominare esplicitamente.

Facciamo un primissimo esempio riprendendo il caso banale del calcolo del perimetro di un rettangolo:

```python
def perimeter(length: int, width: int) -> int:
    return 2 * (length + width)

print(perimeter(5, 10))  # 30
```

Come visto in precedenza, questo codice definisce una funzione `perimeter` che prende in input due numeri e restituisce il perimetro del rettangolo, che in questo caso viene passato alla funzione `print` per essere mostrato a schermo.

Se volessimo definire questa stessa funzione in una singola riga, senza doverle dare un nome esplicito, potremmo usare una lambda function:

```python
perimeter: Callable[[int, int], int] = lambda length, width: 2 * (length + width)
print(perimeter(5, 10))  # 30
```

Per quanto possa apparire strano, questo codice fa esattamente la stessa cosa del precedente, definendo la funzione `perimeter` mediante la sintassi `lambda` che prende in input i parametri `length` e `width` (in questo caso elencati immediatamente dopo la keyword), calcola il valore del perimetro e lo restituisce immediatamente senza la necessità di utilizzare un `return` esplicito.

== Niente comandi, solo espressioni

Ad una prima occhiata, le lambda functions potrebbero sembrare poco più che una curiosità sintattica, fornendo un modo più compatto (per quanto di difficile interpretazione) per definire delle funzioni che eseguono un singolo calcolo.

In realtà, prestando più attenzione all'esempio, si nota come la lambda function sia completamente priva di un modo per "contenere" un blocco di codice, limitando così il suo corpo ad un'unica espressione che viene valutata e il cui risultato viene immediatamente restituito.

Una domanda che potrebbe dunque sorgere spontanea a questo punto è: se le `lambda`-function non sono altro che funzioni associate ad una variabile ma limitate ad una singola espressione, qual è il loro scopo pratico?

Per iniziare a rispondere a questa domanda proviamo a scrivere un nuovo esempio che fa uso della lambda function in un altro contesto che, seppur ancora lontano da quello del loro reale uso, vi si avvicina maggiormente:

```python
print((lambda length, width: 2 * (length + width))(5, 10))
```

In questo caso, la lambda function viene definita "al volo" e invocata immediatamente con i parametri `5` e `10`, restituendo il valore del perimetro che viene poi passato alla funzione `print` per essere mostrato a schermo. Ecco dunque il superpotere delle lambda functions: essere definite inline all'interno di altre espressioni senza la necessità di una intera `def`inizione.

== L'altro pezzo del puzzle

Per arrivare a comprendere appieno il potenziale delle lambda functions, tuttavia, è necessario introdurre un altro concetto fondamentale della programmazione funzionale: le funzioni di ordine superiore (higher-order functions).

Immaginiamo, sulla falsariga del primo esempio visto in apertura, di voler spostare il codice che calcola la lista `result` in una funzione separata, in modo da poterla riutilizzare più facilmente:

```python
def quadrati_oltre_20(numbers: list[int]) -> list[int]:
    result: list[int] = []
    for x in numbers:
        if x % 2 == 0:
            y: int = x * x
            if y > 20:
                result.append(y)
    return result

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(quadrati_oltre_20(numbers))  # [36, 64, 100]
```

Fin qui non c'è nulla di nuovo: per ottenere il risultato desiderato abbiamo semplicemente incapsulato il codice in una funzione chiamata `quadrati_oltre_20`, che prende in input una lista di numeri e restituisce la lista dei quadrati maggiori di 20.

Immaginiamo però che il requisito sia diverso: invece di calcolare il quadrato dei numeri pari prima di controllare se sono maggiori di 20, vogliamo permettere al chiamante di definire una computazione arbitararia (ad esempio, il cubo).

Per fare questo, possiamo modificare la nostra funzione in modo che prenda in input una funzione come parametro, che verrà usata per calcolare il valore da confrontare con 20:

```python
def quadrato(val: int) -> int:
    return val * val

def cubo(val: int) -> int:
    return val * val * val

def risultati_oltre_20(
    numbers: list[int],
    func: Callable[[int], int]
) -> list[int]:
    result: list[int] = []
    for x in numbers:
        if x % 2 == 0:
            y: int = func(x)
            if y > 20:
                result.append(y)
    return result

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(risultati_oltre_20(numbers, quadrato))  # [36, 64, 100]
print(risultati_oltre_20(numbers, cubo))  # [64, 216, 512, 1000]
```

In questo esempio, la funzione `risultati_oltre_20` prende in input una lista di numeri e una funzione `func` che accetta un intero e restituisce un intero; all'interno di essa, `func` viene chiamata per calcolare il valore `y`, che viene poi confrontato con 20.

Queste funzioni di ordine superiore - il cui nome deriva dal fatto che possono accettare altre funzioni come argomenti o restituirle come risultati e la cui designazione più corretta è "funzionali" - sono un concetto chiave della programmazione funzionale, permettendoci di scrivere codice più astratto e riutilizzabile, in grado di fornire al chiamante la possibilità di cambiarne il comportamento in base alle sue necessità semplicemente passando funzioni diverse come argomenti.

== Combiniamo il tutto

Ora che abbiamo fatto la conoscenza dei funzionali e visto come operano, dovrebbe venire naturale intravedere la principale utilità delle lambda functions a loro fianco.

Ma procediamo per gradi: nel nostro esempio di prima, abbiamo definito due funzioni `quadrato` e `cubo` per calcolare rispettivamente il quadrato e il cubo di un numero, che abbiamo poi passato alla funzione `risultati_oltre_20` per ottenere i risultati desiderati. Questo approccio è sicuramente valido qualora queste funzioni vengano utilizzate anche in altri contesti, ma può risultare ingombrante e poco pratico qualora tale assunzione non trovi riscontro nella realtà.

In questi casi, possiamo dunque sfruttare il superpotere delle lambda functions per definire le funzioni "al volo" direttamente all'interno della chiamata a `risultati_oltre_20`, risparmiandoci così l'onere di nominarle esplicitamente:

```python
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(risultati_oltre_20(
    numbers,
    lambda val: val * val
))  # [36, 64, 100]
print(risultati_oltre_20(
    numbers,
    lambda val: val * val * val
))  # [64, 216, 512, 1000]
```

Ecco quindi il cuore della programmazione funzionale: combinare funzioni di ordine superiore con lambda functions per scrivere codice più conciso, espressivo e flessibile, in grado di adattarsi facilmente a diverse esigenze senza dover sacrificare la chiarezza o la manutenibilità.

#pagebreak()

= Gli iteratori

Uno dei principali contesti in cui la programmazione funzionale brilla particolarmente è quello della manipolazione di collezioni di dati, come liste e dizionari.

In Python, infatti, qualunque oggetto iterabile (come le liste) può essere trasformato in un iteratore, che consente di attraversare gli elementi uno alla volta e di applicare operazioni funzionali su di essi in modo elegante e conciso.

== Map e Filter

Due dei funzinali più comuni e potenti per lavorare con gli iteratori sono `map` e `filter`, che ci permettono rispettivamente di trasformare e filtrare gli elementi di una collezione utilizzando operazioni da noi definite e passate come funzioni.

Per illustrare il loro funzionamento, analizziamo un caso in cui dobbiamo calcolare il quadrato di tutti gli elementi di una lista:

```python
small_numbers: list[int] = [1, 2, 3, 4, 5]
squared_numbers: list[int] = list(map(
    lambda x: x * x,
    numbers
))
print(squared_numbers)  # [1, 4, 9, 16, 25]
```

Qui la funzione `map` prende in input una funzione (in questo caso una lambda function che calcola il quadrato di un numero) e un iterabile (la lista `numbers`), applicando la funzione a ciascun elemento dell'iterabile e restituendo un nuovo iteratore con i risultati, che viene poi convertito in una lista.

Allo stesso modo, `filter` ci consente di selezionare solo gli elementi che soddisfano una certa condizione, ad esempio l'essere pari:

```python
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers: list[int] = list(filter(
    lambda x: x % 2 == 0,
    numbers
))
print(even_numbers)  # [2, 4, 6, 8, 10]
```

In questo caso, `filter` prende una funzione che restituisce `True` o `False` (la lambda function che verifica se un numero è pari) e un iterabile, restituendo un nuovo iteratore contenente solo gli elementi per cui la funzione ha restituito `True`.

A questo punto, combinando `map` e `filter`, possiamo risolvere il problema iniziale di calcolare i quadrati dei numeri pari maggiori di 20 in modo più conciso (anche se in realtà questa non è ancora la forma ideale, che andremo a costruire fra qualche laboratorio):

```python
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result: list[int] = list(filter(
    lambda y: y > 20,
    map(
        lambda x: x * x,
        filter(
            lambda x: x % 2 == 0,
            numbers
        )
    )
))
print(result)  # [36, 64, 100]
```

Si noti come, in questo esempio, abbiamo innestato più chiamate a `filter` e `map` per ottenere il risultato desiderato: per interpretarle correttamente, è utile partire dall'interno verso l'esterno, notando come prima vengano filtrati i numeri pari, poi calcolati i loro quadrati e infine selezionati quelli maggiori di 20.

== Aggregazioni con Reduce

Un ultimo funzionale di grande utilità per lavorare con gli iteratori è `reduce`, che ci permette di aggregare gli elementi di una collezione in un singolo valore, applicando una funzione binaria che combina due elementi alla volta.

Per esempio, supponiamo di voler calcolare la somma di tutti gli elementi di una lista:

```python
from functools import reduce

small_numbers: list[int] = [1, 2, 3, 4, 5]
total: int = reduce(
    lambda x, y: x + y,
    small_numbers
)
print(total)  # 15
```

In primis, notiamo come il funzionale `reduce` non sia immediatamente disponibile in Python, ma debba essere importato dal modulo `functools` (comunque incluso nella libreria standard e, dunque, immediatamente disponibile in qualunque installazione).

In secundis, constatiamo come il comportamento della `reduce` sia leggermente più complesso rispetto a quello della `map` o della `filter`; essa prende infatti in input una funzione binaria (in questo caso una lambda function che somma due numeri) e un iterabile, eseguendo la funzione per ogni elemento della collezione affiancato al risultato parziale ottenuto fino a quel momento, fino a ridurre l'intera collezione ad un singolo valore. Passo dopo passo, la traccia degli input e output della funzione lambda è dunque la seguente:

#table(
  columns: (1fr, 1fr, 1fr),
  stroke: none,
  align: center,
  table.header([*`x`*], [*`y`*], [*output*]),
  table.hline(),
  [`1` (primo elemento)], [`2` (secondo elemento)], [`1+2 = 3`],
  [`3` (risultato parziale)], [`3` (terzo elemento)], [`3+3 = 6`],
  [`6` (risultato parziale)], [`4` (quarto elemento)], [`6+4 = 10`],
  [`10` (risultato parziale)], [`5` (quinto elemento)], [`10+5 = 15`],
)
