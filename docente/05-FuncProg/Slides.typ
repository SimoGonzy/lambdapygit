// == Imports ==

#import "../common/typst/cover.typ": slide_cover
#import "../common/typst/utils.typ": slidew, center_url, exp, difficulty, url_with_qr


// == Setup ==

#set page(paper: "presentation-16-9")
#set text(font: "New Computer Modern", size: 25pt, fill: black, lang: "it")

#let title = "Programmazione Funzionale e Iteratori"
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

  - Funzioni di ordine superiore
  - Sintassi `lambda`
  - Funzioni `map`, `filter` e `reduce`

  Questo è il momento perfetto per fare domande su questi argomenti!
]

#slidew(
  slide_title: "Esercizi sugli argomenti del giorno",
  title: title, course: course, author: author
)[
  Vista la natura degli argomenti, gli esercizi di oggi saranno più piccoli e mirati, ma divisi in tre livelli di difficoltà crescente.

  Il lavoro è pensato per essere svolto in *coppia*, con un membro più esperto e uno meno esperto; per ogni livello sarà allocato un po' di tempo per la risoluzione e, alla fine, un momento di *feedback* per discutere le soluzioni adottate.
]

#slidew(
  slide_title: "Esercizi sulle lambda: Livello 1",
  level: 1,
  title: title, course: course, author: author
)[
  - Scrivi una lambda function che, preso un numero, ne restiuisca il quadrato;
  - Scrivi una lambda function che, presi due numeri, ne restiuisca la somma;
  - Scrivi una lambda function che, prese due stringhe con un nome e un cognome, restituisca la stringa con il nome completo (es. "Mario" e "Rossi" #sym.arrow "Mario Rossi").
  - Scrivi una lambda function che, presa una stringa, restituisca True se la stringa ha lunghezza pari, False altrimenti;
]

#slidew(
  slide_title: "Esercizi sui funzionali: Livello 2",
  level: 2,
  title: title, course: course, author: author
)[
  - Scrivi una funzione `apply_to_sum`, che, presi una funzione `fun` e due valori `val1` e `val2`, applichi `fun` alla somma di `val1` e `val2` (cioè calcoli `fun(val1 + val2)`);
  - Scrivi una funzione `apply_twice`, che, presi una funzione `fun` e un valore `val`, applichi `fun` a `val` due volte di seguito (cioè calcoli `fun(fun(val))`);
  - Scrivi una funzione `incrementer`, che, preso un numero `n`, restituisca una funzione che, preso un altro numero `x`, restituisca `x + n`;
]

#slidew(
  slide_title: "Esercizi sugli iteratori: Livello 3",
  level: 3,
  title: title, course: course, author: author
)[
  - Dato l’elenco `nums = [10, 15, 20, 25, 30]`, estrai solo i numeri maggiori di 20.
  - Dato l’elenco `words = ["ciao", "python", "lambda", "hi", "fun"]`, ottieni la lista delle lunghezze di ogni parola.
  - Dato l’elenco `words = ["anna", "bob", "carla", "daniele", "eve"]`, estrai solo le parole che iniziano con la lettera “a”.
  - Dato l’elenco `nums = [2, 3, 5, 7, 11]`, calcola il prodotto di tutti i numeri.
]

#slidew(
  slide_title: "Sfide Finali (1)",
  level: 4,
  title: title, course: course, author: author
)[
  - Supponiamo di avere una lista di tuple
    ```python
    pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]
    ```
    Usa la programmazione funzionale per ottenere la lista delle somme di ogni coppia (i.e. `[3, 7, 11, 15]`).
]
#slidew(
  slide_title: "Sfide Finali (2)",
  level: 4,
  title: title, course: course, author: author
)[
  - Supponiamo di avere una lista di dizionari che rappresentano persone:
    ```python
    people = [
      {"name": "Mario", "age": 23},
      # ...
    ]
    ```
    Usa la programmazione funzionale per estrarre i nominativi delle persone maggiorenni.
]

#slidew(
  slide_title: "Feedback sul laboratorio di oggi",
  title: title, course: course, author: author
)[
  #url_with_qr("https://311to.site/bt")
]

#slidew(
  slide_title: "Per ripassare a casa",
  title: title, course: course, author: author
)[
  #url_with_qr("https://take.panquiz.com/5658-5841-4120")
]
