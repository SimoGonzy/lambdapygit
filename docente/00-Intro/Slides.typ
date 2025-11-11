// == Imports ==

#import "../common/typst/cover.typ": slide_cover
#import "../common/typst/utils.typ": slidew, center_url


// == Setup ==

#set page(paper: "presentation-16-9")
#set text(font: "New Computer Modern", size: 25pt, fill: black, lang: "it")

#let title = "Introduzione al Corso"
#let course = "Python: da Zero a OOP"
#let author = "Riccardo Sacchetto, B.Sc."
#let email = "riccardo.sacchetto@itsdigitalacademy.com"


// == Content ==

#slide_cover(
  title: title, course: course,
  description: "",
  author: author, email: email
)

#slidew(
  slide_title: "Il Docente",
  title: title, course: course, author: author
)[
  *Riccardo Sacchetto, B.Sc.*

  - Studente del Corso di Laurea Magistrale in Ingegneria e Scienze Informatiche all'Università degli Studi di Verona
  - Consulente Informatico per PMI
  - Già docente in corsi STEM presso Istituti Secondari di Secondo Grado

  #v(1em)

  *Contatto*: rsacchetto\@nexxontech.it
]

#slidew(
  slide_title: "Il Corso",
  title: title, course: course, author: author
)[
  Corso di introduzione alla programmazione in Python e all'utilizzo di Git/GitHub, finalizzato a illustrare il paradigma di programmazione ad oggetti (OOP).

  *Tempi*: 12 laboratori da 4h ciascuno, per un totale di 48 ore dal 27 ottobre al 2 febbraio.

  *Modalità*: L'obiettivo è ridurre la teoria al minimo indispensabile, privilegiando esercitazioni pratiche e progetti.
]

#slidew(
  slide_title: "Materiale e Repo del Corso",
  title: title, course: course, author: author
)[
  Il materiale del corso sarà a disposizione su OSASpace prima di ogni lezione nella cartella:

  #center_url("https://311to.site/au")

  La repo in cui caricare gli esercizi e i progetti è disponibile su GitHub all'indirizzo:

  #center_url("https://311to.site/av")
]

#slidew(
  slide_title: "Python",
  title: title, course: course, author: author
)[
  Python è un linguaggio di programmazione *ad alto livello*, *orientato a oggetti*, adatto, tra gli altri usi, a sviluppare applicazioni distribuite, scripting, *computazione numerica* e system testing.

  _- Wikipedia_
]

#slidew(
  slide_title: "Installazione",
  title: title, course: course, author: author
)[
  Essendo un linguaggio interpretato, Python necessita di un interprete per essere eseguito. Questo può essere scaricato dal sito ufficiale:

  #align(center)[
    *#text[https://311to.site/aq]*
  ]

  La distribuzione ufficiale include anche un semplice ambiente di sviluppo integrato (IDE) chiamato IDLE, ma durante il corso utilizzeremo qualcosa di più avanzato.
]

#slidew(
  slide_title: "Zed Editor",
  title: title, course: course, author: author
)[
  Zed è un editor di testo avanzato, personalizzabile, open-source e multipiattaforma, adatto per lo sviluppo in Python e altri linguaggi. Può essere scaricato all'indirizzo:

  #align(center)[
    *#text[https://311to.site/ar]*
  ]

  Alla prima apertura procederà in automatico a configurare il linter per semplificare lo sviluppo dei programmi.
]

#slidew(
  slide_title: "Il Primo Programma",
  title: title, course: course, author: author
)[
  In un nuovo progetto, creiamo un file `Lezione0.py` e inseriamo il seguente codice:

  ```python
  print("Hello World!")
  ```

  Andiamo quindi nel menu sotto la voce `Run` > `Spawn Task` (o `Alt-Shift-T`) e selezioniamo "run C:/.../Lezione0.py".

  Qual è il risultato?
]

#slidew(
  slide_title: "Esercizio 1",
  title: title, course: course, author: author
)[
  1. Fai mostrare al programma una nuova scritta oltre a quella in inglese (ad esempio, un saluto in italiano)
  2. Fai mostrare il risultato di un calcolo (ad esempio, `1+1`)
  3. Trova il modo di andare a capo _senza_ usare due istruzioni `print` distinte
]

#slidew(
  slide_title: "Git",
  title: title, course: course, author: author
)[
  Git è un sistema distribuito di *controllo del versionamento*, utilizzato per gestire le varie versioni di dati e codice.

  Git mantiene una *copia locale* dell'intera repository su cui effettuare le operazioni di modifica della storia, permettendo di lavorare anche *senza connessione ad un server* centrale. Il sistema mette poi a disposizione comandi per *sincronizzare* le modifiche con il server remoto quando necessario.

  _- Wikipedia_
]

#slidew(
  slide_title: "Installazione di Git",
  title: title, course: course, author: author
)[
  Git è disponibile per tutti i principali sistemi operativi (Windows, Linux e macOS) al seguente indirizzo:

  #center_url("https://311to.site/as")

  Si noti che, una volta installato, in genere è necessario configurare nome utente e indirizzo email:

  ```bash
  git config --global user.name "Nome Cognome"
  git config --global user.email "io@domain.tld"
  ```
]

#slidew(
  slide_title: "Versioniamo il nostro primo script",
  title: title, course: course, author: author
)[
  Ora che abbiamo toccato con mano i concetti base di Git, possiamo procedere a versionare il nostro script Python.

  Apriamo la repo del corso e selezioniamo "Fork":

  #center_url("https://311to.site/av")

  Quindi, nella pagina che si apre, copiamo l'indirizzo sotto la voce "Code" e utilizziamolo per clonare la repo:

  ```bash
  git clone [indirizzo copiato]
  ```
]

#slidew(
  slide_title: "Versioniamo il nostro primo script",
  title: title, course: course, author: author
)[
  Nella cartella che è stata creata, cerchiamo `studenti/`, aggiungiamoci la nostra cartella `ncognome`:

  ```bash
  mkdir lambdapygit/studenti/ncognome
  ```

  e spostiamo al suo interno lo script `Lezione0.py`.

  Facciamo dunque il commit per versionarlo:

  ```bash
  git add .
  git commit -m "[Breve riassunto delle modifiche fatte]"
  ```
]

#slidew(
  slide_title: "Versioniamo il nostro primo script",
  title: title, course: course, author: author
)[
  Procediamo dunque a fare il push con

  ```bash
  git push
  ```

  e ad aprire una Pull Request sulla repo originale del corso aprendo la pagina web del fork e selezionando l'opzione "Contribute".
]
