// == Imports ==

#import "../common/typst/cover.typ": slide_cover
#import "../common/typst/utils.typ": slidew, center_url, url_with_qr


// == Setup ==

#set page(paper: "presentation-16-9")
#set text(font: "New Computer Modern", size: 25pt, fill: black, lang: "it")

#let title = "Tipi di Dato e Controllo del Flusso"
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

  - Variabili (dichiarazioni e update)
  - Tipi di dato primitivi (`int`, `float`, `complex`, `str`, `bool`)
  - Controllo del flusso di esecuzione (`if`, `while`, `for`)

  Questo è il momento perfetto per fare domande su questi argomenti!
]

#slidew(
  slide_title: "Proposte di progetto",
  title: title, course: course, author: author
)[
  Per mettere in pratica quello che avete imparato e per *scoprire qualcosa di nuovo*, ci dedicheremo ora a qualche progetto.

  == Regole del gioco:
  - Ognuno deve *scegliere un progetto* da sviluppare tra quelli proposti o, eventualmente, pensare a qualcosa di equivalente da realizzare (e, ovviamente, da mostrare poi alla classe);
  - Per ora non lavoreremo a gruppi, ma chi è già ferrato nella programmazione è invitato a farsi avanti come *"tutor" per i colleghi*;
  - Si lavorerà in locale sulle macchine e alla fine si *caricherà il risultato sulla repo GitHub* di classe;
  - Alla fine faremo delle *presentazioni* per condividere con la classe le soluzioni a cui avete pensato.
]

#slidew(
  slide_title: "1. 🧮 Mini Calcolatrice Interattiva",
  title: title, course: course, author: author
)[
  Scrivere un programma che chieda all'utente un'operazione (`+`, `-`, `*`, `/`, ...) con due numeri di input e mostri il risultato.

  Provare anche a:
  - chiedere all'utente se vuole continuare dopo ogni operazione;
  - gestire input non validi (es. divisione per 0, caratteri non numerici);
  - permettere di calcolare i giorni di differenza tra due particolari mesi (e.g., novembre 2024 e aprile 2025).
]

#slidew(
  slide_title: "2. 🔢 Indovina il Numero",
  title: title, course: course, author: author
)[
  Scrivere un programma che genera un numero segreto e lo fa indovinare all'utente. Dopo ogni tentativo, il programma dovrebbe rispondere "troppo alto", "troppo basso" o "corretto!", contando il numero di tentativi e mostrandolo alla fine.

  Provare anche a:
  - Dare un numero massimo di tentativi (configurabile);
  - Permettere all'utente di giocare di nuovo;
  - Implementare un qualche tipo di multiplayer (locale!).
]

#slidew(
  slide_title: "3. 🧑‍🍳 Menu Interattivo",
  title: title, course: course, author: author
)[
  Creare un programma che mostri un menu (ad esempio, "Caffè – 1€, Cappuccino – 1.5€, The – 1€"), chieda all'utente cosa vuole ordinare e poi stampi il prezzo. L'utente può continuare a ordinare finché non digita “stop”, dopodichè il programma somma il totale e lo mostra.

  Provare anche a introdurre una "admin mode" che, a fronte dell'inserimento di una password, consenta di rinominare gli articoli e di modificarne il prezzo.
]

#slidew(
  slide_title: "Riepilogo",
  title: title, course: course, author: author
)[
  Potete scegliere tra:

  1. 🧮 Mini Calcolatrice Interattiva;
  2. 🔢 Indovina il Numero;
  3. 🧑‍🍳 Menu Interattivo;
  4. Una vostra proposta!

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
  #url_with_qr("https://311to.site/bi")
]

#slidew(
  slide_title: "Per ripassare a casa",
  title: title, course: course, author: author
)[
  #url_with_qr("https://take.panquiz.com/8287-4913-9383")
]
