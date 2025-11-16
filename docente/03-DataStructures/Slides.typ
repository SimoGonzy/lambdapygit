// == Imports ==

#import "../common/typst/cover.typ": slide_cover
#import "../common/typst/utils.typ": slidew, center_url, exp, difficulty, url_with_qr


// == Setup ==

#set page(paper: "presentation-16-9")
#set text(font: "New Computer Modern", size: 25pt, fill: black, lang: "it")

#let title = "Strutture Dati: Liste, Tuple e Dizionari"
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

  - Liste
  - Tuple
  - Dizionari
  - Mutabilità

  Questo è il momento perfetto per fare domande su questi argomenti!
]

#slidew(
  slide_title: "Proposte di progetto",
  title: title, course: course, author: author
)[
  Si propongono tre semplici progetti per mettere in pratica quello che avete imparato e per *scoprire qualcosa di nuovo*:

  1. 📈 Generatore di Statistiche; #difficulty(1)
  2. 📘 Rubrica Telefonica; #difficulty(2)
  3. 📋 Catalogo Prodotti; #difficulty(3)
]

#slidew(
  slide_title: "1. 📈 Generatore di Statistiche",
  level: 1,
  title: title, course: course, author: author
)[
  Scrivere un programma che chieda all'utente di inserire una serie di numeri e consenta successivamente di:

  - Calcolare massimo e minimo; #exp(10)
  - Estrarre i numeri pari o i numeri dispari; #exp(10)
  - Ordinare la lista; #exp(10)
  - Calcolare moda, media e mediana; #exp(20)
  - Estrarre i numeri sopra la media; #exp(20)
]

#slidew(
  slide_title: "2. 📘 Rubrica Telefonica",
  level: 2,
  title: title, course: course, author: author
)[
  Realizzare un programma che consenta di associare nomi a uno o più numeri di telefono. Nello specifico, consentire all'utente di:

  - Aggiungere un nuovo contatto; #exp(10)
  - Cercare un contatto per nome; #exp(10)
  - Aggiungere/rimuovere un numero a un contatto; #exp(20)
  - Modificare il nome di un contatto; #exp(20)
  - Cercare a chi appartiene un numero. #exp(30)
]

#slidew(
  slide_title: "3. 📋 Catalogo Prodotti",
  level: 3,
  title: title, course: course, author: author
)[
  Sviluppare un piccolo gestionale che consenta di memorizzare i prodotti in catalogo. Il programma deve permettere di:

  - Mostrare un prodotto con nome, prezzo e categoria; #exp(10)
  - Rimuovere un prodotto dato il nome; #exp(10)
  - Aggiungere un nuovo prodotto; #exp(20)
  - Filtrare i prodotti per prezzo o categoria; #exp(30)
  - Trovare il prodotto più costoso o più economico; #exp(30)
]

#slidew(
  slide_title: "Challenge:\nSistema di Raccomandazioni",
  level: 4,
  title: title, course: course, author: author
)[
  Realizzare un algoritmo di raccomandazione di contenuti che, dato un database di utenti e di film che hanno gradito:

  - Prenda in input il nome dell'utente corrente;
  - Trovi quello più simile (cfr. coefficiente di Jaccard);
  - Suggerisca i film che l'utente simile ha gradito e che l'utente corrente non ha ancora visto.
]

#slidew(
  slide_title: "Riepilogo",
  title: title, course: course, author: author
)[
  Potete scegliere tra:

  1. 📈 Generatore di Statistiche; #difficulty(1)
  2. 📘 Rubrica Telefonica; #difficulty(2)
  3. 📋 Catalogo Prodotti; #difficulty(3)

  La challenge finale è facoltativa ma consigliata per i più esperti.

  Queste slide con la definizione dei requisiti sono già disponibili su OSASpace. *Buon lavoro!*
]

#slidew(
  slide_title: "Time's up!",
  title: title, course: course, author: author
)[
  *Il tempo è scaduto!*

  Come la volta scorsa, fate il commit del vostro lavoro sulla repo Git, il push su GitHub e il merge della Pull Request.

  *Chi intende presentare il proprio lavoro alla classe, si faccia avanti ora!* L'ideale sarebbe avere almeno una presentazione per ognuno dei tre tipi di progetto.
]

#slidew(
  slide_title: "Feedback sul laboratorio di oggi",
  title: title, course: course, author: author
)[
  #url_with_qr("https://311to.site/br")
]

#slidew(
  slide_title: "Per ripassare a casa",
  title: title, course: course, author: author
)[
  #url_with_qr("https://take.panquiz.com/9389-2303-0877")
]
