// == Imports ==

#import "@preview/wrap-it:0.1.1": wrap-content

#import "../common/typst/cover.typ": handout_cover
#import "../common/typst/utils.typ": slidew, center_url


// == Setup ==

#let title = "Gerarchia delle Classi & Polimorfismo"
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

= Una gerarchia logica

Se le classi che abbiamo visto nella scorsa lezione ci consentono di rappresentare i dati in un formato quanto più vicino possibile al mondo reale, spesso può capitare che alcune entità condividano delle caratteristiche comuni pur rimanendo concettualmente distinte, rendendo così la modellazione più complessa.

Prendiamo per esempio una società che si occupa di noleggio di veicoli e deve dunque gestire flotte composte sia da Autovetture che da Autocarri; come il lettore potrà facilmente intuire, entrambi i tipi di veicoli condividono alcune caratteristiche comuni (es. targa, marca, modello, anno di immatricolazione) che potrebbero spingerci a rappresentarli con un'unica definizione di classe, ma hanno anche delle differenze (es. capacità di carico, numero di posti a sedere, ecc.) che potrebbero portarci a pensare che la soluzione corretta sia creare una classe distinta per ogni tipo di mezzo.

Proviamo ad adottare entrambe le soluzioni e vediamo quali problemi emergono in ciascun caso.

== Soluzione 1: una sola classe per tutti i tipi di veicolo

In questo primo approccio, definiamo una singola classe `Veicolo` che rappresenta sia le Autovetture che gli Autocarri, includendo tutti gli attributi necessari per entrambi i tipi di veicoli:

```python
class Veicolo:
    def __init__(
        self, targa: str, marca: str, modello: str, anno: int,
        capacita_carico: Optional[int] = None, posti_a_sedere: Optional[int] = None
    ) -> None:
        self.targa: str = targa
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno
        self.capacita_carico: Optional[int] = capacita_carico
        self.posti_a_sedere: Optional[int] = posti_a_sedere
```

Con questa definizione, possiamo creare istanze di `Veicolo` per rappresentare sia autovetture che autocarri, ma ci troviamo a dover gestire attributi che non sono rilevanti per entrambi i tipi di veicoli (es. una autovettura non ha una capacità di carico significativa, mentre un autocarro non ha posti a sedere) e che, non essendo sempre inizializzati, potrebbero causare problemi inaspettati.

Immaginiamo per esempio di dover definire un metodo che verifichi se un veicolo può trasportare un certo carico; con questa struttura, dovremmo includere controlli aggiuntivi per gestire i casi in cui l'attributo `capacita_carico` non è pertinente, andando a perdere chiarezza e semplicità nel codice:

```python
def puo_trasportare(self, peso: int) -> bool:
    if self.capacita_carico is None:
        return False
    return peso <= self.capacita_carico
```

== Soluzione 2: classi distinte per ogni tipo di veicolo

Proviamo ora a definire due classi separate, `Autovettura` e `Autocarro`, ognuna con i propri attributi specifici:

```python
class Autovettura:
    def __init__(
        self, targa: str, marca: str, modello: str, anno: int, posti_a_sedere: int
    ):
        self.targa: str = targa
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno
        self.posti_a_sedere: int = posti_a_sedere

class Autocarro:
    def __init__(
        self, targa: str, marca: str, modello: str, anno: int, capacita_carico: int
    ):
        self.targa: str = targa
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno
        self.capacita_carico: int = capacita_carico
```

Con questa struttura ogni classe è sicuramente più chiara e specifica e può ospitare i propri metodi specifici (come `puo_trasportare`) senza influenzare l'altra, ma si nota subito come una montagna di codice finisca per essere duplicato, introducendo problemi di leggibilità e di manutenzione di eventuali metodi che dovranno essere inseriti in entrambe le classi.

Prendiamo per esempio il caso in cui si renda necessario consentire di calcolare l'età di un veicolo; per farlo, dovremmo implementare lo stesso metodo due volte, aumentando il rischio di errori e incongruenze:

```python
def eta(self, anno_corrente: int) -> int:
    return anno_corrente - self.anno
```

== Una soluzione migliore: l'ereditarietà

Proviamo quindi a prendere il meglio di entrambi gli approcci, creando innanzitutto una classe base `Veicolo` che contenga gli attributi e i metodi comuni a tutti i veicoli, rinunciando (temporaneamente) a quelli specifici di ogni tipo:

```python
class Veicolo:
    def __init__(self, targa: str, marca: str, modello: str, anno: int):
        self.targa: str = targa
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno

    def eta(self, anno_corrente: int) -> int:
        return anno_corrente - self.anno
```

In questo modo, abbiamo creato una rappresentazione chiara e concisa dei veicoli in generale, evitando duplicazioni di codice ed escludendo gli attributi che non sono rilevanti per tutti i tipi di veicoli; a questo punto, un primo tentativo di estendere questa classe per rappresentare Autovetture e Autocarri potrebbe essere il seguente, incapsulando un'istanza di `Veicolo` all'interno delle classi specifiche:

```python
class Autovettura:
    def __init__(self, targa: str, marca: str, modello: str, anno: int, posti_a_sedere: int):
        self.veicolo: Veicolo = Veicolo(targa, marca, modello, anno)
        self.posti_a_sedere: int = posti_a_sedere

class Autocarro:
    def __init__(self, targa: str, marca: str, modello: str, anno: int, capacita_carico: int):
        self.veicolo: Veicolo = Veicolo(targa, marca, modello, anno)
        self.capacita_carico: int = capacita_carico

    def puo_trasportare(self, peso: int) -> bool:
        return peso <= self.capacita_carico
```

In questo modo, `Autovettura` e `Autocarro` condividono il codice comune definito in `Veicolo`, mentre mantengono i propri attributi e metodi specifici, andando essenzialmente a definire una gerarchia logica tra le classi dove `Veicolo` funge da classe base e le altre due da classi derivate, le quali possono essere viste come specializzazioni della classe `Veicolo`:

#align(center)[
  #image("./images/gerarchiaVeicoli.png", alt: "Diagramma che illustra la gerarchia tra i diversi tipi di veicoli", width: 200pt),
]

Sebbene questa soluzione funzioni, consentendoci di scrivere una sola volta tutto il codice condiviso e di assicurarci che quello specifico sia applicabile solo nei casi in cui è rilevante, si nota subito come l'accesso agli attributi e ai metodi della classe `Veicolo` risulti più macchinoso, richiedendo di passare attraverso l'istanza incapsulata; ad esempio, per ottenere l'età di un'`Autovettura`, dovremmo scrivere:

```python
auto: Autovettura = Autovettura("AB123CD", "Lancia", "Ypsilon", 2005, 4)
print(auto.veicolo.eta(2025))   # 20
```

Fortunatamente, al contrario di altri linguaggi di programmazione in cui l'incapsulamento è l'unico modo per ottenere gerarchie simili, Python ci offre un meccanismo più elegante e potente per definire relazioni di tipo base-specalizzatore tra classi: l'estensione.

Per estendere una classe in Python è sufficiente specificare la classe base tra parentesi dopo il nome della classe derivata; in questo modo, la classe derivata erediterà automaticamente tutti gli attributi e i metodi della classe base, consentendoci di accedervi direttamente senza dover incapsulare manualmente un'istanza; ecco quindi come possiamo riscrivere le classi `Autovettura` e `Autocarro` utilizzando l'estensione:

```python
class Autovettura(Veicolo):
    def __init__(self, targa: str, marca: str, modello: str, anno: int, posti_a_sedere: int):
        super().__init__(targa, marca, modello, anno)
        self.posti_a_sedere: int = posti_a_sedere

class Autocarro(Veicolo):
    def __init__(self, targa: str, marca: str, modello: str, anno: int, capacita_carico: int):
        super().__init__(targa, marca, modello, anno)
        self.capacita_carico: int = capacita_carico

    def puo_trasportare(self, peso: int) -> bool:
        return peso <= self.capacita_carico
```

Si noti come, seppur non ci sia un attributo `veicolo` all'interno delle classi derivate, i due costruttori siano molto simili a quelli precedenti, con la differenza che ora possiamo chiamare il costruttore della classe base `Veicolo` utilizzando la funzione `super()`, che ci consente di accedere ai metodi della classe base senza dover specificare esplicitamente il nome della classe.

Con questa nuova struttura, possiamo ora creare istanze di `Autovettura` e `Autocarro` e accedere direttamente ai metodi ereditati dalla classe `Veicolo`, come mostrato di seguito:

```python
auto: Autovettura = Autovettura("AB123CD", "Lancia", "Ypsilon", 2005, 4)
print(auto.eta(2025))   # 20
```

#pagebreak()

= Override dei metodi

Un altro aspetto importante dell'ereditarietà è la possibilità di sovrascrivere (override) i metodi ereditati dalla classe base all'interno delle classi derivate, consentendoci di personalizzare il comportamento di tali metodi in base alle esigenze specifiche della classe derivata.

Immaginiamo ad esempio il caso del calcolo della tassa di circolazione, che potrebbe avere una cifra base per tutti i veicoli e prevedere una maggiorazione per gli autocarri in base alla loro capacità di carico.

Per implementare questo comportamento, possiamo definire un metodo `tassa_circolazione` nella classe base `Veicolo` e poi sovrascriverlo nella classe `Autocarro` per includere la logica specifica:

```python
class Veicolo:
    # --snip--
    def tassa_circolazione(self) -> float:
        return 100.0  # cifra base per tutti i veicoli

class Autocarro(Veicolo):
    # --snip--
    def tassa_circolazione(self) -> float:
        base: float = super().tassa_circolazione()
        maggiorazione: float = self.capacita_carico * 0.1  # maggiorazione
        return base + maggiorazione
```

In questo esempio, il metodo `tassa_circolazione` nella classe `Autocarro` chiama prima il metodo della classe base utilizzando `super()`, ottenendo così la cifra base (che, in caso di modifiche, dovrà essere modificata in un unico punto) per poi aggiungere la maggiorazione calcolata in base alla capacità di carico dell'autocarro. Si noti come negli Autoveicoli il metodo `tassa_circolazione` rimanga invariato, ereditando il comportamento definito nella classe `Veicolo`:

```python
auto: Autovettura = Autovettura("AB123CD", "Lancia", "Ypsilon", 2005, 4)
camion: Autocarro = Autocarro("EF456GH", "Iveco", "Stralis", 2015, 2000)

print(auto.tassa_circolazione())   # 100.0
print(camion.tassa_circolazione()) # 100.0 + (2000 * 0.1) = 300.0
```

#pagebreak()

= Il Polimorfismo

Un ulteriore vantaggio dell'uso dell'ereditarietà è la possibilità di sfruttare il polimorfismo, un concetto che consente di trattare oggetti di classi diverse in modo uniforme, purché condividano una stessa interfaccia (cioè abbiano metodi con lo stesso nome e firma).

Immaginiamo di avere una classe `Cliente` che modella - per l'appunto - un cliente di una società di noleggio veicoli, il quale può noleggiare sia Autovetture che Autocarri:

```python
class Cliente:
    def __init__(self, nome: str):
        self.nome: str = nome
        self.veicoli_noleggiati: list[Veicolo] = []
```

Per poter gestire il noleggio di veicoli, possiamo definire un metodo `noleggia_veicolo` che accetta un oggetto di tipo `Veicolo` (o di una sua sottoclasse) e lo aggiunge alla lista dei veicoli noleggiati:

```python
class Cliente:
    # --snip--
    def noleggia_veicolo(self, veicolo: Veicolo):
        self.veicoli_noleggiati.append(veicolo)
```

Per Python non importa se l'oggetto passato a `noleggia_veicolo` è un'istanza di `Autovettura` o di `Autocarro`, purché entrambi abbiano i metodi e gli attributi necessari per essere gestiti correttamente: questo è il cuore del polimorfismo. Immaginiamo ora di voler calcolare la tassa di circolazione totale per tutti i veicoli noleggiati da un cliente; possiamo farlo iterando sulla lista dei veicoli e chiamando il metodo `tassa_circolazione` su ciascuno di essi, senza preoccuparci del tipo specifico di veicolo, in quanto Python risolverà automaticamente la chiamata al metodo corretto in base al tipo effettivo dell'oggetto:

```python
class Cliente:
    # --snip--
    def tassa_totale(self) -> float:
        totale: float = 0.0
        for veicolo in self.veicoli_noleggiati:
            totale += veicolo.tassa_circolazione()
        return totale
```

In questo modo, possiamo gestire veicoli di tipi diversi in modo uniforme, sfruttando il polimorfismo per semplificare il codice e migliorare la sua manutenibilità:

```python
cliente: Cliente = Cliente("Mario Rossi")
auto: Autovettura = Autovettura("AB123CD", "Lancia", "Ypsilon", 2005, 4)
camion: Autocarro = Autocarro("EF456GH", "Iveco", "Stralis", 2015, 2000)

cliente.noleggia_veicolo(auto)
cliente.noleggia_veicolo(camion)

print(cliente.tassa_totale())  # 100.0 + 300.0 = 400.0
```

Si noti che, una volta che una istanza specifica è stata mescolata in un contesto polimorfico, per risalire al suo tipo originale (ad esempio per accedere a metodi o attributi specifici della sottoclasse) si renderà necessario utilizzare il controllo del tipo con l'operatore `is`; ad esempio, se volessimo accedere alla capacità di carico di un veicolo noleggiato solo se si tratta di un autocarro, dovremmo fare quanto segue:

```python
for veicolo in cliente.veicoli_noleggiati:
    if type(veicolo) is Autocarro:
        print(f"Capacità di carico: {veicolo.capacita_carico} kg")
```
