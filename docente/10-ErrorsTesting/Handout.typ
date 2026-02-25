// == Imports ==

#import "@preview/wrap-it:0.1.1": wrap-content

#import "../common/typst/cover.typ": handout_cover
#import "../common/typst/utils.typ": slidew, center_url


// == Setup ==

#let title = "Gestione degli Errori e Testing"
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

= Anche il codice è fallibile

Come sarà sicuramente stato possibile notare nel corso dello svolgimento delle eserictazioni del corso e, più in generale, durante lo sviluppo di qualsiasi progetto software, l'esecuzione di un programma può andare incontro a situazioni impreviste che producono errori di varia natura.

Spesso, tali errori sono dovuti a una semplice svista del programmatore, come ad esempio un errore di battitura nel nome di una variabile, ma in altri casi possono essere causati da situazioni più complesse e talvolta impossibili da prevedere, come la ricezione di un dato non valido o la mancanza di una risora esterna come un file o un host remoto.

In tali casi, non essendo possibile rimuovere con certezza assoluta la fonte del "problema" - ovvero la causa dell'errore - è fondamentale che il programmatore sia in grado di gestire tali situazioni in modo appropriato, evitando che l'intero programma vada in crash o produca risultati errati, tentando di recuperare il controllo del flusso di esecuzione o, in alternativa, segnalando in modo chiaro e preciso l'errore verificatosi.

Immaginiamo il semplice caso di un file di configurazione che il nostro programma deve leggere all'avvio per poter funzionare correttamente: se tale file non fosse presente, il programma dovrebbe essere in grado di gestire questa situazione, magari creando un file di configurazione di default o avvisando l'utente della mancanza del file in modo chiaro prima di terminare l'esecuzione.

#pagebreak()

= Rappresentazione degli errori

A oggi, l'unico caso di "situazione inaspettata" che abbiamo avuto occasione di rappresentare in Python è stato quello relativo alla mancanza di un valore, modellata attraverso il valore speciale `None`.

Immaginiamo ad esempio una funzione che deve restituire la media di uno studente; se questi non ha ancora sostenuto esami, la funzione potrebbe restituire `None` per indicare l'assenza di un valore valido:

```python
class Studente:
    def __init__(self, nome: str):
        self.nome: str = nome
        self.voti: list[int] = []

    def aggiungi_voto(self, voto: int):
        self.voti.append(voto)

    def media(self) -> int:
        if not self.voti:
            return None  # Nessun voto disponibile
        return sum(self.voti) // len(self.voti)
```

Questo approccio è indubbiamente corretto in questa situazione, in quanto ci permette di prevenire un crash del programma nel caso in cui si tenti di calcolare la media di uno studente senza voti (causato dal tentativo di divisione per zero), ma presenta comunque alcuni limiti:

1. *Ambiguità*: L'uso di `None`, in generale, può essere ambiguo, in quanto non distingue tra "nessun valore" e "errore nell'esecuzione della funzione". In situazioni più complesse, potrebbe essere difficile capire se `None` indica un'assenza di dati o un errore;
2. *Necessità di controlli espliciti*: Ogni volta che si chiama la funzione `media`, è necessario effettuare un controllo esplicito per verificare se il valore restituito è `None`, altrimenti si rischia di incorrere in errori successivi quando si tenta di utilizzare il valore restituito; immaginiamo una funzione che fa uso della media per decidere se uno studente è promosso o bocciato:
    ```python
    class Studente:
      # --snip--
      def verifica_promozione(self) -> str:
        if self.media() >= 6:
          return "Promosso"
        else:
          return "Bocciato"

    mario = Studente("Mario Rossi")
    print(mario.verifica_promozione())
    ```
    In questo caso il programma andrebbe in errore, in quanto si sta tentando di confrontare `None` con un numero intero:
    ```
    TypeError: '>=' not supported between instances of 'NoneType' and 'int'
    ```
3. *Difficoltà di debug*: Quando si verifica un errore, l'uso di `None` non fornisce informazioni dettagliate sul tipo di errore o sulla sua origine, rendendo più difficile il debug del codice.

Proprio per superare questi limiti, Python offre un meccanismo più robusto per la gestione degli errori: le eccezioni. Organizzate in classi, le eccezioni consentono di rappresentare in modo chiaro e strutturato le situazioni di errore, consentendo al programmatore di gestirle in modo appropriato attraverso costrutti specifici del linguaggio qualora lo ritenga appropriato o di ignorarle del tutto lasciando che il programma termini l'esecuzione.

L'eccezione più generica in Python è rappresentata dalla classe `Exception`, dalla quale derivano tutte le altre eccezioni predefinite del linguaggio, come ad esempio `ValueError`, `TypeError` e `FileNotFoundError`; possiamo istanziarla per rappresentare un errore generico nel nostro codice così come istanzaimo qualunque altra classe:

```python
class Studente:
    # --snip--
    def media(self) -> int:
        if not self.voti:
          errore = Exception()
        return sum(self.voti) // len(self.voti)
```

In questo caso, ovviamente, non stiamo facendo nulla di utile con l'istanza di `Exception` creata, quindi dobbiamo fare in modo di "inviarla" al chiamante per segnalare che si è verificato un errore. Al contrario di quanto accade con valori di ritorno e con `None`, in questo caso non possiamo semplicemente restituire l'istanza dell'eccezione, ma dobbiamo "lanciarla" utilizzando la parola chiave `raise`:

```python
class Studente:
  # --snip--
  def media(self) -> int:
    if not self.voti:
      errore = Exception()
      raise errore
    return sum(self.voti) // len(self.voti)
```

In questo modo, quando la funzione `media` viene chiamata e si verifica la condizione di errore, l'eccezione viene "lanciata" e il flusso di esecuzione del programma viene interrotto, passando il controllo al chiamante. Se il chiamante non gestisce l'eccezione con le modalità che vedremo fra poco, Python provvederà a terminare l'esecuzione e stampare un messaggio di errore che include il tipo di eccezione e lo stack trace.

```python
mario: Studente = Studente("Mario Rossi")
print(mario.media())
```

```
Traceback (most recent call last):
  File "/home/rsacchetto/lambdapygit/docente/10-ErrorsTesting/examples.py", line 41, in <module>
    print(mario.media())
          ~~~~~~~~~~~^^
  File "/home/rsacchetto/lambdapygit/docente/10-ErrorsTesting/examples.py", line 37, in media
    raise Exception()
Exception
```

In questo modo, anche se ovviamente non eliminiamo al 100% la necessità di inserire controlli espliciti nel codice, otteniamo comunque un meccanismo che ci consente di fallire nel momento più corretto (la media non può essere calcolata perchè la media di 0 voti non può esistere, la divisione per 0 è solo una conseguenza).

Si noti tuttavia che non abbiamo risolto il problema dell'ambiguità: l'eccezione `Exception` è molto generica e non fornisce informazioni specifiche sul tipo di errore che si è verificato. Per questo motivo, è buona pratica utilizzare eccezioni più specifiche o creare proprie classi di eccezioni personalizzate per rappresentare situazioni di errore particolari nel proprio codice; ad esempio, potremmo definire una classe di eccezione personalizzata chiamata `NessunVotoError` per rappresentare il caso in cui si tenta di calcolare la media di uno studente senza voti:

```python
class NessunVotoError(Exception):
  pass

class Studente:
  # --snip--
  def media(self) -> int:
    if not self.voti:
      raise NessunVotoError()
    return sum(self.voti) // len(self.voti)

mario: Studente = Studente("Mario Rossi")
print(mario.media())
```

```
Traceback (most recent call last):
  File "/home/rsacchetto/lambdapygit/docente/10-ErrorsTesting/examples.py", line 41, in <module>
    print(mario.media())
          ~~~~~~~~~~~^^
  File "/home/rsacchetto/lambdapygit/docente/10-ErrorsTesting/examples.py", line 37, in media
    raise NessunVotoError()
NessunVotoError
```

Le exceptions, tra l'altro, possono anche accettare argomenti nel loro costruttore per fornire ulteriori dettagli sull'errore verificatosi, come ad esempio un messaggio di errore descrittivo:

```python
class NessunVotoError(Exception):
  pass

class Studente:
  # --snip--
  def media(self) -> int:
    if not self.voti:
      raise NessunVotoError(f"{self.nome} non ha voti registrati.")
    return sum(self.voti) // len(self.voti)
```

```
Traceback (most recent call last):
  File "/home/rsacchetto/lambdapygit/docente/10-ErrorsTesting/examples.py", line 41, in <module>
    print(mario.media())
          ~~~~~~~~~~~^^
  File "/home/rsacchetto/lambdapygit/docente/10-ErrorsTesting/examples.py", line 37, in media
    raise NessunVotoError(f"{self.nome} non ha voti registrati.")
NessunVotoError: Mario Rossi non ha voti registrati.
```

Questo, trattandosi di un argomento opzionale del costruttore della classe `Exception`, è una funzionalità disponibile per tutte le eccezioni in Python, incluse quelle predefinite. Naturalmente, nel pieno stile dell'ereditarietà, è possibile estendere classi di eccezioni predefinite per creare eccezioni personalizzate utili a facilitarci la vita in casi specifici; ad esempio, se volessimo fare in modo che `NessunVotoError` prendesse semplicemente in input l'istanza di studente su cui il problema si è verificato e si occupasse da sola di costruire il messaggio di errore, potremmo fare così:

```python
class NessunVotoError(Exception):
  def __init__(self, studente: Studente):
    super().__init__(f"{studente.nome} non ha voti registrati.")

class Studente:
  # --snip--
  def media(self) -> int:
    if not self.voti:
      raise NessunVotoError(self)
    return sum(self.voti) // len(self.voti)
```

In questo modo, il codice che utilizza la nostra eccezione personalizzata risulta più pulito e facile da leggere, in quanto non è necessario preoccuparsi di costruire manualmente il messaggio di errore ogni volta che si lancia l'eccezione.

#pagebreak()

= Gestione delle eccezioni

Ora che abbiamo visto come rappresentare e lanciare eccezioni in Python, vediamo come gestirle in modo appropriato nel nostro codice. Nota che tutto quello che vedremo in questo capitolo non si applica esclusivamente alle eccezioni che lanciamo manualmente con `raise`, ma a tutti i casi di codice che può fallire (come la divisione per zero).

Il costrutto principale per la gestione delle eccezioni in Python è rappresentato dalle parole chiave `try` e `except`. Il codice che potrebbe generare un'eccezione viene racchiuso all'interno di un blocco `try`, mentre il codice che gestisce l'eccezione viene inserito all'interno di uno o più blocchi `except` in cui viene specificato il tipo di eccezione da gestire:

```python
class Studente:
  # --snip--
  def verifica_promozione(self) -> str:
    try:
      if self.media() >= 6:
        return "Promosso"
      else:
        return "Bocciato"
    except NessunVotoError as e:
      return f"Impossibile verificare la promozione: {e}"
```

Nota come all'interno di `try` abbiamo scritto la logica del programma così come ce la aspettavamo: se la media è maggiore o uguale a 6, lo studente è promosso; altrimenti, è bocciato. Tuttavia, nel caso in cui si verifichi un'eccezione di tipo `NessunVotoError` durante l'esecuzione del blocco `try`, il flusso di esecuzione viene interrotto e il controllo passa al blocco `except`, dove possiamo gestire l'errore in modo appropriato; in questo particolare caso, ad esempio, restituiamo un messaggio che indica che non è possibile verificare la promozione a causa della mancanza di voti.

Inoltre, notiamo che all'interno del blocco `except` abbiamo utilizzato la sintassi `as e` per catturare l'istanza dell'eccezione lanciata, in modo da poterla aggiungere alla stringa ritornata per arricchire il contesto.

Come accennavamo poco fa, tuttavia, i blocchi `except` possono essere multipli, in modo da gestire in modo differente i vari tipi di eccezioni che potrebbero essere lanciate all'interno del blocco `try`. Immaginiamo ad esempio il caso in cui la funzione `media` provi a leggere i voti dello studente da un file con il suo nome che funge da database:

```python
class Studente:
  # --snip--
  def media(self) -> int:
    voti: list[int] = []
    file_voti: Path = Path(f"{self.nome}_voti.txt")
    with file_voti.open("r") as f:
      for line in f:
        voti.append(int(line.strip()))
    if not voti:
      return sum(voti) // len(voti)
```

In questo caso non solo dobbiamo gestire il caso in cui lo studente non ha voti registrati, ma anche il caso in cui il file non esiste o non è accessibile. Possiamo fare ciò aggiungendo un ulteriore blocco `except` per gestire l'eccezione `FileNotFoundError`:

```python
class Studente:
  # --snip--
  def verifica_promozione(self) -> str:
    try:
      if self.media() >= 6:
        return "Promosso"
      else:
        return "Bocciato"
    except NessunVotoError as e:
      return f"Impossibile verificare la promozione: {e}"
    except FileNotFoundError as e:
      return f"Impossibile verificare la promozione: il file dei voti non esiste."
```

In alternativa, possiamo anche gestire tutte le possibile eccezioni in un unico blocco `except` omettendo di specificare il tipo di eccezione:

```python
class Studente:
  # --snip--
  def verifica_promozione(self) -> str:
    try:
      if self.media() >= 6:
        return "Promosso"
      else:
        return "Bocciato"
    except Exception as e:
      return f"Impossibile verificare la promozione: {e}"
```

In questo caso, ovviamente, rinunciamo alla specificità della gestione delle eccezioni, ma in situazioni in cui non è necessario distinguere tra i vari tipi di errori per recuperare il controllo dell'esecuzione, questa può essere una soluzione più semplice e concisa.

#pagebreak()

= Unit testing con PyTest

Se gli errori sono una costante inevitabile per tutti i programmatori, un buon modo per mitigare il loro impatto è sicuramente rappresentato dai test automatici, ovvero da piccoli programmi che verificano in modo automatico che il codice scritto si comporti come previsto in una serie di scenari predefiniti, in modo da assicurarsi che le funzionalità implementate funzionino correttamente e che eventuali modifiche future non introducano regressioni o bug.

Per iniziare, è innanzitutto fondamentale assicurarsi di avere installato pytest, il framework di testing che utilizzeremo per scrivere e eseguire i nostri test automatici; per farlo, possiamo semplicemente ricorrere a `pip` inserendo il seguente comando nel terminale:

```bash
python -m pip install --user pytest
```

A questo punto, assumendo di avere a disposizione in un file `studente.py` l'ultima versione senza lettura da file della classe `Studente` e dell'eccezione `NessunVotoError` viste in precedenza:

```python
class NessunVotoError(Exception):
  def __init__(self, studente: Studente):
    super().__init__(f"{studente.nome} non ha voti registrati.")

class Studente:
  def __init__(self, nome):
    self.nome = nome
    self.voti = []

  def aggiungi_voto(self, voto):
    self.voti.append(voto)

  def media(self) -> int:
    if not self.voti:
      raise NessunVotoError(self)
    return sum(self.voti) // len(self.voti)

  def verifica_promozione(self) -> str:
    try:
      if self.media() >= 6:
        return "Promosso"
      else:
        return "Bocciato"
    except NessunVotoError as e:
      return f"Impossibile verificare la promozione: {e}"
```

dovremo occuparci dei seguenti test case necessari per assicurarci che il codice si comporti come previsto:
- Verificare che la media di uno studente con voti sia calcolata correttamente;
- Verificare che la media di uno studente senza voti lanci l'eccezione `NessunVotoError`;
- Verificare che la promozione di uno studente con media sufficiente ritorni "Promosso";
- Verificare che la promozione di uno studente con media insufficiente ritorni "Bocciato";
- Verificare che la promozione di uno studente senza voti ritorni il messaggio di errore corretto.

Iniziamo con il primo caso, creando un nuovo file chiamato `test_studente.py` e definendo una funzione di test per verificare il calcolo della media:

```python
from studente import Studente, NessunVotoError
import pytest

def test_media_con_voti():
    studente = Studente("Mario Rossi")
    studente.aggiungi_voto(8)
    studente.aggiungi_voto(6)
    studente.aggiungi_voto(7)
    assert studente.media() == 7
```

In questa funzione, non dobbiamo fare altro che creare un'istanza di `Studente`, aggiungervi alcuni voti e utilizzare l'istruzione `assert` per verificare che la media calcolata sia quella che ci aspettiamo: se la condizione dell'`assert` è vera, il test passerà indicando che il codice si comporta esattamente come ci aspettimo; altrimenti, fallirà inducendo pytest a segnalarci un problema.

Per provare a lanciare il test, possiamo semplicemente eseguire il comando `pytest test_studente.py` nel terminale all'interno della cartella in cui si trovano i file `studente.py` e `test_studente.py`: se tutto funziona correttamente, dovremmo vedere un output simile al seguente:

```
=== test session starts ===
platform linux -- Python 3.13.9, pytest-8.4.2, pluggy-1.6.0
rootdir: /home/rsacchetto/lambdapygit
collected 1 item

docente/10-ErrorsTesting/examples/examples_tests.py .         [100%]

=== 1 passed in 0.03s ===
```

Come è possibile dedurre da queste righe, il test è passato con successo, indicando che la funzione `media` si comporta correttamente quando lo studente ha voti registrati. Passiamo ora al secondo caso, ovvero verificare che la media di uno studente senza voti lanci l'eccezione `NessunVotoError`:

```python
def test_media_senza_voti():
    studente = Studente("Luigi Bianchi")
    with pytest.raises(NessunVotoError):
        studente.media()
```

Nota che in questo caso, un po' come in un `try/catch`, utilizziamo il costrutto `with pytest.raises(...)` per indicare che ci aspettiamo che il codice all'interno del blocco generi un'eccezione di tipo `NessunVotoError`: se l'eccezione viene effettivamente lanciata, il test passerà, altrimenti fallirà.

Per quanto riguarda infine il testing della funzione `verifica_promozione`, possiamo definire i seguenti test case molto simili tra loro:

```python
def test_verifica_promozione_promosso():
    studente = Studente("Anna Verdi")
    studente.aggiungi_voto(7)
    studente.aggiungi_voto(8)
    assert studente.verifica_promozione() == "Promosso"

def test_verifica_promozione_bocciato():
    studente = Studente("Carlo Neri")
    studente.aggiungi_voto(4)
    studente.aggiungi_voto(5)
    assert studente.verifica_promozione() == "Bocciato"

def test_verifica_promozione_senza_voti():
    studente = Studente("Elena Gialli")
    assert studente.verifica_promozione()
        == "Impossibile verificare la promozione: Elena Gialli non ha voti registrati."
```

In questi casi, infatti, non dobbiamo preoccuparci di gestire eccezioni, in quanto la funzione `verifica_promozione` si occupa già di farlo internamente; possiamo quindi semplicemente utilizzare gli `assert` per verificare che il valore ritornato sia quello che ci aspettiamo in ciascuno scenario.

Di nuovo, se eseguiamo `pytest test_studente.py` dovremmo vedere un output simile al seguente, che indica che tutti e 5 i test configurati sono passati con successo:

```
=== test session starts ===
platform linux -- Python 3.13.9, pytest-8.4.2, pluggy-1.6.0
rootdir: /home/rsacchetto/lambdapygit
collected 5 items

docente/10-ErrorsTesting/examples/examples_tests.py .....         [100%]

=== 5 passed in 0.01s ===
```

Se, tuttavia, apportassimo una modifica al codice per introdurre un bug (come, ad esempio, cambiando la formula della media in `sum(self.voti) + 1 // len(self.voti)`) potremmo apprezzare uno scenario simile al seguente:

```
=== test session starts ===
platform linux -- Python 3.13.9, pytest-8.4.2, pluggy-1.6.0
rootdir: /home/rsacchetto/lambdapygit
collected 5 items

docente/10-ErrorsTesting/examples/examples_tests.py F..F.         [100%]

=== FAILURES ===
___ test_media_con_voti ___

    def test_media_con_voti():
        studente = Studente("Mario Rossi")
        studente.aggiungi_voto(8)
        studente.aggiungi_voto(6)
        studente.aggiungi_voto(7)
>       assert studente.media() == 7
E       assert 21 == 7
E        +  where 21 = media()
E        +    where media = <examples04.Studente object at 0x7ff0d52a3110>.media

docente/10-ErrorsTesting/examples/examples_tests.py:10: AssertionError
___ test_verifica_promozione_bocciato ___

    def test_verifica_promozione_bocciato():
        studente = Studente("Carlo Neri")
        studente.aggiungi_voto(4)
        studente.aggiungi_voto(5)
>       assert studente.verifica_promozione() == "Bocciato"
E       AssertionError: assert 'Promosso' == 'Bocciato'
E
E         - Bocciato
E         + Promosso

docente/10-ErrorsTesting/examples/examples_tests.py:27: AssertionError
=== short test summary info ===
FAILED docente/10-ErrorsTesting/examples/examples_tests.py::test_media_con_voti - assert 21 == 7
FAILED docente/10-ErrorsTesting/examples/examples_tests.py::test_verifica_promozione_bocciato - AssertionError: assert 'Promosso' == 'Bocciato'

=== 2 failed, 3 passed in 0.05s ===
```

In questo caso, pytest ci segnalerà che due dei test definiti sono falliti, fornendoci informazioni dettagliate su quali test non sono passati, sul motivo del fallimento e sui valori trovati ai due capi dell'`assert`, in modo da poter provare ad individuare e correggere il bug introdotto.

A proposito di assert, comunque, si noti che in Python esistono diverse varienti di questa istruzione, utili a valutare diversi tipi di proprietà che ci aspettiamo essere valide per il nostro codice:

#align(center)[
  #table(
    columns: (1fr, 1fr),
    stroke: (x, y) => if y == 0 {
      (bottom: 0.7pt + black)
    },
    table.header(
      [ Assertion ], [ Significato ]
    ),
    [ `assert a == b` ], [ Verifica che `a` sia uguale a `b` ] ,
    [ `assert a != b` ], [ Verifica che `a` sia diverso da `b` ] ,
    [ `assert a` ], [ Verifica che `a` sia vero ] ,
    [ `assert not a` ], [ Verifica che `a` sia falso ] ,
    [ `assert a in b` ], [ Verifica che `a` sia contenuto nella lista `b` ] ,
    [ `assert a not in b` ], [ Verifica che `a` non sia contenuto nella lista `b` ] ,
  )
]
