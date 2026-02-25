// == Imports ==

#import "../common/typst/cover.typ": handout_cover
#import "../common/typst/utils.typ": slidew, center_url


// == Setup ==

#let title = "Funzioni e Moduli"
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

= Organizzare il Codice

Negli scorsi laboratori abbiamo studiato i costrutti di base di Python: variabili, tipi primitivi, strutture dati e controllo del flusso di esecuzione. Tutti questi elementi costituiscono i blocchetti fondamentali per scrivere programmi in Python e sono teoricamente sufficienti per realizzare qualsiasi tipo di software ci venga in mente.

Come abbiamo tuttavia notato nel corso delle esercitazioni, scrivere programmi anche relativamente semplici può portare a dover gestire file di codice molto lunghi, complessi e pieni di ripetizioni, difficili da leggere, comprendere e manutenere.

È in questo contesto che entrano in gioco le funzioni e i moduli, due concetti fondamentali per organizzare il codice in modo più efficiente, leggibile e riutilizzabile.

Prendiamo ad esempio il caso comune di un menu che consente all'utente di scegliere tra diverse opzioni: senza funzioni, il programma presenterebbe molteplici rami, ognuno dei quali contenente tutto il codice necessario a gestire l'operazione, in un approccio che porta inevitabilmente a codice difficile da seguire:

```python
operazione: str = input("Operazione da eseguire [+, -, *, /]: ")
if operazione == "+":
    val1: int = int(input("Primo addendo: "))
    val2: int = int(input("Secondo addendo: "))
    somma: int = val1 + val2
    print(f"Somma: {somma}")
elif operazione == "-":
    val1: int = int(input("Minuendo: "))
    val2: int = int(input("Sottraendo: "))
    differenza: int = val1 - val2
    print(f"Differenza: {differenza}")
elif operazione == "*":
    val1: int = int(input("Primo fattore: "))
    val2: int = int(input("Secondo fattore: "))
    prodotto: int = val1 * val2
    print(f"Prodotto: {prodotto}")
elif operazione == "/":
    val1: int = int(input("Dividendo: "))
    val2: int = int(input("Divisore: "))
    quoziente: float = val1 / val2
    quoto: int = val1 // val2
    resto: int = val1 % val2
    print(f"Quoziente: {quoziente}")
    print(f"Quoto: {quoto}")
    print(f"Resto: {resto}")
else:
    print("Operazione non valida.")
```

Ovviamente in questo esempio il codice è volutamente ridondante per evidenziare il problema; in un programma reale, infatti, si cercherebbe di evitare la ripetizione del codice per la lettura dei valori e la stampa dei risultati, ma non è difficile intuire come il codice possa diventare rapidamente ingombrante e difficile da gestire.

#pagebreak()

= Le Funzioni: codice con un nome

Per risolvere i problemi di leggibilità e ridondanza, Python offre il concetto di funzione, che consente di raggruppare un blocco di codice sotto un nome significativo che può poi essere utilizzato per "chiamarlo".

La sintassi di base per la definizione di una funzione in Python è la seguente:

```python
def nome_funzione():
  # Corpo della funzione...
```

Dove:
- `def` è la parola chiave che indica la definizione di una funzione;
- `nome_funzione` è il nome scelto per la funzione, che dovrebbe essere descrittivo del suo scopo, che ha gli stessi vincoli di denominazione delle variabili e che deve seguire la convenzione `snake_case`;
- Il corpo della funzione contiene il codice che viene eseguito quando la funzione viene chiamata.

Ad esempio, possiamo definire una funzione `addizione` che chiede all'utente i due addendi e ne calcola la somma da mostrare a schermo, in modo da poter iniziare a snellire il codice dell'esempio precedente:

```python
def addizione():
    val1: int = int(input("Primo addendo: "))
    val2: int = int(input("Secondo addendo: "))
    somma: int = val1 + val2
    print(f"Somma: {somma}")
```

Questa funzione - e le eventuali gemelle per le altre operazioni algebriche - può ora essere chiamata nel programma principale per eseguire l'operazione di addizione utilizzando la sintassi `nome_funzione()`:

```python
operazione: str = input("Operazione da eseguire [+, -, *, /]: ")
if operazione == "+":
    addizione()
elif operazione == "-":
    sottrazione()
elif operazione == "*":
    moltiplicazione()
elif operazione == "/":
    divisione()
else:
    print("Operazione non valida.")
```

== Parametri e Valori di Ritorno

Le funzioni possono però fare molto di più che raggruppare codice. Con qualche piccolo ritocco alla sintassi vista sopra, possono infatti accettare parametri in ingresso, che consentono di passare dati alla funzione al momento della chiamata, e possono restituire valori di ritorno, che le permettono di produrre risultati una volta completata la sua esecuzione.

La sintassi completa per la definizione di una funzione con parametri e valore di ritorno è la seguente:

```python
def nome_funzione(parametro1: tipo1, parametro2: tipo2, ...) -> tipo_ritorno:
    # Corpo della funzione...
    return valore_ritorno
```

dove:
- `parametro1`, `parametro2`, ... sono i nomi dei parametri che la funzione accetta in ingresso, ciascuno con il proprio tipo `tipo1`, `tipo2`, ...;
- `tipo_ritorno` è il tipo del valore che la funzione restituirà al termine della sua esecuzione;
- `return` è la parola chiave utilizzata per restituire il valore di ritorno dalla funzione (in questo caso, `valore_ritorno`).

Immaginiamo ad esempio una funzione che, dato un nome e un anno di nascita, produce una stringa con un saluto che può poi essere utilizzato a piacere dal chiamante:

```python
def presentazione(nome: str, anno_nascita: int) -> str:
    eta: int = 2025 - anno_nascita
    presentazione: str = f'''
    Ciao, il mio nome è {nome}!
    Sono nato nel {anno_nascita} e ho {eta} anni.
    '''
    return presentazione
```

Questa funzione può essere chiamata passando i parametri richiesti, e il valore di ritorno può essere catturato in una variabile per essere utilizzato successivamente:

```python
nome_utente: str = input("Inserisci il tuo nome: ")
anno_nascita_utente: int = int(input("Inserisci il tuo anno di nascita: "))
messaggio_presentazione: str = presentazione(nome_utente, anno_nascita_utente)
print(messaggio_presentazione)
```

Nota come i _parametri formali_ definiti nella funzione (`nome`, `anno_nascita`) siano distinti dai _parametri attuali_ passati durante la chiamata (`nome_utente`, `anno_nascita_utente`): i nomi utilizzati dal chiamante non hanno infatti nulla a che fare con quelli utilizzati nella definizione della funzione e Python effettuerà l'associazione in base all'ordine in cui sono elencati.

La stessa cosa vale per il valore di ritorno: il chiamante può scegliere di catturarlo in una variabile con un nome a piacere, indipendentemente da quello utilizzato all'interno della funzione, che rimane valido solo nel corpo della funzione stessa e viene distrutto al termine della sua esecuzione.

Se proprio volessimo esplicitare l'associazione tra parametri formali e attuali, tuttavia, potremmo decidere di ricorrere alla sintassi dei _parametri nominativi_ (o _keyword arguments_), che consente di specificare il nome del parametro al momento della chiamata (e quindi, potenzialmente, di variare l'ordine di passaggio):

```python
messaggio_presentazione: str = presentazione(
    nome=nome_utente,
    anno_nascita=anno_nascita_utente
)
```

== Parametri di Default

Per quanto possa essere utile esporre parametri per personalizzare il comportamento di una funzione, in alcuni casi può essere comodo fornire dei valori di default per alcuni parametri, in modo che il chiamante possa decidere se specificarli o meno, in base alle proprie esigenze.

La sintassi per definire un parametro con valore di default è la seguente:

```python
def nome_funzione(parametro1: tipo1, parametro2: tipo2 = valore_default, ...) -> tipo_ritorno:
    # Corpo della funzione...
```

dove `parametro2` ha un valore di default `valore_default` che verrà utilizzato sse il chiamante non specifica un valore per quel parametro.

Immaginiamo ad esempio una funzione che calcola l'area di un rettangolo, con la possibilità di specificare se il risultato deve essere restituito in metri quadrati o centimetri quadrati. Potremmo definire la funzione in questo modo:

```python
def area_rettangolo_conv(lunghezza: float, larghezza: float, in_centimetri: bool = False) -> float:
    area: float = lunghezza * larghezza
    if in_centimetri:
        area = area * 10000  # Converti da m² a cm²
    return area
```

== Ritornare più Valori

Una caratteristica di Python che può tornare utile in molte situazioni è la possibilità di restituire più valori da una funzione, semplicemente elencandoli separati da virgole nell'istruzione `return`.

La sintassi per restituire (e ricevere) più valori è la seguente:

```python
def nome_funzione(parametro1: tipo1, parametro2: tipo2, ...) -> tuple[tipo_ritorno1, tipo_ritorno2, ...]:
    # Corpo della funzione...
    return valore_ritorno1, valore_ritorno2, ...

risultato_1, risultato_2 = nome_funzione(argomento1, argomento2, ...)
```

Si noti come, in pratica, quello che stiamo facendo non è altro che produrre e destrutturare al volo una tupla contenente i valori di ritorno utilizzando una sintassi un po' più conveniente (cosa che in gergo tecnico si descrive come _syntactic sugar_).

Ad esempio, potremmo definire una funzione che calcola il quoziente, il quoto e il resto di una divisione intera, restituendo tutti e tre i valori al chiamante in un colpo solo:

```python
def divisione_completa(dividendo: int, divisore: int) -> tuple[float, int, int]:
    quoziente: float = dividendo / divisore
    quoto: int = dividendo // divisore
    resto: int = dividendo % divisore
    return quoziente, quoto, resto
```

Questa funzione può poi essere chiamata e i tre valori di ritorno possono essere catturati in tre variabili distinte:

```python
dividendo_utente: int = int(input("Dividendo: "))
divisore_utente: int = int(input("Divisore: "))
quoziente_utente, quoto_utente, resto_utente = divisione_completa(
    dividendo_utente, divisore_utente
)
print(f"Quoziente: {quoziente_utente}")
print(f"Quoto: {quoto_utente}")
print(f"Resto: {resto_utente}")
```

== Funzioni e Mutabilità

Un aspetto importante da considerare quando si lavora con le funzioni in Python è la distinzione tra tipi di dato mutabili e immutabili, poiché questo influisce su come i dati vengono passati alle funzioni e su come le modifiche ai parametri all'interno della funzione possono (o non possono) influenzare le variabili originali nel chiamante.

Prendiamo ad esempio una funzione che aggiunge in coda a una lista di numeri la loro somma:

```python
def aggiungi_somma(numeri: list[int]) -> list[int]:
    somma: int = sum(numeri)
    numeri.append(somma)
    return numeri
```

Richiamando alla memoria quello che sappiamo sui tipi mutabili possiamo facilmente intuire come qulunque lista venga passata alla funzione `aggiungi_somma` venga modificata direttamente:

```python
numeri_utente: list[int] = [1, 2, 3]
numeri_aggiornato: list[int] = aggiungi_somma(numeri_utente)
print(numeri_utente)  # Output: [1, 2, 3, 6]
```

Sarà quindi di fondamentale importanza tenere a mente questa distinzione quando si progettano funzioni che manipolano dati, onde evitare effetti collaterali indesiderati.

A titolo d'informazione, qualora volessimo passare alla funzione una copia di un oggetto mutabile per evitare di modificarlo, potremmo ricorrere al metodo `copy`:

```python
numeri_utente: list[int] = [1, 2, 3]
numeri_aggiornato: list[int] = aggiungi_somma(numeri_utente.copy())
print(numeri_utente)        # Output: [1, 2, 3]
print(numeri_aggiornato)    # Output: [1, 2, 3, 6]
```

#pagebreak()

= I Moduli: organizzare il codice in file

Un'ultima caratteristica fondamentale di Python che ci consente organizzare efficientemente il codice è il concetto di modulo, che permette di suddividere il codice in più file, ciascuno dei quali può contenere funzioni, variabili e, come vedremo più avanti, classi correlate tra loro.

Questa tecnica di suddivisione diventa irrinunciabile nel momento in cui si inizi a lavorare su progetti di una certa complessità, poiché consente di mantenere il codice più ordinato, leggibile e manutenibile.

== Creare e Utilizzare Moduli

A livello pratico, un modulo Python non è altro che un file con estensione `.py` contenente molteplici definizioni, realizzate esattamente come faremmo in un singolo file di codice.

Per utilizzare il codice definito in un modulo all'interno di un altro file possiamo poi utilizzare la parola chiave `import`, esattamente come in questo esempio in cui separiamo la funzione che calcola l'area di un rettangolo in un modulo chiamato `operazioni.py`:

```python
# operazioni.py
def area_rettangolo(lunghezza: float, larghezza: float) -> float:
    return lunghezza * larghezza
```

e la andiamo a utilizzare nel file principale `main.py`:

```python
# main.py
import operazioni

lunghezza_utente: float = float(input("Lunghezza del rettangolo (m): "))
larghezza_utente: float = float(input("Larghezza del rettangolo (m): "))
area: float = operazioni.area_rettangolo(lunghezza_utente, larghezza_utente)
print(f"Area del rettangolo: {area} m²")
```

Si noti come questo uso della parola chiave `import` consenta di accedere a tutte le funzioni e variabili definite nel modulo `operazioni` utilizzando la sintassi `operazioni.nome_funzione()`; se volessimo però importare solo una specifica funzione dal modulo per poi chiamarla come se fosse definita localmente, potremmo ricorrere alla sintassi `from ... import ...`:

```python
# main.py
from operazioni import area_rettangolo

lunghezza_utente: float = float(input("Lunghezza del rettangolo (m): "))
larghezza_utente: float = float(input("Larghezza del rettangolo (m): "))
area: float = area_rettangolo(lunghezza_utente, larghezza_utente)
print(f"Area del rettangolo: {area} m²")
```

== I Package: Cartelle di Moduli

Quando un progetto inizia a crescere ancora di più, può essere utile un ulteriore livello d'indirezione che ci consenta di organizzare i moduli in cartelle (dette _package_) per raggruppare logicamente molteplici file correlati tra loro.

Pensiamo ad esempio ad un progetto che offre funzioni per calcolare il perimetro e l'area di diverse forme geometriche; in tale contesto potremmo decidere di organizzare il codice in un package chiamato `geometria`, con moduli separati per ogni forma (si noti la presenza del file `__init__.py`, che indica a Python che quella cartella deve essere trattata come un package):

```
/
|- main.py
\- geometria/
 |- __init__.py
 |- rettangolo.py
 |- triangolo.py
 |- cerchio.py
```

Ognuno di questi moduli potrebbe contenere funzioni specifiche per calcolare area e perimetro della rispettiva forma:

```python
# geometria/rettangolo.py
def area(lunghezza: float, larghezza: float) -> float:
    return lunghezza * larghezza

def perimetro(lunghezza: float, larghezza: float) -> float:
    return 2 * (lunghezza + larghezza)
```

mentre il file principale `main.py` potrebbe importare e utilizzare queste funzioni in questo modo:

```python
# main.py
from geometria.rettangolo import area as area_rettangolo, perimetro as perimetro_rettangolo

lunghezza_utente: float = float(input("Lunghezza del rettangolo (m): "))
larghezza_utente: float = float(input("Larghezza del rettangolo (m): "))
area: float = area_rettangolo(lunghezza_utente, larghezza_utente)
perimetro: float = perimetro_rettangolo(lunghezza_utente, larghezza_utente)
print(f"Area del rettangolo: {area} m²")
print(f"Perimetro del rettangolo: {perimetro} m")
```

Si noti come, in questo caso, abbiamo utilizzato la sintassi `from ... import ... as ...` per rinominare le funzioni importate, in modo da evitare conflitti di nomi e rendere più chiaro il loro scopo.
