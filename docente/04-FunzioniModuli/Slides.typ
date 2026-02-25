// == Imports ==

#import "../common/typst/cover.typ": slide_cover
#import "../common/typst/utils.typ": slidew, center_url, exp, difficulty, url_with_qr


// == Setup ==

#set page(paper: "presentation-16-9")
#set text(font: "New Computer Modern", size: 25pt, fill: black, lang: "it")

#let title = "Funzioni e Moduli"
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

  - Funzioni
  - Moduli
  - Package

  Questo è il momento perfetto per fare domande su questi argomenti!
]

#slidew(
  slide_title: "Live project",
  title: title, course: course, author: author
)[
  Realizziamo insieme un software per la gestione di liste elettorali usando funzioni, moduli e concetti già esplorati. Il programma dovrà gestire candidati appartenenti a più liste, organizzando il codice in funzioni e moduli:

  - Permettendo l'aggiunta di una nuova lista;
  - Permettendo l'aggiunta di un nuovo candidato;
  - Permettendo di votare un candidato.
]

#slidew(
  slide_title: "Progetto: Libreria Musicale",
  title: title, course: course, author: author
)[
  Oggi il progetto sarà unico, diviso in *livelli ben separati*.

  Per ognuno allocheremo il tempo necessario a svolgerlo e dedicheremo un *momento di feedback* prima di passare al successivo.

  Prima di iniziare formeremo delle *coppie*, con il requisito che ognuna di queste dovrà essere formata da un programmatore con *esperienza pregressa* a questo corso e l'*altro senza*.
]

#slidew(
  slide_title: "Libreria Musicale: Livello 1",
  level: 1,
  title: title, course: course, author: author
)[
  L'elemento base di ogni collezione musicale sono le singole tracce, quindi il nostro programma non potrà prescindere dal gestirle:

  - Trovare una rappresentazione adatta a descrivere una *singola traccia* con i suoi dati annessi (titolo, durata, voto da 1 a 5);
  - Creare una funzione che, data una lista e questi tre dati, aggiunga in coda alla lista la rappresentazione della traccia.
]

#slidew(
  slide_title: "Libreria Musicale: Livello 2",
  level: 2,
  title: title, course: course, author: author
)[
  Gli album sono il raccoglitore delle tracce e sono l'oggetto ideale a contenerle anche nella nostra applicazione:

  - Trovare una rappresentazione adatta a descrivere un *album* (titolo, autore, tracce);
  - Creare una funzione che dato titole e autore crei un album vuoto;
  - Creare una funzione che, dato l'album e i singoli dati di una traccia ne crei una rappresentazione al suo interno.
]

#slidew(
  slide_title: "Libreria Musciale: Livello 3",
  level: 3,
  title: title, course: course, author: author
)[
  Finalmente siamo pronti a creare la nostra collezione vera e propria, raccogliendo più album in una lista; a questo punto:

  - Scrivere una funzione, che dato un album, calcoli la media delle recensioni delle sue tracce;
  - Scrivere una funzione, che data una raccolta e il titolo di una canzone, ne trovi l'autore;
  - Organizzare tutte le funzioni create fino ad ora in una struttura di file in base al loro scopo.
]

#slidew(
  slide_title: "Feedback sul laboratorio di oggi",
  title: title, course: course, author: author
)[
  #url_with_qr("https://311to.site/bs")
]

#slidew(
  slide_title: "Per ripassare a casa",
  title: title, course: course, author: author
)[
  #url_with_qr("https://take.panquiz.com/2615-9944-1000")
]
