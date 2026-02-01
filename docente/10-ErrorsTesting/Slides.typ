// == Imports ==

#import "../common/typst/cover.typ": slide_cover
#import "../common/typst/utils.typ": slidew, center_url, exp, difficulty, url_with_qr


// == Setup ==

#set page(paper: "presentation-16-9")
#set text(font: "New Computer Modern", size: 25pt, fill: black, lang: "it")

#let title = "Gestione degli Errori e Testing"
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
  slide_title: "Argomenti del Laboratorio",
  title: title, course: course, author: author
)[
  Nella dispensa di questa settimana erano trattati i seguenti argomenti:

  - Gestione delle eccezioni
  - Eccezioni personalizzate
  - Testing del codice con unit test

  Questo è il momento perfetto per fare domande su questi argomenti!
]

#slidew(
  slide_title: "Progetto: Riordinatore Intelligente",
  title: title, course: course, author: author
)[
  Come al solito, la cartella Downloads del tuo computer è piena di file disordinati e vuoi creare un programma per riordinarli automaticamente in cartelle basate sul tipo di file.

  Quello che vorresti ottenere è un programma che legga l'elenco di file contenuti in una certa cartella, li classifichi uno per uno (e.g., Documenti, Immagini, Video, etc.) e li smisti spostandoli nelle cartelle appropriate.
]

#slidew(
  slide_title: "Livello 1: il Classificatore",
  level: 1,
  title: title, course: course, author: author
)[
  Scrivi una funzione (o un metodo, in base a come intendi organizzare il codice) che, dato in input un Path, restituisca il Path della cartella in cui il file dovrebbe essere spostato in base alla sua estensione.

  Ricordati di gestire in maniera appropriata il caso in cui l'estensione del file non sia supportata e non sia dunque possibile decidere la cartella di destinazione.
]

#slidew(
  slide_title: "Livello 2: il Motore di Smistamento",
  level: 2,
  title: title, course: course, author: author
)[
  Scrivi una funzione che, preso in input il Path di una cartella, legga tutti i file al suo interno e li sposti nelle cartelle appropriate utilizzando il classificatore del Livello 1.

  Anche qui, fai attenzione a gestire in maniera opportuna eventuali errori che possono verificarsi durante la classificazione e lo spostamento dei file (e.g., permessi insufficienti, file in uso, etc.).

  Le funzioni che possono fallire possono essere verificate nella documentazione ufficiale di Python.
]

#slidew(
  slide_title: "Livello 3: testing!",
  level: 3,
  title: title, course: course, author: author
)[
  Scrivi degli unit test opportuni per verificare il corretto funzionamento delle funzioni sviluppate nei Livelli 1 e 2. In particolare, assicurati che i seguenti casi siano coperti, eventualmente creando una cartella ad-hoc nello unit test stesso:

  1. Classificazione corretta dei file con estensioni supportate;
  2. Gestione appropriata delle estensioni non supportate;
  3. Spostamento corretto dei file nelle cartelle appropriate;
  4. Gestione degli errori durante lo spostamento dei file.
]

#slidew(
  slide_title: "Challenge Finale: Audit Logging",
  level: 4,
  title: title, course: course, author: author
)[
  Introduci un sistema di logging che tenga traccia di tutte le operazioni di smistamento effettuate dal programma, registrando informazioni come il nome del file, la cartella di destinazione e l'esito dell'operazione (successo o errore).

  Il log dovrebbe essere creato istanziando una serie di oggetti che rappresentano le singole operazioni di smistamento, e salvato su un file di testo mediante serializzazione alla fine dell'esecuzione del programma.
]

#slidew(
  slide_title: "Feedback sul laboratorio di oggi",
  title: title, course: course, author: author
)[
  #url_with_qr("https://311to.site/c8")
]

#slidew(
  slide_title: "Per ripassare a casa",
  title: title, course: course, author: author
)[
  #url_with_qr("https://kahoot.it/challenge/001333601")
]
