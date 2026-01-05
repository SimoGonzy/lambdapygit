// == Imports ==

#import "@preview/wrap-it:0.1.1": wrap-content

#import "../common/typst/cover.typ": handout_cover
#import "../common/typst/utils.typ": slidew, center_url


// == Setup ==

#let title = "Introduzione alle Classi"
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

= Un codice orientato ai dati

Con l'introduzione di strutture dati e di funzioni, siamo ora in grado di scrivere programmi in grado di eseguire operazioni anche complesse su insiemi di dati correlati tra loro; prendiamo ad esempio il seguente codice:

```python
def mostra_eta(utente: dict[str, str | int]):
  eta = 2025 - utente["anno_nascita"]
  print(f"{utente['nome']} ha {eta} anni")

utente = {
  "nome": "Riccardo",
  "anno_nascita": 2003
}
mostra_eta(utente)  # "Riccardo ha 22 anni"
```

Rispolverando quanto visto in precedenza, possiamo notare che viene definita una funzione `mostra_eta` che prende in input un dizionario rappresentante un utente (dotato di nome e anno di nascita), ne computa l'età e mostra a schermo un messaggio che mostra il valore calcolato; ma cosa accadrebbe se alla funzione `mostra_eta` venisse passato un dizionario diverso da quello che si aspetta?

```python
auto = {
  "modello": "Lancia Ypsilon",
  "immatricolazione": 2005
}
mostra_eta(auto)
```

In questo caso, al contrario di quanto si verificherebbe con una funzione che accetta un `int` ma riceve una `str`, il type checker non è in grado di rilevare che abbiamo passato un input errato, in quanto il tipo `dict[str, str | int]` è corretto anche per il dizionario che rappresenta l'automobile; il risultato è che, durante l'esecuzione del programma, si verificherà un errore dovuto alla mancanza delle chiavi `nome` e `anno_nascita` all'interno del dizionario `auto` (`KeyError`).

Per evitare questo tipo di problemi, sarebbe utile poter definire dei tipi di dato personalizzati che rappresentino in modo più preciso le strutture dati che andiamo a utilizzare all'interno del nostro programma; in questo modo, potremmo definire un tipo `Utente` che rappresenti esattamente la struttura dati che ci aspettiamo, e il type checker sarebbe in grado di rilevare eventuali errori di tipo durante la fase di analisi statica del codice.

#pagebreak()

= Tipi personalizzati: le Classi

Ecco quindi che entrano a gamba tesa le Classi: introdotte per la prima volta negli anni '60 con il linguaggio di programmazione Simula, le classi sono dei costrutti che permettono di definire nuovi tipi di dato personalizzati con una struttura ben definita (attributi) e delle operazioni associate (metodi).

Iniziamo subito da un esempio pratico costruendo una classe `Utente` che rappresenti una persona con nome e anno di nascita e che includa un metodo per mostrarne l'età:

```python
class Utente:
  def __init__(self, nome: str, anno_nascita: int):
    self.nome: str = nome
    self.anno_nascita: int = anno_nascita

  def mostra_eta(self):
    eta = 2025 - self.anno_nascita
    print(f"{self.nome} ha {eta} anni")

utente = Utente("Riccardo", 2003)
utente.mostra_eta()  # "Riccardo ha 22 anni"
```

In questo esempio definiamo, mediante la parola chiave `class`, una nuova classe chiamata `Utente`; questa, dal nostro punto di vista, non rappresenta altro che un nuovo tipo di dato che possiamo utilizzare all'interno del nostro programma, utile a rappresentare - appunto - un certo utente con le sue caratteristiche.

All'interno della classe abbiamo quindi definito due funzioni un po' particolari, una di nome `__init__` e l'altra di nome `mostra_eta`. Queste, per quanto ad un primo sguardo appaiano simili a delle normali funzioni, sono in realtà dei metodi, ovvero delle procedure che possono essere eseguite solo prendendo in input un _oggetto_ di tipo `Utente`.

Analizziamoli partendo da `mostra_eta`, il più intuitivo dei due: proprio come la funzione `mostra_eta` vista in precedenza, questo metodo calcola l'età dell'utente e mostra a schermo un messaggio con il risultato; la differenza sta nel fatto che, essendo un metodo della classe `Utente`, invece di ricevere un generico parametro riceve una variabile speciale `self`, ovvero un riferimento che può puntare *esclusivamente* ad un oggetto di tipo `Utente` e che viene valorizzato con l'istanza su cui il metodo viene invocato.

Per l'invocazione, in particolare, guardiamo l'ultima riga dell'esempio, ove questa avviene: `utente.mostra_eta()`. Qui, il metodo `mostra_eta` viene invocato sull'oggetto `utente` mediante la dot-syntax (`.`); in questo modo, Python sa che il parametro `self` all'interno del metodo deve essere valorizzato con l'oggetto `utente`, permettendoci così di eseguire il codice che ci interessa.

#wrap-content(
  align: top + right,
  image("./images/objects.png", alt: "Diagramma che mostra come un oggetto contenga degli attributi come se fossero variabili", width: 100pt),
  [
    #set par(justify: true)

    Un oggetto, in effetti, può essere visto come un contenitore che racchiude al suo interno delle variabili e dei metodi che possono essere recuperati utilizzando la dot-syntax (e.g., `utente.nome`) e che sono definti sulla base della _classe_ a cui questo oggetto appartiene; in questo modo, essendo che i vari metodi che sono pensati per essere utilizzati con un certo tipo di oggetto sono presenti esclusivamente "al suo interno", non è possibile scrivere del codice che tenti di utilizzare un metodo su un oggetto di tipo errato, evitando così sul nascere errori di tipo durante l'esecuzione del programma.

    Per quanto riguarda invece `__init__`, questo è un metodo speciale chiamato _costruttore_ che viene eseguito automaticamente ogni volta che viene creato un nuovo oggetto di tipo `Utente`; il suo scopo è quello di inizializzare l'oggetto appena creato, valorizzando in qualche modo gli attributi al suo interno (in questo caso, `nome` e `anno_nascita` vengono entrambi presi come parametri e memorizzati all'interno del nuovo oggetto).
  ]
)

Si noti come anche `__init__` riceva come primo parametro `self`, che in questo caso fa riferimento all'oggetto `Utente` che si sta creando. Quando si genera un nuovo oggetto, infatti, Python alloca lo spazio necessario in memoria per poi chiamare automaticamente il costruttore in modo da consentire l'inizializzazione dell'oggetto appena creato, passando come primo parametro un riferimento ad esso.

#pagebreak()

= Oggetti con uno stato

Alla pari di strutture dati come liste e dizionari, anche un oggetto è trattato da Python come una entità mutabile e può quindi contenere al suo interno uno stato che può essere modificato nel corso dell'esecuzione del programma.

Prendiamo ad esempio una classe `Studente` dotata di una matricola e di una lista di voti:

```python
class Studente:
  def __init__(self, matricola: str):
    self.matricola: str = matricola
    self.voti: list[int] = []
```

Questa rappresentazione potrebbe essere utilizzata per modellare il sistema di gestione delle carriere di una università, dove ogni studente è identificato da una matricola e possiede una lista di voti ottenuti negli esami sostenuti in cui è possibile aggiungere nuovi voti nel corso del tempo:

```python
def aggiungi_voto(self, voto: int):
  self.voti.append(voto)
```

e che può essere utilizzata per calcolare la media dei risultati ottenuti:

```python
def media_voti(self) -> float:
  return sum(self.voti) / len(self.voti)
```

Non è difficile immaginare come una simile struttura possa essere utilizzata in un contesto reale per tenere traccia dei voti degli studenti e calcolare le loro medie in modo semplice, efficiente ed incredibilmente intuitivo:

```python
studente = Studente("VR123456")

studente.aggiungi_voto(28)
studente.aggiungi_voto(30)
print(studente.media_voti())  # 29.0
```

I metodi possono poi essere chiamarsi a vicenda per realizzare operazioni più complesse, come ad esempio il calcolo della media aritmetica di laurea:

```python
def media_laurea(self) -> float:
  media = self.media_voti()
  return media * 110 / 30
```

#pagebreak()

= Incapsulamento: oggetti come piccole black box

Oltre a rendere il codice che scriviamo più vicino al modello mentale con cui pensiamo ai dati, classi e oggetti ci permettono di incapsulare al loro interno lo stato e il comportamento degli oggetti che rappresentano, nascondendo i dettagli implementativi e fornendo un'interfaccia chiara e semplice per interagire con essi.

Immaginiamo ad esempio di star scrivendo un software che deve essere in grado di svolgere calcoli matematici, con alcune funzioni che necessitano di misure in metri e altre in chilometri; per evitare di dover continuamente convertire le misure tra le due unità di misura, potremmo definire una classe `Misura` che rappresenti una misura in metri e che includa dei metodi per convertire la misura in chilometri e viceversa:

```python
class Misura:
  def __init__(self, metri: float):
    self.metri: float = metri

  def in_metri(self) -> float:
    return self.metri

  def in_chilometri(self) -> float:
    return self.metri / 1000
```

In questo modo, possiamo creare oggetti di tipo `Misura` e utilizzare i metodi forniti per ottenere la misura nella unità di misura desiderata, senza doverci preoccupare di come avviene la conversione:

```python
def calcola_area_stanza(lunghezza: Misura, larghezza: Misura) -> float:
  return lunghezza.in_metri() * larghezza.in_metri()

def calcola_tempo_viaggio(distanza: Misura) -> float:
  distanza_km = distanza.in_chilometri()
  velocita = 130  # km/h
  return distanza_km / velocita

stanza = calcola_area_stanza(Misura(5), Misura(3))
vrsud_valdagno = calcola_tempo_viaggio(Misura(55_000))
print(stanza)           # 15.0
print(vrsud_valdagno)   # 0.42...
```

#pagebreak()

= Magic Methods

Per quanto utili a raggruppare informazioni che rappresentano un certo concetto, gli oggetti hanno una limitazione apparente se confrontati con le strutture dati built-in come liste e dizionari: non possiamo stampare a video le istanze per visualizzarne al volo i contenuti, in quanto la `print` non fa altro che restituire un output criptico:

```python
studente = Studente("VR123456")
print(studente)     # "<__main__.Studente object at 0x7fcb0164f620>"
```

Questo accade perché, di default, Python non sa come rappresentare a schermo un oggetto di tipo `Studente` e quindi si limita a mostrare il tipo dell'oggetto e il suo indirizzo in memoria.

Fortunatamente, oltre ai metodi che definiamo esplicitamente all'interno delle nostre classi, Python permette di definire una serie di metodi speciali, chiamati _magic methods_ o _dunder methods_ (dalla contrazione di "double underscore"), che permettono di definire il comportamento degli oggetti in determinate situazioni, tra cui la conversione in stringa.

Uno di questi è il metodo `__str__`, che viene chiamato automaticamente ogni volta che un oggetto deve essere convertito in una stringa, ad esempio quando viene passato alla funzione `print`; definendolo all'interno della nostra classe `Studente`, possiamo personalizzare l'output mostrato a schermo:

```python
class Studente:
  # --snip--
  def __str__(self) -> str:
    return f"Studente(matricola={self.matricola}, voti={self.voti})"

studente = Studente("VR123456")
print(studente)     # "Studente(matricola=VR123456, voti=[])"
```

In questo modo, quando invochiamo `print(studente)`, Python chiama automaticamente il metodo `__str__` dell'oggetto `studente` e mostra a schermo la stringa restituita da questo metodo, permettendoci così di visualizzare in modo chiaro e leggibile le informazioni contenute nell'oggetto.

`__str__` non è però l'unico magic method disponibile: esistono infatti molti altri metodi speciali che permettono di definire il comportamento degli oggetti in situazioni diverse, come ad esempio `__add__` per la somma di due oggetti, `__len__` per ottenere la lunghezza di un oggetto, e molti altri ancora.

Torniamo ad esempio al caso della classe `Misura`, e immaginiamo di voler sommare due misure insieme; non essendo le variabili di tipo `Misura` supportate dall'operatore `+` di default, otterremmo un errore se provassimo a farlo:

```python
m1 = Misura(500)
m2 = Misura(300)
m3 = m1 + m2  # TypeError: unsupported operand type(s) for +: 'Misura' and 'Misura'
```

Per risolvere questo problema e ottenere la somma di due Misure, potremmo quindi definire il metodo `__add__` all'interno della classe in modo da specificare come devono essere sommate due istanze di `Misura`:

```python
class Misura:
  # --snip--
  def __add__(self, other: Misura) -> Misura:
    return Misura(self.metri + other.metri)

m1 = Misura(500)
m2 = Misura(300)
m3 = m1 + m2  # Misura con 800 metri
print(m3.in_chilometri())  # 0.8
```

Con questa definizione, qualora utilizzassimo l'operatore `+` tra due oggetti di tipo `Misura`, Python chiamerà automaticamente il metodo `__add__` del primo oggetto, passando come parametro il secondo oggetto; in questo modo, possiamo ottenere una nuova istanza di `Misura` che rappresenta la somma delle due misure.

Stesso discorso vale per gli operatori di confronto. Ad esempio, un problema molto comune è quello di voler confrontare due oggetti per verificarne l'uguaglianza; senza una definizione esplicita, Python confronterà gli indirizzi in memoria degli oggetti, portando a risultati inattesi:

```python
m1 = Misura(500)
m2 = Misura(500)
print(m1 == m2)  # False
```

Per risolvere questo problema, possiamo definire il metodo `__eq__` all'interno della classe `Misura` per specificare come devono essere confrontate due istanze di `Misura`:

```python
class Misura:
  # --snip--
  def __eq__(self, other: object) -> bool:
    return type(other) is Misura and self.metri == other.metri

m1 = Misura(500)
m2 = Misura(500)
print(m1 == m2)  # True
```

Si noti come il tipo del parametro `other` sia `object`, in quanto il metodo `__eq__` può essere chiamato con qualsiasi tipo di oggetto; all'interno del metodo, quindi, verifichiamo prima che `other` sia effettivamente di tipo `Misura` prima di procedere al confronto degli attributi interni.
