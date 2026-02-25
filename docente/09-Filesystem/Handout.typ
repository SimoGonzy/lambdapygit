// == Imports ==

#import "@preview/wrap-it:0.1.1": wrap-content

#import "../common/typst/cover.typ": handout_cover
#import "../common/typst/utils.typ": slidew, center_url


// == Setup ==

#let title = "Lavorare con il filesystem"
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

= Memoria a lungo termine

Immaginiamo di aver scritto un programma per gestire la nostra finanza personale, ovvero un piccolo software in grado di tenere traccia delle nostre entrate e uscite di denaro: applicando quanto visto finora dovremmo essere in grado di rappresentare nel modo più opportuno le nostre transazioni economiche, magari creando una classe `Transazione` con gli attributi `importo`, `data` e `categoria` e una classe `Portafoglio` in grado di contenere una lista di transazioni e di calcolare il saldo attuale:

```python
class Transazione:
    def __init__(self, importo: float, data: str, categoria: str):
        self.importo: float = importo
        self.data: str = data
        self.categoria: str = categoria

class Portafoglio:
    def __init__(self):
        self.transazioni: list[Transazione] = []

    def aggiungi_transazione(self, transazione: Transazione):
        self.transazioni.append(transazione)

    def calcola_saldo(self) -> float:
        return sum([ t.importo for t in self.transazioni ])

portafoglio: Portafoglio = Portafoglio()
while True:
    print(f"Saldo attuale: {portafoglio.calcola_saldo()}€")

    continua: str = input("Vuoi aggiungere una nuova transazione? (S/n) ").strip().lower()
    if continua == "n":
        break

    importo: float = float(input(
        "Inserisci l'importo della transazione (positivo per entrate, negativo per uscite): "
    ))
    data: str = input("Inserisci la data della transazione (YYYY-MM-DD): ")
    categoria: str = input("Inserisci la categoria della transazione: ")
    portafoglio.aggiungi_transazione(Transazione(importo, data, categoria))
```

Tuttavia, un problema emerge non appena iniziamo a utilizzare seriamente il nostro programma: ogni volta che finiremo di utilizzarlo e procederemo a terminarlo, tutte le informazioni sulle transazioni vengono perse e alla successiva esecuzione dovremo ricominciare da capo con un portafoglio vuoto.

Questo accade perché, come abbiamo visto, le variabili e gli oggetti che creiamo in Python vengono memorizzati nella RAM, una memoria *volatile* che viene cancellata ogni volta che il programma termina la sua esecuzione, rendendola inadatta a conservare dati che vogliamo preservare tra una sessione e l'altra.

Per risolvere questo problema abbiamo quindi bisogno di un modo per salvare i dati in una memoria *persistente*, ovvero una memoria che conserva le informazioni anche quando il programma non è in esecuzione. In informatica, questo tipo di memoria è rappresentato dal filesystem del computer, ovvero l'insieme di file e cartelle memorizzati su un disco rigido o un'unità a stato solido.

#pagebreak()

= Leggere dati da un file CSV

Il metodo più comune per memorizzare lo stato di un programma è quindi quello di ricorrere a un file esterno, in cui scrivere i dati che vogliamo preservare. Visto però che i dati dovranno essere letti e compresi dal nostro programma, non possiamo disporli a casaccio, ma dobbiamo organizzarli in un formato strutturato e standardizzato per assicurarci che possano essere interpretati correttamente.

Uno dei formati più semplici e diffusi per memorizzare dati tabellari è il formato CSV (Comma-Separated Values), in cui ogni riga del file rappresenta un record (\~ istanza di classe) e i campi all'interno di ogni riga sono separati da virgole (\~ attributi); ed esempio, per memorizzare le transazioni del nostro portafoglio potremmo utilizzare un file `transazioni.csv` con il seguente contenuto:

```csv
importo,data,categoria
1000.0,2024-01-15,Stipendio
-50.0,2024-01-16,Spesa alimentare
-20.0,2024-01-17,Trasporti
```

Nota come la prima riga del file (header) venga dedicata alla memorizzazione dei nomi dei campi, che ci serviranno in seguito per associare correttamente i valori agli attributi della nostra classe `Transazione`.

A questo punto, non ci resta che scrivere un piccolo codice in grado di leggere il file riga per riga, di suddividere ogni riga nei suoi campi e di creare un'istanza di `Transazione` per ogni riga, in modo da popolare il nostro `Portafoglio` con le transazioni salvate nel file.

Iniziamo con un approccio molto semplice, evitando per ora di sfruttare tecniche OOP e inserendo il seguente snippet tra la definizione delle classi `Transazione` e `Portafoglio` e la parte di codice che richiede l'inserimento:

```python
# --snip--
portafoglio: Portafoglio = Portafoglio()

file: Path = Path("transazioni.csv")
with file.open("r", encoding="utf-8") as transazioni:
    next(transazioni)  # Salta l'header
    for riga in transazioni:
        campi: list[str] = riga.strip().split(",")  # Estrai i singoli campi del record

        importo: float = float(campi[0])
        data: str = campi[1]
        categoria: str = campi[2]
        portafoglio.aggiungi_transazione(
            Transazione(importo, data, categoria)
        )

while True:
    print(f"Saldo attuale: {portafoglio.calcola_saldo()}€")
    # --snip--
```

Proviamo a commentare quello che accade in queste righe di codice:

1. Per prima cosa creiamo un oggetto `Path` (offerto dalla libreria `pathlib`) che punta al file `transazioni.csv` e lo apriamo in modalità lettura (`"r"`) con codifica UTF-8; si noti l'uso della sintassi `with`, che ci permette di aprire il file in modo sicuro, assicurandoci che venga chiuso automaticamente al termine dell'operazione (ovvero al termine del blocco indentato) onde evitare che rimanga aperto inutilmente;
2. Utilizziamo la funzione `next()` per saltare la prima riga del file, che contiene l'header con i nomi dei campi e non una transazione vera e propria: possiamo infatti vedere l'oggetto `transazioni` come un iteratore che restituisce una riga del file alla volta e di cui possiamo scartare il primo elemento;
3. Iteriamo quindi sulle righe rimanenti del file, rappresentando ciascuna riga come una stringa di testo che andiamo a "ripulire" dai caratteri di newline e da eventuali spazi bianchi con il metodo `strip()` (cfr. lezione 01) e a suddividere nei singoli campi utilizzando il metodo `split(",")`, che restituisce una lista delle stringhe presenti tra una virgola e l'altra;
4. A questo punto, possiamo estrarre i singoli campi dalla lista `campi`, convertire il campo `importo` in un numero decimale di tipo `float` e creare una nuova istanza di `Transazione` con i valori estratti, che andiamo ad aggiungere al nostro `Portafoglio`.

Il risultato è ovviamente che, all'avvio del programma, il nostro portafoglio verrà popolato con le transazioni salvate nel file `transazioni.csv`, permettendoci di visualizzare il saldo attuale e di aggiungere nuove transazioni senza perdere le informazioni precedenti, ottenendo essenzialmente un metodo per "recuperare" i dati da una sessione precedente.

#pagebreak()

= Scrivere dati su un file CSV

Naturalmente, per rendere il nostro programma veramente utile, dobbiamo anche essere in grado di salvare nel file `transazioni.csv` le nuove transazioni che andiamo ad aggiungere nel corso della sessione in modo che siano disponibili alla successiva esecuzione del programma.

Per fare ciò, dobbiamo aprire il file in modalità scrittura (`"w"`) o in modalità append (`"a"`) - a seconda che vogliamo sovrascrivere il contenuto esistente o aggiungere nuove righe alla fine del file - e scriverci i dati formattati correttamente. In questo caso, visto che ogni volta abbiamo a disposizione nel nostro `Portafoglio` l'elenco completo delle transazioni, possiamo aprire il file in modalità scrittura e riscrivere tutte le transazioni al termine della sessione, ovvero immediatamente dopo il ciclo `while True`:

```python
# --snip--
with file.open("w", encoding="utf-8") as transazioni:
    transazioni.write("importo,data,categoria\n")  # Scriviamo l'header
    for t in portafoglio.transazioni:
        transazioni.write(f"{t.importo},{t.data},{t.categoria}\n")
```

Commentiamo anche questo blocco di codice:

1. Apriamo il file `transazioni.csv` in modalità scrittura (`"w"`) con codifica UTF-8, utilizzando nuovamente la sintassi `with` per assicurarci che il file venga chiuso automaticamente al termine dell'operazione;
2. Scriviamo la prima riga del file, ovvero l'header con i nomi dei campi, utilizzando il metodo `write()`;
3. Iteriamo quindi sulla lista delle transazioni presenti nel nostro `Portafoglio` e per ciascuna transazione scriviamo una riga nel file formattata correttamente secondo le regole previste dal formato CSV, separando quindi i campi con delle virgole e terminando ogni riga con un carattere di newline (`\n`).

A questo punto, il nostro programma è completo e in grado di leggere e scrivere le transazioni del nostro portafoglio su un file CSV, permettendoci di preservare interamente i dati tra una sessione e l'altra.

#pagebreak()

= L'approccio OOP: serializzazione e deserializzazione

Il codice che abbiamo scritto finora funziona correttamente, ma presenta alcuni limiti legati al fatto che la logica di lettura e scrittura dei dati è stata inserita direttamente nel flusso principale del programma, rendendo il codice meno leggibile e più difficile da mantenere, sopratutto se in futuro volessimo inserire più tipi di transazione (e.g., spese in negozio, bonifici, prestiti, etc.) rappresentati da specifiche sottoclassi di `Transazione` e composti da attributi differenti.

Per risolvere questo problema, possiamo sfruttare i concetti di serializzazione e deserializzazione, ovvero dotare i nostri oggetti della capacità di "convertirsi" in una rappresentazione testuale (serializzazione) e di "ricostruirsi" a partire da una rappresentazione testuale (deserializzazione).

== Serializzazione

Partiamo con la serializzazione, ovvero con la capacità di un oggetto di trasformarsi in una stringa formattata secondo le regole del formato CSV. Per fare ciò, non dobbiamo far altro che aggiungere un metodo `to_csv()` alla nostra classe `Transazione`, assicurandoci banalmente che produca una stringa con i campi separati da virgole:

```python
class Transazione:
    # --snip--
    def to_csv(self) -> str:
        return f"{self.importo},{self.data},{self.categoria}"
```

Questo metodo, come abbiamo visto nella lezione precedente, potrà eventualmente essere sovrascritto dalle sottoclassi di `Transazione` per adattare la formattazione alle specifiche esigenze di ciascun tipo di transazione.

A questo punto, non ci resta che aggiungere il metodo `to_csv` anche alla nostra classe `Portafoglio`, in modo da poter serializzare l'intero elenco di transazioni in un'unica chiamata:

```python
class Portafoglio:
    # --snip--
    def to_csv(self) -> str:
        righe: list[str] = [ "importo,data,categoria" ]  # Header
        for t in self.transazioni:
            righe.append(t.to_csv())
        return "\n".join(righe)
```

Questo codice, semplicemente, andrà a creare una lista di stringhe partendo dall'header e aggiungendo la rappresentazione CSV di ciascuna transazione, per poi restituire l'intera lista unita in un'unica stringa con i caratteri di newline utilizzati come separatore.

A questo punto, possiamo riscrivere il blocco di codice che salva le transazioni su file in modo molto più conciso:

```python
with file.open("w", encoding="utf-8") as transazioni:
    transazioni.write(portafoglio.to_csv())
```

Decisamente più leggibile!

== Deserializzazione

Per parlare della deserializzazione, ovvero della capacità di un oggetto di ricostruirsi a partire da una rappresentazione testuale, dobbiamo invece fermarci un istante per introdurre il concetto di *metodo di classe* (class method). Visto infatti che la deserializzazione non riguarda un'istanza esistente di una classe, ma la creazione di una nuova istanza a partire da una stringa di testo, non possiamo utilizzare un normale metodo di istanza (definito con `def` e operante su `self`), ma dobbiamo definire un metodo che appartenga alla classe stessa.

In Python, i metodi di classe vengono definiti utilizzando il decoratore `@classmethod` e prendono come primo argomento la classe stessa (convenzionalmente chiamata `cls`) invece dell'istanza. Ad esempio, potremmo creare un metodo di classe all'interno di `Transazione` che, dato un mese e un anno, crea la trazione del deposito dello stipendio:

```python
class Transazione:
    # --snip--
    @classmethod
    def deposito_stipendio(cls, mese: int, anno: int) -> Transazione:
        # Supponiamo che lo stipendio venga sempre depositato
        # il 25 del mese e ammonti a 1000€
        data: str = f"{anno:04d}-{mese:02d}-25"
        return cls(1_000, data, "Stipendio")
```

Questo metodo di classe può essere chiamato direttamente sulla classe `Transazione` senza bisogno di un'istanza, e restituirà una nuova istanza di `Transazione` con i valori predefiniti:

```python
transazione_stipendio: Transazione = Transazione.deposito_stipendio(12, 2025)
print(transazione_stipendio.to_csv())  # Output: 1000,2025-12-25,Stipendio
```

A questo punto, possiamo utilizzare questa tecnica per aggiungere un metodo di classe `from_csv()` alla nostra classe `Transazione` che prenda in input una stringa formattata secondo le regole del formato CSV e restituisca una nuova istanza di `Transazione`, costruita esattamente con lo stesso metodo utilizzato nel nostro codice di lettura del file:

```python
class Transazione:
    # --snip--
    @classmethod
    def from_csv(cls, csv_string: str) -> Transazione:
        campi: list[str] = csv_string.strip().split(",")

        importo: float = float(campi[0])
        data: str = campi[1]
        categoria: str = campi[2]
        return cls(importo, data, categoria)
```

Ovviamente, questo può essere fatto anche per la classe `Portafoglio`, creando un metodo di classe `from_csv()` che prenda in input una stringa contenente più righe CSV e restituisca una nuova istanza di `Portafoglio` popolata con le transazioni deserializzate:

```python
class Portafoglio:
    # --snip--
    @classmethod
    def from_csv(cls, csv_string: str) -> Portafoglio:
        portafoglio: Portafoglio = cls()
        righe: list[str] = csv_string.strip().split("\n")
        for riga in righe[1:]:  # Salta l'header considerando le righe successive alla prima
            transazione: Transazione = Transazione.from_csv(riga)
            portafoglio.aggiungi_transazione(transazione)
        return portafoglio
```

Con questo metodo, possiamo riscrivere il blocco di codice che legge le transazioni dal file in modo molto più conciso:

```python
with file.open("r", encoding="utf-8") as transazioni:
    contenuto: str = transazioni.read()
    portafoglio: Portafoglio = Portafoglio.from_csv(contenuto)
```

#pagebreak()

= Altre operazioni su file e cartelle

Finora abbiamo visto come leggere e scrivere dati su file, ma in molti casi potremmo aver bisogno di effettuare operazioni come spostamenti e copie o semplicmente lavorare con intere directory, ad esempio per elaborare in batch più file di dati o per organizzare i file generati dal nostro programma; in ogni caso, la classe `Path` ci mette a disposizione dei metodi utili a svolgere le operazioni principali.

Ad esempio, per elencare tutti i file presenti in una cartella possiamo utilizzare il metodo `iterdir()` dell'oggetto `Path` che rappresenta la cartella per ottenere un iteratore sui file e le sottocartelle in essa contenuti:

```python
cartella: Path = Path("dati")
for file in cartella.iterdir():
    print(file.name)
```

Nota che `file` è anch'esso un oggetto `Path` e possiamo quindi utilizzare i suoi metodi per ottenere informazioni sul file (come il nome (`name`), l'estensione (`suffix`) e la dimensione (`stat().st_size`)) o per eseguire operazioni su di esso (come la lettura o la scrittura viste in precedenza).

Per creare una nuova cartella, possiamo utilizzare il metodo `mkdir()`:

```python
nuova_cartella: Path = Path("output")
nuova_cartella.mkdir(exist_ok=True)  # exist_ok evita l'errore se la cartella esiste già
```

Per spostare o rinominare un file, possiamo utilizzare il metodo `rename()`:

```python
file_originale: Path = Path("dati/vecchio_nome.txt")
file_rinominato: Path = Path("dati/nuovo_nome.txt")
file_originale.rename(file_rinominato)
```

mentre per compiarlo possiamo utilizzare il metodo `copy`:

```python
file_sorgente: Path = Path("dati/file.txt")
file_destinazione: Path = Path("backup/file_copia.txt")
file_sorgente.copy(file_destinazione)
```

Infine, per eliminare un file o una cartella, possiamo utilizzare rispettivamente i metodi `unlink()` e `rmdir()`:

```python
file_da_eliminare: Path = Path("dati/file_da_eliminare.txt")
file_da_eliminare.unlink()  # Elimina il file

cartella_da_eliminare: Path = Path("dati/cartella_da_eliminare")
cartella_da_eliminare.rmdir()  # Elimina la cartella (deve essere vuota)
```

Per maggiori informazioni su queste e altre operazioni sul filesystem, ovviamente, è possibile fare riferimento alla documentazione ufficiale della libreria `pathlib` all'indirizzo https://docs.python.org/3/library/pathlib.html
