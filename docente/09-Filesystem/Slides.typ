// == Imports ==

#import "../common/typst/cover.typ": slide_cover
#import "../common/typst/utils.typ": slidew, center_url, exp, difficulty, url_with_qr


// == Setup ==

#set page(paper: "presentation-16-9")
#set text(font: "New Computer Modern", size: 25pt, fill: black, lang: "it")

#let title = "Lavorare con il filesystem"
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
  slide_title: "",
  title: title, course: course, author: author
)[
  #align(center)[
    #image("images/logoitscyber.png", width: 150pt)
  ]

  La *ITSCyberGame* è una competizione nazionale dedicata agli studenti degli ITS, progettata per promuovere l’eccellenza e le competenze nel campo della *cybersicurezza*.

  Organizzata dal *CINI Cybersecurity National Lab* e *Edulife Impresa Sociale*, in collaborazione con l’*Associazione Rete ITS Italy* e con il patrocinio e il supporto dell’*ACN*.
]

#slidew(
  slide_title: "ITSCyberGame - Sito Ufficiale",
  title: title, course: course, author: author
)[
  #url_with_qr("https://itscybergame.it/")
]

#slidew(
  slide_title: "ITSCyberGame - Materiale di Training",
  title: title, course: course, author: author
)[
  #url_with_qr("https://training.olicyber.it/")
]

#slidew(
  slide_title: "Argomenti del Laboratorio",
  title: title, course: course, author: author
)[
  Nella dispensa di questa settimana erano trattati i seguenti argomenti:

  - Lettura e scrittura di file
  - Formato CSV
  - Serializzazione e deserializzazione di classi

  Questo è il momento perfetto per fare domande su questi argomenti!
]

#slidew(
  slide_title: "Progetto: Mini-Tamagotchi",
  title: title, course: course, author: author
)[
  Tra una lezione e l'altra hai iniziato a sentirti un po' solo, così hai deciso di sviluppare un piccolo programma per prenderti cura di un Tamagotchi virtuale.

  Quello che vorresti realizzare è un piccolo gioco in cui devi prenderti cura di uno o più Tamagotchi, assicurandoti che siano felici e in salute. Requisito fondamentale è che lo stato dei tuoi Tamagotchi venga salvato su file, in modo da poter riprendere il gioco in qualsiasi momento.
]

#slidew(
  slide_title: "Livello 1: il Tamagotchi",
  level: 1,
  title: title, course: course, author: author
)[
  Trova il modo più adatto di rappresentare il Tamagotchi, che deve avere almeno le seguenti caratteristiche:

  - Un nome e degli indicatori per fame, felicità e stanchezza;
  - Metodi per nutrirlo (diminuisce la fame e aumenta la stanchezza), giocare con lui (aumenta la felicità e la stanchezza) e farlo dormire (diminuisce stanchezza e felicità e aumenta la fame);
  - Indroduci un menu da CLI per interagirvi (vedere lo stato e scegliere l'azione da fare).
]

#slidew(
  slide_title: "Livello 2: più Tamagotchi",
  level: 2,
  title: title, course: course, author: author
)[
  Avere un Tamagotchi è divertente, ma averne di più lo è ancora di più!

  - Modifica il programma in modo da poter gestire più Tamagotchi contemporaneamente;
  - Permetti all'utente di scegliere con quale Tamagotchi interagire dal menu principale;
  - Permetti all'utente di aggiungere nuovi Tamagotchi o rimuoverli.
]

#slidew(
  slide_title: "Livello 3: salvataggio su file",
  level: 3,
  title: title, course: course, author: author
)[
  Non si può certo perdere il progresso fatto con i propri Tamagotchi ogni volta che si chiude il programma!

  - Implementa il salvataggio dello stato di tutti i Tamagotchi su un file quando il programma termina;
  - Implementa il caricamento dello stato dei Tamagotchi dal file all'avvio del programma.
]

#slidew(
  slide_title: "Challenge Finale: diversi tipi di Tamagotchi",
  level: 4,
  title: title, course: course, author: author
)[
  Introduci delle sottoclassi per gestire Tamagotchi adulti o cuccioli in base al numero di cicli di sonno, con comportamenti diversi:

  - I cuccioli si stancano più velocemente quando giocano, ma si riposano più velocemente quando dormono;
  - Gli adulti si stancano meno velocemente, ma richiedono più cibo per essere nutriti.
]

#slidew(
  slide_title: "Feedback sul laboratorio di oggi",
  title: title, course: course, author: author
)[
  #url_with_qr("https://311to.site/c7")
]

#slidew(
  slide_title: "Per ripassare a casa",
  title: title, course: course, author: author
)[
  #url_with_qr("https://kahoot.it/challenge/004298455")
]
