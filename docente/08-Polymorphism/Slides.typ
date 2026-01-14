// == Imports ==

#import "../common/typst/cover.typ": slide_cover
#import "../common/typst/utils.typ": slidew, center_url, exp, difficulty, url_with_qr


// == Setup ==

#set page(paper: "presentation-16-9")
#set text(font: "New Computer Modern", size: 25pt, fill: black, lang: "it")

#let title = "Gerarchia delle Classi & Polimorfismo"
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

  - Ereditarietà
  - Polimorfismo

  Questo è il momento perfetto per fare domande su questi argomenti!
]

#slidew(
  slide_title: "Progetto: Gestionale HR",
  title: title, course: course, author: author
)[
  Sei stato contattato da una azienda per realizzare un gestionale delle Buste Paga per il dipartimento di Risorse Umane.

  Il gestionale dovrà essere in grado di calcolare lo stipendio dei vari dipendenti in base al loro ruolo nell'azienda (i Dipendenti hanno uno stipendio orario base, mentre Manager e Commerciali hanno uno stipendio calcolato anche in base alla performance).
]

#slidew(
  slide_title: "Livello 1: il Dipendente",
  level: 1,
  title: title, course: course, author: author
)[
  Il tipo di lavoratore più semplice che deve essere gestito è il Dipendente:

  - Trovare una rappresentazione adatta per gestirne dati anagrafici (nome, cognome, codice fiscale) e paga oraria;
  - Scrivere un metodo che, dato un numero di ore di lavoro solte, ne calcoli lo stipendio;
  - Fare in modo che la `print()` del Dipendente mostri dati utili e che il confronto tra Dipendenti (`<`, `>`, ...) dipenda dalla paga.
]

#slidew(
  slide_title: "Livello 2: Manager e Commerciale",
  level: 2,
  title: title, course: course, author: author
)[
  Il Manager e il Commerciale sono diversi tipi di Dipendenti il cui stipendio è aumentato in base al rendimento:

  - Fare in modo che lo stipendio del Manager abbia un bonus calcolato sulla base del numero di sottoposti;
  - Fare in modo che lo stipendio del Commerciale includa una provvigione percentuale sul fatturato generato;
  - Assicurarsi che `print()` e confronti continiuno a operare correttamente.
]

#slidew(
  slide_title: "Livello 3: l'Azienda",
  level: 3,
  title: title, course: course, author: author
)[
  Per consentire ad HR di svolgere analisi BI, ci viene chiesto di:

  - Trovare una rappresentazione dell'Azienda in modo da raggrupparvi all'interno i Dipendenti;
  - Definire un metodo per calcolare il costo totale di tutti gli stipendi (assumendo un numero standard di ore di lavoro);
  - Definire un metodo per trovare il Commerciale più performante (ovvero con più fatturato).
]

#slidew(
  slide_title: "Feedback sul laboratorio di oggi",
  title: title, course: course, author: author
)[
  #url_with_qr("https://311to.site/c4")
]

#slidew(
  slide_title: "Per ripassare a casa",
  title: title, course: course, author: author
)[
  #url_with_qr("https://take.panquiz.com/0227-5058-3651")
]
