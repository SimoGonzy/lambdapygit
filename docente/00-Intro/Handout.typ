// == Imports ==

#import "../common/typst/cover.typ": handout_cover
#import "../common/typst/utils.typ": slidew, center_url


// == Setup ==

#let title = "Introduzione al Corso"
#let course = "Python: da Zero a OOP"
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
  description: "",
  author: author, email: email
)

#set page(numbering: "1")

= Presentazione

Questo documento è la prima di una serie di dispense per l'insegnamento di Introduzione al linguaggio di programmazione Python e a Git/GitHub tenuto nell'ambito del Corso di Artificial Intelligence Developer and Data Specialist (Lambda).

Il docente del corso è Riccardo Sacchetto, B.Sc. #sym.angle.l#text("rsacchetto@nexxontech.it")#sym.angle.r, studente del Corso di Laurea Magistrale in Ingegneria e Scienze Informatiche presso l'Università degli Studi di Verona, consulente informatico nell'ambito della digital transformation per piccole e medie imprese e già docente in corsi STEM presso Istituti Secondari di Secondo Grado.

I laboratori in aula saranno 12, della durata di 4 ore ciascuno, per un totale di 48 ore complessive. Le lezioni si terranno dal 27 ottobre al 2 febbraio e saranno incentrate principalmente su esercitazioni pratiche e progetti, con la teoria ridotta al minimo indispensabile.

Il materiale del corso sarà disponibile su OSASpace prima di ogni lezione nella cartella raggiungibile al seguente indirizzo: https://app.osaspace.it/f/172881 (https://311to.site/au).

La repository GitHub in cui caricare gli esercizi e i progetti è disponibile all'indirizzo: https://github.com/fondazioneedulife/lambdapygit (https://311to.site/av).

Tutto il materiale è rivolto ad un pubblico alle prime armi con la programmazione ed è rilasciato sotto licenza Creative Commons Attribuzione - Condividi allo stesso modo 4.0 Internazionale (CC BY-SA 4.0).

Per ogni dubbio riguardo il materiale delle dispense (alla sua primissima iterazione e dunque inevitabilmente prono a errori) o quanto presentato in aula, il lettore è invitato a contattare il docente all'indirizzo email fornito in qualunque momento e senza particolari riserve.

#pagebreak()

= Python

Citando quanto si può leggere sulla pagina Wikipedia dedicata, Python è un linguaggio di programmazione *ad alto livello*, *orientato a oggetti*, adatto, tra gli altri usi, a sviluppare applicazioni distribuite, scripting, *computazione numerica* e system testing.

Proprio per la sua versatilità e per la sua facilità di apprendimento Python è uno dei linguaggi di programmazione più popolari al mondo, perfetto per chi si avvicina per la prima volta al mondo della programmazione e per il nostro Corso di Studi.

== Configurazione dell'ambiente

Python è un linguaggio di programmazione interpretato, il che significa che il codice sorgente viene eseguito direttamente da un interprete, senza la necessità di una fase di compilazione preventiva. Questa sua caratteristica, che tra l'altro rende Python particolarmente adatto per lo sviluppo rapido e per la prototipazione, ci richiede di installare un interprete Python sul nostro computer per poter eseguire i programmi che andremo a scrivere.

Per iniziare, rechiamoci dunque sul sito ufficiale di Python, https://www.python.org/downloads/ (https://311to.site/aq), e scarichiamo l'ultima versione stabile disponibile per il nostro sistema operativo (Windows, macOS o Linux).

Una volta installato Python, potremo eseguire i nostri programmi in diversi modi: utilizzando l'interprete interattivo (REPL), eseguendo script direttamente dalla riga di comando con `python /path/to/script.py` o utilizzando ambienti di sviluppo integrati (IDE).

Per questo corso, il suggerimento è quello di utilizzare Zed Editor (https://zed.dev/ (https://311to.site/ar)), un editor di testo avanzato e leggero, perfetto per scrivere codice Python in modo efficiente. Zed Editor è disponibile per Windows, macOS e Linux, e può essere scaricato gratuitamente dal sito ufficiale.

== Il nostro primo programma Python

In Informatica, un programma non è altro che una sequenza finita e ordinata di istruzioni elementari che un computer è in grado di eseguire.

In questo contesto, un linguaggio di programmazione (e, dunque, Python) non è altro che un linguaggio comprensibile sia dall'umano che dal computer in cui scrivere tali istruzioni.

Per iniziare, quindi, sarà sufficiente aprire l'editor di testo e scrivere, riga per riga, i comandi che la macchina dovrà eseguire.

Prima di iniziare, però, si consiglia di creare una nuova cartella dedicata a questo corso e di aprirla nell'editor come progetto (in Zed, selezionando `File` > `Open Folder...`).

Una volta pronti, apriamo un nuovo file `Lezione0.py` (in Zed, tasto destro nel pannello di destra > New File) e partiamo da qualcosa di semplice:

```python
print("Hello World!")
```

Tutto qua: questo è il nostro primissimo programma; per eseguirlo abbiamo ora due possibilità:

1. Aprendo un nuovo terminale, possiamo entrare nella cartella dove abbiamo salvato il file ed eseguire il comando `python Lezione0.py`;
2. In Zed, aprendo il menu Run > Spawn Task (o Alt-Shift-T) abbiamo immediatamente a disposizione il comando `run C:/.../Lezione0.py`.

Il risultato sarà quello che probabilmente vi siete immaginati leggendo il contenuto del file: il computer mostrerà a schermo la scritta "Hello World", restituendoci dunque il controllo.

== Come te la cavi con la matematica?

Il termine "computer" significa calcolatore, no? Allora proviamo a fargli fare un'addizione:

```python
print(1+1)
```

A differenza di prima, possiamo notare che a schermo non apparirà la scritta "1+1", ma il risultato del calcolo algebrico (ovvero 2).

Nelle prossime lezioni scopriremo come funziona esattamente la sintassi del linguaggio e come esprimere tutte le operazioni che vorremo far eseguire al nostro computer.

== Commenti

Prima di continuare con lo studio del linguaggio, è importante però famigliarizzarci fin da subito con uno strumento che ci tornerà estremamente utile: i commenti.

Dato infatti che il codice può alle volte risultare complesso da comprendere a un primo sguardo, se dovessimo inserire il carattere `#` in un qualunque punto dello script, tutto ciò che lo seguirà fino alla fine della riga sarà ignorato dall'interprete, consentendoci di inserire annotazioni a piacere.

Ad esempio, il codice

```python
print("Hello World!")
# print("Ciao Mondo!")
```

stamperà a schermo esclusivamente "Hello World!" (e non "Ciao Mondo!", la cui istruzione viene ignorata).

#pagebreak()

= Git e GitHub

Citando ancora una volta Wikipedia, Git è un sistema distribuito di *controllo del versionamento*, utilizzato per gestire le varie versioni di dati e codice.

Questo significa, in poche parole, che Git ci permette di tenere traccia di tutte le modifiche apportate nel tempo ai nostri file, consentendoci di tornare a versioni precedenti, collaborare con altri sviluppatori e gestire progetti complessi in modo efficiente.

La peculiarità di Git rispetto ai suoi predecessori è il suo mantenere una *copia locale* dell'intera repository su cui effettuare le operazioni di modifica della storia, consentendoci di lavorare anche *senza connessione ad un server* centrale. Il sistema mette poi a disposizione comandi per *sincronizzare* le modifiche con il server remoto quando necessario.

GitHub, in effetti, svolge proprio quest'ultimo ruolo: nella sua essenza, non è altro che una piattaforma di hosting per repository Git che consente agli sviluppatori di condividere il proprio codice, collaborare su progetti e gestire il versionamento da una interfaccia web.

Per il nostro corso, come accennato in precedenza, ci appoggremo alla repository GitHub https://github.com/fondazioneedulife/lambdapygit, su cui caricheremo gli esercizi e i progetti che andremo a sviluppare durante le lezioni.

== Creazione del nostro fork

Visto appunto che nel corso dei vari laboratori lavoreremo tutti sullo stesso progetto, per evitare di sovrascrivere il lavoro degli altri è buona norma creare un *fork* della repository originale e sincronizzare le proprie modifiche attraverso una Pull Request solo in un secondo momento, una volta sicuri di essere pronti a "inviare" il proprio lavoro.

Per creare un fork della repository centrale (detta "upstream"), apriamola nel nostro browser e selezioniamo il pulsante "Fork" in alto a destra nella pagina che compare.

Questo creerà una copia della repository sotto il nostro account GitHub, su cui potremo lavorare liberamente senza influenzare il progetto originale.

== Clonazione del nostro fork

Siamo quasi pronti per iniziare a lavorare in locale. Prima di procedere, però, è necessario installare Git sul nostro computer; per fare ciò, visitiamo il sito ufficiale https://git-scm.com/downloads (https://311to.site/as) e scarichiamo l'ultima versione stabile adatta al proprio sistema operativo (Windows, macOS o Linux).

Una volta installato Git, apriamo un terminale (Prompt dei comandi su Windows, Terminale su macOS e Linux) e configuriamo il nostro nome utente e la nostra email con i seguenti comandi:

```bash
git config --global user.name "Nome Cognome"
git config --global user.email "io@domain.tld"
```

Successivamente, recuperiamo l'indirizzo per clonare in locale il nostro fork cliccando sul pulsante "Code" nella sua pagina web.

A questo punto, rechiamoci nella cartella del corso che abbiamo creato in precedenza per il nostro primo script Python (ad esempio, `cd /path/to/your/project`) ed eseguiamo il comando:

```bash
git clone [indirizzo copiato]
```

Questo creerà una nuova cartella contenente tutti i file della repository, tra cui le cartelle `docente/` e `studenti/`; spostiamoci nella seconda di queste con:

```bash
cd lambdapygit/studenti
```

e creiamo la nostra cartella studente da nominare secondo il pattern `ncognome` (iniziale del nome + cognome; ad esempio, `rsacchetto`) con:

```bash
mkdir ncognome
```

Infine, spostiamo al suo interno lo script Python creato poco fa ed effettuiamo il primo commit con i comandi:

```bash
git add .
git commit -m "[Breve riassunto delle modifiche fatte]"
```

Fatto, ora il nostro script è versionato all'interno della copia locale della repo Git! Per caricarlo su GitHub, però, è necessario ancora un piccolo passaggio:

```bash
git push
```

Questo comando caricherà su GitHub le modifiche al nostro fork, pronte da essere eventualmente integrate nella repository principale tramite una Pull Request.

In effetti, si potrebbe ora tornare alla pagina web del nostro fork e, dopo averla ricaricata per assicurarsi che le modifiche siano state applicate, fare click sul pulsante "Contribute" per inviare il tutto upstream.

Si noti che questa prima operazione di merge dovrà essere approvata manualmente dal docente prima di essere effettivamente applicata alla repository principale, mentre dalle volte successive sarà sufficiente commentare `/merge` nella Pull Request per far sì che venga accettata automaticamente dal sistema.

Abbiamo finito (per ora)! Nelle prossime lezioni vedremo più nel dettaglio come lavorare con Git per facilitare la collaborazione su progetti condivisi tra più persone.
