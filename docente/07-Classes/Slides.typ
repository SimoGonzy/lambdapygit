// == Imports ==

#import "../common/typst/cover.typ": slide_cover
#import "../common/typst/utils.typ": slidew, center_url, exp, difficulty, url_with_qr


// == Setup ==

#set page(paper: "presentation-16-9")
#set text(font: "New Computer Modern", size: 25pt, fill: black, lang: "it")

#let title = "Introduzione alle Classi"
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

  - Definizione di una classe con attributi e metodi;
  - Costruttore `__init__`;
  - Incapsulamento;
  - Magic methods.

  Questo è il momento perfetto per fare domande su questi argomenti!
]

#slidew(
  slide_title: "Progetto: Gestione Bibliotecaria",
  title: title, course: course, author: author
)[
  Sei stato contattato da una biblioteca per sviluppare un software di gestione della loro collezione di libri.

  Ogni volume dovrà essere catalogato dal software con titolo, autore, editore, anno di pubblicazione e stato (libero/noleggiato) e raggruppato sotto un certo scaffale caratterizzato da un codice identificativo e una sezione tematica (es. "Narrativa", "Saggistica", "Informatica", ecc.).
]

#slidew(
  slide_title: "Livello 1: il Libro",
  level: 1,
  title: title, course: course, author: author
)[
  L'elemento base della nostra applicazione sarà il libro, per cui:

  - Trovare una rappresentazione adatta a descrivere un *libro* (titolo, autore, editore, anno di pubblicazione, stato);
  - Fare sì che la `print` di un libro mostri tutte le sue informazioni in modo leggibile;
  - Creare un metodo che cambi lo stato del libro da "libero" a "noleggiato" e viceversa.
]

#slidew(
  slide_title: "Livello 2: lo Scaffale",
  level: 2,
  title: title, course: course, author: author
)[
  Gli scaffali dovranno consentire di memorizzare al loro interno più libri, per cui:

  - Trovare una rappresentazione adatta a descrivere uno *scaffale* (codice identificativo, sezione tematica, lista di libri);
  - Creare metodi che permettano di aggiungere e rimuovere dei libri;
  - Creare un metodo che permetta di cercare un libro per titolo all'interno dello scaffale.
]

#slidew(
  slide_title: "Livello 3: miglioramenti QoL",
  level: 3,
  title: title, course: course, author: author
)[
  Modificare quanto fatto fino a ora per fare sì che:

  - La `print` di uno scaffale mostri tutte le sue informazioni in modo leggibile, inclusi i libri al suo interno;
  - La somma di due libri risulti in un nuovo scaffale con entrambi i libri al suo interno;
  - La somma di due scaffali risulti in un nuovo scaffale con tutti i libri al suo interno;
  - La funzione `len` su uno scaffale ritorni il numero di libri al suo interno;
  - Il confronto tra due scaffali operi sulla quantità di libri al loro interno.
]

#slidew(
  slide_title: "Feedback sul laboratorio di oggi",
  title: title, course: course, author: author
)[
  #url_with_qr("https://311to.site/bu")
]

#slidew(
  slide_title: "Per ripassare a casa",
  title: title, course: course, author: author
)[
  #url_with_qr("https://take.panquiz.com/5348-9029-7529")
]
