// == Imports ==

#import "../common/typst/cover.typ": handout_cover
#import "../common/typst/utils.typ": slidew, center_url


// == Setup ==

#let title = "Tipi di Dato e Controllo del Flusso"
#let course = "Python: da Zero a OOP"
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
  description: "",
  author: author, email: email
)

#set page(numbering: "1")

= Le Variabili

Come chiunque abbia avuto l'occasione di assemblare il proprio PC sicuramente saprà, uno dei componenti principali di un computer è la sua memoria di lavoro, implementata a livello hardware dai moduli RAM.

Questo spazio in cui conservare temporaneamente informazioni è a nostra disposizione quando scriviamo un programma attraverso le variabili, che possiamo vedere come piccoli contenitori dotati di nome utile a distinguerli (indirizzarli) in cui memorizzare un singolo dato di interesse che può quindi essere recuperato e riutilizzato in un secondo momento:

#align(center)[
  #image("./images/variables.png", alt: "Diagramma che mostra come valori di tipo diverso ('Riccardo', 22 e true) sono associati a variabili con nomi specifici (Nome, Età e Patante B).", width: 35%)
]

== Come si creano?

In Python, per poter utilizzare una variabile è sufficiente dichiararla e inizializzarla con un valore di partenza con la sintassi `nome_variabile: tipo = valore`:

```python
nome: str = "Riccardo"
eta: int = 22
patente_b: bool = True
```

Si noti come, al contrario di quanto mostrato nel diagramma precedente, in Python non sono ammessi spazi nei nomi delle variabili, in genere sostituiti da un underscore (`_`).

Altre limitazioni e indicazioni riguardo i nomi delle variabili includono le seguenti:

- Il nome deve iniziare con una lettera (a–z oppure A–Z) oppure con il carattere underscore:
  - Es: `_miaVariabile` va bene, `1variabile` non va bene;
  - Il fatto che inizi con underscore (es. `_nome`) è permesso; ma alcuni underscore hanno significato speciale;
- Dopo il primo carattere, il nome può contenere solo lettere, numeri e underscore. Non sono permessi spazi, trattini, simboli come `@`, `#`, `$`, `%`, `-`, `!`, etc.;
  - Esempi non validi: `my-var`, `my var`, `var$123`;
  - Le lettere possono essere sia minuscole che maiuscole;
- Il nome è case-sensitive (fa differenza tra minuscole e maiuscole); `variabile`, `Variabile`, `VARIABILE` sono tre nomi distinti;
- Non è possibile utilizzare come nome di variabile una delle parole chiave riservate di Python (i cosiddetti keywords) perché servono al linguaggio:
  - Esempi: `if`, `for`, `while`, `class`, `def`, `None`, `True`, `False`, …
  - Se provi, ottieni un errore di sintassi.

Esistono poi delle convenzioni e delle best-practice da seguire nella scelta nel nome delle variabili. Queste non sono limitazioni tecniche e non sono imposte dall'interprete, ma è buona norma rispettarle per rendere il codice leggibile ad altri programmatori:

- Evita nomi troppo lunghi ed eccessivamente “descrittivi”, fino al punto di diventare contorti:
  - Ad esempio, `data_di_nascita_del_genitore_dell_utente_minorenne` può funzionare, ma rende il codice difficile da leggere (oltre che da scrivere);
- Scegli nomi che siano significativi rispetto al contenuto che rappresentano:
  - Ad esempio, `eta` è meglio di `x` se stai memorizzando un’età;
- Non usare variabili che sovrascrivono o confondono funzioni built-in o moduli standard: anche se tecnicamente può essere permesso, è fortemente sconsigliato perché può generare confusione o errori impliciti;
- Segui uno stile coerente: ad esempio in Python è molto comune usare `snake_case` (tutto minuscolo + underscore tra le parole) per le variabili;
- Non iniziare il nome di una variabile con una lettera maiuscola, in quanto tale formattazione è tradizionalmente riservata ai nomi delle classi (che vedremo più avanti).

== Come si utilizzano?

Una volta create, le variabili possono essere utilizzate all'interno del codice semplicemente invocandole con il loro nome. Ad esempio, per stampare a schermo il nome dell'utente salvato in username:

```python
username: str = "rsacchetto"
print(username)
```

Per aggiornarle, invece, è sufficiente assegnare un nuovo valore con la stessa modalità della dichiarazione iniziale (con l'unica differenza che non è più necessario specificare il tipo):

```python
nome: str = "Riccardo"
print(nome)
nome = "Riccardo Sacchetto"
print(nome)
```

#pagebreak()

= I Tipi di Dato

Ogni variabile in Python (e in virtualmente tutti i linguaggi di programmazione) è associata a un tipo di dato, che ne definisce la natura e le operazioni che possono essere eseguite su di essa.

Come accennavamo in fase d'introduzione, Python è un linguaggio fortemente tipizzato, il che significa che ogni variabile ha un tipo specifico che non può essere cambiato arbitrariamente durante l'esecuzione del programma. Per questo motivo, è fondamentale conoscere i vari tipi di dato disponibili in Python per poterli utilizzare correttamente.

== I Numeri

Elemento alla base del funzionamento stesso dei computer, i numeri (e l'aritmetica) sono uno degli aspetti fondamentali di qualunque linguaggio di programmazione.

Normalmente, in informatica, i numeri si dividono in due grandi categorie: i numeri interi (integer) e i numeri razionali (floating point, a virgola mobile), utilizzati dal programmatore in base alle necessità specifiche del contesto.

In Python, in realtà, disponiamo di tre diversi tipi di numero: gli interi e i razionali, rappresentati dai tipi `int` e `float`, e i complessi, rappresentati dal tipo `complex`:

```python
intero: int = 5
reale: float = 2.5
complesso: complex = complex(5, 2.5) # 5+2.5j
```

Per tutti questi, Python mette a disposizione le classiche operazioni aritmetiche, `+`, `-`, `*`, `/`, che possono essere utilizzate sia tra numeri dello stesso tipo che tra numeri di tipi diversi (in quest'ultimo caso Python esegue una conversione implicita al tipo più “grande”):

```python
print(intero - 1)         # 4
print(intero / intero)    # 1.0
print(intero * reale)     # 12.5
print(intero + complesso) # 10+2.5j
```

Si noti che, a causa della rappresentazione interna dei numeri a virgola mobile e a proprietà intrinseche della codifica binaria, alcune operazioni possono produrre risultati leggermente imprecisi; si provi ad esempio a mandare in esecuzione i seguenti calcoli:

```python
print(0.1 + 0.2)
print(3 * 0.1)
```

A tal proposito, per chi fosse interessato ad approfondire la rappresentazione dei numeri in un formato che preservi la precisione richiesta da una calcolatrice, si consiglia la lettura di A. Popovitch, "The Impossible Calculator": https://asteriskmag.com/issues/10/the-impossible-calculator.

== Le Stringhe

Apparentemente banali a un primo sguardo, le stringhe sono uno dei tipi di dato fondamentali in ogni programma Python, indispensabili nell'input/output e nella rappresentazione di qualunque tipo di informazione testuale.

Internamente, le stringhe non sono altro che una sequenza di caratteri concatenati per formare un qualche tipo di messaggio.

=== Rappresentazione

In Python, tutto quello che si trova tra singoli e doppi apici è considerato una stringa:

```python
"Ciao, come va?"
'Io tutto bene, grazie. E tu?'
```

Questo torna particolarmente utile quando è necessario utilizzare uno di questi due caratteri all'interno della stringa stessa:

```python
"Lo sapevi che ho iniziato a studiare il linguaggio 'Python'?"
'Ieri è uscito un nuovo episodio di "The Pitt"!'
```

In ogni caso, è sempre possibile inserirli sfruttando il carattere di escape, il backslash (`\`), utile anche a rappresentare il line feed:

```python
"Ieri è uscito un nuovo episodio di \"The Pitt\"!"
'Cosa stai guardando in questi giorni?\nI nuovi episodi di "The Pitt"!'
```

=== Operazioni sulle stringhe

Una delle operazioni più comuni sulle stringhe è la concatenazione, ovvero l'accostamento di due o più stringhe una dopo l'altra:

```python
message: str = "Hello" + " " + "World"
print(message)
```

Ovviamente funzionante anche tra variabili:

```python
greeting: str = "Hello"
target: str = "World"
print(greeting + " " + target)
```

Altre operazioni spesso molto utili in contesti pratici sono:

- Il cambio del casing:

  ```python
  nome: str = "riccardo sacchetto"
  nome = nome.title()
  print(nome)            # Riccardo Sacchetto
  print(nome.lower())    # riccardo sacchetto
  print(nome.upper())    # RICCARDO SACCHETTO
  ```

- La pulizia di spazi all'inizio e alla fine della stringa (stripping):

  ```python
  linguaggio: str = "  python  "
  print(linguaggio.rstrip())    # "  python"
  print(linguaggio.lstrip())    # "python  "
  print(linguaggio.strip())     # "python"
  ```

- Rimozione di prefissi e suffissi:

  ```python
  its: str = "https://itsdigitalacademy.com"
  print(its.removeprefix("https://"))    # itsdigitalacademy.com
  print(its.removesuffix(".com"))         # https://itsdigitalacademy
  ```

Si noti come ognuna di queste operazioni non muti la stringa originale, ma produca una nuova stringa che può essere salvata in una nuova variabile o utilizzata per sovrascrivere il vecchio valore (ma sempre esplicitamente).

=== Format strings

Spesso può essere utile formare delle stringhe partendo da dati contenuti in diverse variabili, ad esempio per mostrare il risultato di un calcolo.

Un primo approccio potrebbe essere la concatenazione, che però risulta problematica per valori che non sono stringhe; se provassimo a eseguire:

```python
eta: int = 2025 - 2003
output: str = "Sono Riccardo e ho " + eta + " anni"
print(output)
```

otterremmo infatti il seguente errore:

```
File "/path/to/examples.py", line 2, in <module>
  output = "Sono Riccardo e ho " + eta + " anni"
           ~~~~~~~~~~~~~~~~~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str
```

che ci comunica come Python non sia in grado di concatenare un numero a delle stringhe.

Ora, sicuramente è possibile convertire il numero in stringa prima di procedere con la concatenazione:

```python
eta: int = 2025 - 2003
output: str = "Sono Riccardo e ho " + str(eta) + " anni"
print(output)
```

Tuttavia, esiste un metodo ancora più pratico, le format strings:

```python
eta: int = 2025 - 2003
output: str = f"Sono Riccardo e ho {eta} anni"
print(output)
```

Tutte le stringhe precedute da una `f` dispongono infatti della capacità di ospitare template, ovvero coppie di parentesi graffe il cui contenuto viene elaborato come codice Python, trasformato in stringa e inserito nel testo finale.

=== Lettura da Riga di Comando

Una stringa può poi essere letta da riga di comando, offrendoci la possibilità di interagire con l'utente del programma. Ad esempio, se volessimo chiedergli il nome, potremmo fare così:

```python
print("Come ti chiami?")
nome: str = input("Nome: ")
print(f"Ciao, {nome}!")
```

== I Booleani

Formalizzata da George Boole nel 1854, l'algebra booleana è la base matematica che consente ai computer di prendere decisioni; come vedremo fra poco, infatti, manipolare valori di verità risulta fondamentale per il controllo del flusso di un programma, permettendo di eseguire determinate operazioni solo se certe condizioni sono soddisfatte.

In Python, i valori booleani sono rappresentati dal tipo `bool`, che può assumere solo due valori: `True` (vero) e `False` (falso):

```python
sta_piovendo: bool = True
ombrello_aperto: bool = False
```

I valori booleani possono essere combinati e manipolati attraverso gli operatori logici - `and`, `or` e `not` - definiti sulla base di tabelle di verità:

```
| A       | B       | A and B | A or B | not A |
|---------|---------|---------|--------|-------|
| True    | True    | True    | True   | False |
| True    | False   | False   | True   | False |
| False   | True    | False   | True   | True  |
| False   | False   | False   | False  | True  |
```

Questi ci permettono di costruire espressioni complesse che valutano a `True` o `False`, utili a derivare nuove informazioni logiche a partire da quelle già note:

```python
mi_bagno: bool = sta_piovendo and not ombrello_aperto # True
```

I booleani possono poi essere ottenuti come risultato di confronti tra valori di altri tipi di dato mediante gli operatori di confronto (`==`, `!=`, `<`, `<=`, `>`, `>=`):

```python
eta: int = 2025 - 2003
maggiore_eta: int = 18
posso_bere: bool = eta >= maggiore_eta # True
```

#pagebreak()

= Controllo del Flusso

Fin'ora abbiamo visto come creare e utilizzare variabili di diversi tipi di dato in Python, posizionando le nostre istruzioni in ordine sequenziale. Tuttavia, per scrivere programmi utili e interessanti, è fondamentale poter controllare il flusso di esecuzione del codice in base a determinate condizioni.

In questa sezione esploreremo le strutture di controllo del flusso più comuni in Python: le istruzioni condizionali (`if`, `elif`, `else`) e i cicli (`for`, `while`).

== If/elif/else

Le istruzioni condizionali permettono di eseguire blocchi di codice sse certe condizioni sono soddisfatte. Un esempio immediato di utilizzo di un'istruzione condizionale in Python è il seguente:

```python
if sta_piovendo and not ombrello_aperto:
  print("Mi bagno!")
else:
  print("Resto asciutto!")
```

L'istruzione `if` valuta la condizione; se questa risulta vera (`True`), esegue il blocco di codice associato (contraddistinto dall'essere indentato sotto la condizione stessa). Se invece è falsa (`False`) viene eseguito il blocco di codice sotto l'istruzione `else`.

Se avessimo la necessità di verificare altre condizioni qualora la prima risulti falsa, possiamo poi utilizzare l'istruzione `elif` (abbreviazione di "else if"):

```python
if eta < maggiore_eta:
  print("Sei minorenne, non puoi bere!")
elif eta == maggiore_eta:
  print("Sei appena maggiorenne, bevi con moderazione!")
else:
  print("Sei maggiorenne, puoi bere liberamente!")
```

Si noti come ogni ramo di codice è mutualmente esclusivo: non appena una condizione risulta soddisfatta, l'interprete inizia ad eseguire il codice all'interno del blocco relativo per poi saltare immediatamente alla fine dell'intero costrutto condizionale. Se si volesse dunque avere la possibilità di eseguire anche gli altri rami qualora più condizioni siano verificate simultaneamente, si dovrebbe utilizzare una serie di istruzioni `if` indipendenti:

```python
if sta_piovendo:
  print("Oggi non è una bella giornata...")
if eta >= 18:
  print("Puoi bere liberamente!")
```

= I Cicli

Mentre gli statement condizionali ci permettono di eseguire blocchi di codice in modo selettivo, i cicli ci consentono di ripetere l'esecuzione di un blocco di codice più volte, fino a quando una certa condizione non viene soddisfatta.

== Il Ciclo While

Nella teoria dei linguaggi di programmazione il ciclo `while` è il ciclo più "potente", in quanto ci permette di ripetere un blocco di codice fintantochè una qualunque condizione da noi fissata risulta vera, permettendoci di eseguire la stessa operazione un numero a priori indefinito di volte.

Un esempio di base del ciclo `while` in Python potrebbe essere il seguente:

```python
energia: int = 100
while energia != 0:
  print("Sono carico! Continuiamo a studiare Python!")
  energia = energia - 1
print("Ora sono stanco...")
```

In questo esempio, il ciclo `while` continua a eseguire il blocco di codice al suo interno finché la variabile `energia` non raggiunge il valore 0; ad ogni iterazione, viene stampato un messaggio e la variabile `energia` viene decrementata di 1; alla fine, quando `energia` è uguale a 0, il ciclo termina e viene stampato un messaggio finale.

Si noti come nella testa del ciclo non esista un vincolo particolare su ciò che deve accadere a `energia`: se a fronte di una qualche particolare condizione, magari dipendente da variabili esterne al contesto immediato, dovessimo decidere di sommare `10` a `energia`, potremmo aumentare in ogni istante il numero d'iterazioni da eseguire, possibilmente generando un loop infinito:

```python
energia: int = 100
while energia != 0:
  print("Sono carico! Continuiamo a studiare Python!")
  if energia <= 50 and abbiamo_caffe:
    abbiamo_caffe = False
    energia = energia + 10
  else:
    energia = energia - 1
print("Ora sono stanco...")
```

== Il Ciclo For

Al contrario di quanto accade con il ciclo `while`, il ciclo `for` itera su una sequenza di elementi ben definita al suo avvio, eseguendo il blocco di codice per ogni elemento che vi appartiene.

Ad esempio, potremmo decidere di utilizzare un ciclo `for` per stampare ogni numero da 0 a 9:

```python
for num in range(0, 10):
  print(num)
```

Si noti come in questo caso la variabile `num` venga valorizzata da Python iterazione per iterazione utilizzando gli elementi del range specificato all'inizio del ciclo (e non modificabile durante la sua esecuzione).

I range di numeri non sono poi l'unica sequenza su cui è possibile iterare con un ciclo `for`: possiamo infatti fare la stessa operazione anche sulle stringhe e, come vedremo più avanti, su liste e dizionari:

```python
for char in "Ciao!":
  print(char)
```
