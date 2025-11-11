// == Imports ==

#import "../common/typst/cover.typ": handout_cover
#import "../common/typst/utils.typ": slidew, center_url


// == Setup ==

#let title = "Basi di Git"
#let course = "Python: da Zero a OOP"
#let description = "Basato sul libro \"Pro Git\" di S. Chacon et al. (CC BY-NC-SA 3.0)"
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
  description: description,
  author: author, email: email
)

#set page(numbering: "1")

= Una soluzione in cerca di un problema?

Per uno studente che si avvicina per la prima volta alla programmazione, la complessità di un sistema di controllo del versionamento come Git può apparire soverchiante e, per i primi piccoli progetti, qualcosa di diversamente utile.

Man mano che si avanza nello studio della programmazione, però, la necessità di un sistema di versionamento diventa sempre più evidente: collaborare con altri sviluppatori, tenere traccia delle modifiche apportate al codice, sperimentare nuove funzionalità senza compromettere il lavoro svolto sono solo alcune delle ragioni per cui Git diventa uno strumento indispensabile.

In queste pagine andremo a esplorare le basi di Git, imparando a utilizzare i comandi fondamentali e a comprendere il flusso di lavoro tipico di un progetto versionato con Git.

= Cos'è Git?

Come anticipato nell'introduzione al corso, Git è un sistema di controllo di versione distribuito, creato da Linus Torvalds nel 2005 per gestire lo sviluppo del kernel Linux.

Ma cosa vuol dire "controllo del versionamento"? In sostanza, Git è in grado di tenere traccia di tutte le modifiche apportate ai file di un progetto nel tempo, conservando una sorta di backup del lavoro svolto consentendoci non solo di recuperare l'ultima versione del codice qualora dovessimo commettere un errore, ma anche di esplorare la storia del progetto e vedere chi e quando ha apportato quali modifiche, potenzialmente risalendo al momento esatto in cui un bug particolarmente insidioso è stato introdotto nella codebase:

#align(center)[
  #image("./images/01-version_database.png", width: 30%)
]

E cosa intendiamo invece per "distribuito"? Banalmente, significa che ogni sviluppatore possiede in locale una copia completa del repository, riuscendo così a lavorare offline in modo indipendente dal server centrale. Questo approccio offre numerosi vantaggi, tra cui una maggiore velocità nelle operazioni locali e una maggiore resilienza del sistema, in quanto non dipendente da un singolo punto di fallimento:

#align(center)[
  #image("./images/02-distribuited.png", width: 35%)
]

#pagebreak()

= Come "ragiona" Git?

== Snapshots, ma non semplici copie

L'elemento fondamentale di Git (per quanto ci riguarda in questo momento, almeno) è il *commit*. Un commit rappresenta uno "snapshot" dello stato del progetto in un dato momento, includendo tutte le modifiche apportate ai file rispetto al commit precedente.

Internamente, Git tratta la storia del nostro repository come un flusso di versioni di file (le righe dello schema riportato qui sotto) raccolte appunto in tali commit (le colonne):

#align(center)[
  #image("./images/03-snapshots.png", width: 80%)
]

Si noti che, a differenza di quanto potremmo fare noi copia-incollando tutto il nostro progetto ogni volta che ne vogliamo salvare un backup, Git andrà a fare un uso pesante del linking per riutilizzare i dati che rimangono invariati da un commit all'altro ed evitare dunque di sprecare spazio inultilmente.

Il risultato sarà quindi che uno stesso file, se non modificato, apparterrà a più commit contemporaneamente, conferendo alla rappresentazione interna dello storico una struttura ad albero.

== Git gestisce l'integrità dei dati

Altra caratteristica fondamentale di Git è la sua capacità di garantire l'integrità dei dati: prima di essere salvato, ogni commit è infatti identificato in modo univoco da un hash SHA-1, che funge da "impronta digitale" del contenuto del commit stesso. A titolo di esempio, un hash SHA-1 di un commit potrebbe essere:

```
24b9da6552252987aa493b52f8696cd6d3b00373
```

Questo hash, calcolato a partire non solo dal contenuto dei file, ma anche dai metadati del commit (come l'autore, la data, il messaggio e il predecessore nello storico), permette a Git di rilevare qualsiasi modifica non autorizzata ai dati. Se qualcuno tentasse infatti di alterare il contenuto di un commit o vi fosse una corruzione dei dati, l'hash risultante non corrisponderebbe più a quello originale, segnalando così un potenziale problema.

== Git non elimina mai\* dati

Per come è progettato, Git espone quasi esclusivamente operazioni che _aggiungono_ dati al database, mai che li rimuovono in modo definitivo. In genere risulta quindi molto difficile fare modifiche che causano una perdita irreversibile di dati; certo, è sempre possibile sovrascrivere per errore le modifice di cui non è ancora stato fatto il commit, ma una volta che qualcosa è stato "catturato" nella storia del progetto è facile annullare modifiche indesiderate.

#pagebreak()

= I tre stati di un file in Git

Iniziamo ora a vedere come funziona Git in pratica, partendo dal concetto dei tre stati in cui può trovarsi un file all'interno di un repository Git. Costruire il proprio modello mentale del sistema attorno a questo concetto è fondamentale per utilizzare efficacemente Git senza rischiare di smarrirsi tra i vari comandi disponibili, quindi assicurati di comprenderlo bene prima di continuare lo studio.

Git ha tre stati principali in cui il file può trovarsi: _Modified_, _Staged_ e _Committed_:

- _Modified_ siginfica che il file è stato cambiato rispetto all'ultima versione salvata nel repository, ma queste modifiche non sono ancora state preparate per essere salvate nel prossimo commit;
- _Staged_ indica che le modifiche al file sono state marcate per essere incluse nel prossimo commit;
- _Committed_ significa che le modifiche sono state salvate definitivamente nel repository come parte della storia del progetto.

Ne consegue che dovranno esistere tre aree distinte in cui un file può trovarsi all'interno di un repository Git, corrispondenti a questi stati: il _working tree_, la _staging area_ e la _Git directory_:

#align(center)[
  #image("./images/04-three_states.png", width: 60%)
]

- L'area di lavoro (*working tree*) è una singola copia di una versione del progetto. Questi file vengono estratti dal database compresso presente nella directory di Git e posizionati sul disco, pronti per essere utilizzati o modificati;
- L'area di staging (*staging area*) è un file, generalmente contenuto nella directory di Git, che memorizza le informazioni su ciò che verrà incluso nel prossimo commit. Il suo nome tecnico nel gergo di Git è “index”, ma il termine “staging area” è altrettanto valido;
- La directory di Git (*Git directory*) è il luogo in cui Git conserva i metadati e il database degli oggetti relativi al progetto. Questa è la parte più importante di Git, ed è ciò che viene copiato quando si clona un repository da un altro computer;

Il flusso di lavoro di base in Git si svolge più o meno così:

- Modifichi i file nell'area di lavoro;
- Selezioni e aggiungi solo le modifiche che desideri includere nel prossimo commit, inserendo solo queste modifiche nell'area di staging;
- Esegui un commit, che prende i file così come sono nell'area di staging e salva in modo permanente quello snapshot nella directory di Git.

Se una particolare versione di un file si trova nella directory di Git, si considera *committed*. Se è stata modificata e aggiunta all'area di staging, è *staged*. Se è stata cambiata dopo il checkout ma non è stata aggiunta all'area di staging, è *modified*.

#pagebreak()

= Ottenere una repository Git

Se sei pronto a iniziare a lavorare con Git, esistono due modi per ottenere una repo. Quello più comune per chi collabora a un progetto esistente è clonare una repository remota, esattamente come abbiamo fatto nella lezione introduttiva del corso (a cui si rimanda), mentre l'altro metodo, che andremo ora a vedere, è quello di inizializzare una nuova repository da zero.

Quest'ultima procedura è in genere necessaria quando si inizia un nuovo progetto e non si dispone ancora di una codebase esistente da modificare, ma si desidera iniziare a tracciare del nuovo codice.

Come per un qualunque progetto è innanzitutto imprescindibile creare una nuova cartella in cui andremo a posizionare i nostri file e, una volta fatto ciò, navigarci all'interno utilizzando il comando `cd`:

```bash
cd /path/to/my/project
```

In questo modo sarà possibile procedere con l'inizializzazione vera e propria del repository Git:

```bash
git init
```

Nota che il comando `git init` funziona anche in cartelle in cui sono già presenti dei file: in questo caso, Git inizializzerà la repository senza sovrascrivere o eliminare alcun file esistente, limitandosi a marcare come _untracked_ tutto ciò che troverà.

#pagebreak()

= Lavorare con Git

A questo punto dovresti avere davanti una repository Git su cui sperimentare. In genere, vorrai iniziare a fare modifiche ai file al suo interno e salvare degli snapshot di essi ogniqualvolta il progetto raggiunga uno stato che desideri registrare (ad esempio, a fronte della conclusione dell'implementazione di una particolare feature).

Ricorda che ogni file nella tua directory di lavoro può trovarsi in uno di due stati: tracciato (_tracked_) o non tracciato (_untracked_). I file tracciati sono quelli che erano presenti nell’ultimo snapshot, oltre a qualsiasi nuovo file che sia stato aggiunto manualmente all’area di staging; questi possono essere non modificati, modificati o già preparati per il commit (_staged_). In breve, i file tracciati sono quelli di cui Git è a conoscenza.

I file non tracciati (_untracked_) sono tutto il resto, qualsiasi file nella tua directory di lavoro che non era presente nell’ultimo snapshot e non si trovi nell’area di staging. Quando cloni una repository per la prima volta, tutti i tuoi file saranno tracciati e non modificati, perché Git li ha appena estratti e tu non hai ancora modificato nulla; quando crei una nuova repository, di contro, tutti i file nello spazio di lavoro sono visti da Git come nuovi e devono essere aggiunti manualmente all’area di staging prima di poter essere inclusi in un commit.

Quando modifichi il contenuto di un file, Git lo considera automaticamente come variato rispetto all’ultimo commit, tuttavia puoi decidere di selezionare e aggiungere all’area di staging solo i file che desideri effettivamente includere nel prossimo commit prima di andare a generarlo. Questo ciclo si ripete ogni volta che apporti nuove modifiche al progetto.

#align(center)[
  #image("./images/05-file_status_lifecycle.png", width: 60%)
]

== Controllare lo stato dei tuoi file

Lo strumento fondamentale per determinare in quale stato si trovano i tuoi file è il comando `git status`. Se esegui questo comando subito dopo aver creato una nuova repository, dovresti vedere qualcosa del tipo:

```
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

Questo output ti informa che ti trovi sul branch principale (`main`), che non esistono ancora commit e che non ci sono modifiche da salvare: la tua directory di lavoro è "pulita".

== Aggiungere un nuovo file

Proviamo allora ad aggiungere un file `Io.txt`:

```bash
echo "Riccardo" > Io.txt
```

L'output dovrebbe cambiare in qualcosa del tipo:

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	Io.txt

nothing added to commit but untracked files present (use "git add" to track)
```

Questo significa che Git si è reso conto dell'esistenza di `Io.txt` ma che non lo sta ancora tracciando: il file è infatti nello stato _untracked_. Per includerlo nel prossimo commit, dobbiamo prima aggiungerlo all'area di staging utilizzando il comando `git add`:

```bash
git add Io.txt
```

A questo punto, lo `status` della repo dovrebbe essere:

```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   Io.txt
```

Come prevedevamo, `Io.txt` è ora nello stato _staged_, pronto per essere incluso nel prossimo commit. Se volessimo annullare questa operazione è possibile utilizzare il comando `git restore --staged Io.txt` per riportare il file allo stato _untracked_, ma quello che vogliamo fare ora è procedere con il commit vero e proprio:

```bash
git commit -m "Aggiunto il mio primo file"
```

il quale dovrebbe produrre un output simile a questo:

```
[main (root-commit) bd9f7e3] Aggiunto il mio primo file
 1 file changed, 1 insertion(+)
 create mode 100644 Io.txt
```

Nota l'uso del parametro `-m` per specificare il messaggio di commit direttamente da linea di comando: in assenza di questo parametro, Git aprirà l'editor di testo predefinito per permetterti di scrivere un messaggio più dettagliato. Il messaggio di commit è sempre obbligatorio ed è fondamentale per capire a colpo d'occhio quali modifiche introduce alla codebase, pertanto ricordati di scriverlo sempre in modo chiaro e conciso!

Dopo aver eseguito il commit, lo `status` della repo dovrebbe confermarci che ora esiste uno snapshot e che non ci sono più file modificati o non tracciati:

```
On branch main
nothing to commit, working tree clean
```

== Modificare un file esistente

Vediamo ora cosa succede modificando un file esistente:

```bash
echo "Riccardo Sacchetto" > Io.txt
```

`git status` dovrebbe farci presente come un file precedentemente tracciato sia stato modificato:

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   Io.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

Come prima, possiamo allora procedere allo staging (`git add Io.txt`):

```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   Io.txt
```

e al commit (`git commit -m "Inserito il cognome"`):

```
On branch main
nothing to commit, working tree clean
```

Nota che Git è in grado di tenere automaticamente traccia di tutti i tipi di modifica ad un file. Se dovessimo ad esempio spostarlo in una sottocartella documenti:

```bash
mkdir documenti
mv Io.txt documenti/
git add .               # Il punto indica la cartella corrente, quindi tutta la repo
git status
```

```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	renamed:    Io.txt -> documenti/Io.txt
```

Oppure, se dovessimo rimuoverlo:

```bash
rm Io.txt
git add .
git status
```

```
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	deleted:    Io.txt
```

== Viaggiare nel tempo

E se volessimo annullare l'ultima modifica fatta a `Io.txt`? In questo caso non ci resta che imparare a viaggiare nel tempo con Git!

Vediamo innanzitutto come consultare lo stato dell'intera linea temporale memorizzata nella repo con il comando `git log`:

```
commit b8b8d85f78e3b9e53d4efa160ef430f0250d62b7 (HEAD -> main)
Author: Riccardo Sacchetto <rsacchetto@nexxontech.it>
Date:   Sat Nov 8 22:52:26 2025 +0100

    Inserito il cognome

commit bd9f7e38980e136f64cc66b017af38737397b8a2
Author: Riccardo Sacchetto <rsacchetto@nexxontech.it>
Date:   Sat Nov 8 22:50:24 2025 +0100

    Aggiunto il mio primo file
```

Questo output ci mostra i due commit che abbiamo fatto finora, con il loro hash univoco, l'autore, la data e il messaggio di commit. Se dovessimo disegnare la linea temporale avermmo qualcosa del tipo:

#align(center)[
  #image("./images/06-history01.png", width: 60%)
]

dove i rettangoli gialli rappresentano i commit, l'etichetta `main` punta al commit in testa alla linea temporale e la pedina indica lo stato di cui abbiamo fatto il checkout:

Supponiamo ora di voler fare il checkout del commit precedente per vedere come il file `Io.txt` appariva prima dell'ultima modifica. Per fare ciò, possiamo utilizzare il comando `git checkout` seguito dall'hash del commit a cui vogliamo tornare:

```bash
git checkout bd9f7e38980e136f64cc66b017af38737397b8a2
```

```
Note: switching to 'bd9f7e38980e136f64cc66b017af38737397b8a2'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at bd9f7e3 Aggiunto il mio primo file
```

Questo messaggio ci informa che siamo ora in uno stato di _detached HEAD_, ovvero che abbiamo temporaneamente abbandonato il regolare flusso della storia della nostra repo per tornare indietro a un particolare istante temporale:

#align(center)[
  #image("./images/07-history02.png", width: 60%)
]

In questo stato possiamo esplorare il codice come era in quel momento specifico, ma qualsiasi modifica che facciamo non sarà associata a un branch e potrebbe essere persa se non dovessimo taggarla correttamente.

Per tornare al branch principale e riprendere il lavoro da dove lo avevamo lasciato, possiamo utilizzare il comando:

```bash
git checkout main
```

== Annullare i nostri errori

Cosa succede se, dopo aver fatto delle modifiche, ci rendiamo conto di aver commesso un errore e vogliamo annullare le modifiche apportate? La capacità di Git di viaggiare nel tempo ci permette di farlo facilmente.

Analizziamo innanzitutto il caso in cui abbiamo modificato un file ma non abbiamo ancora fatto il commit; supponiamo ad esempio di aver cambiato `Io.txt` ma di voler tornare alla versione dell'ultimo commit:

```bash
echo "Tizio Caio" > Io.txt
```

Quello che possiamo fare è utilizzare il comando `git restore` per annullare le modifiche (*Attenzione*: questo comando sovrascriverà il file con la versione dell'ultimo commit, perdendo le modifiche non salvate!):

```bash
git restore Io.txt
```

Ma se avessimo invece già fatto il commit delle modifiche e volessimo annullare l'ultimo commit?

```bash
echo "Tizio Caio" > Io.txt
git add Io.txt
git commit -m "Modifica che non dovrei fare"
```

```
[main 4f07478] Modifica che non dovrei fare
 1 file changed, 1 insertion(+), 1 deletion(-)
```

#align(center)[
  #image("./images/08-history03.png", width: 60%)
]

In questo caso, possiamo utilizzare il comando `git reset --hard HEAD^`, che riporta la testa della nostra linea temporale al commit immediatamente precedente:

```
HEAD is now at b8b8d85 Inserito il cognome
```

#align(center)[
  #image("./images/09-history04.png", width: 60%)
]

Nota che, come dicevamo prima, Git non elimina immediatamente il commit "sbagliato", proprio per evitare che un nostro errore possa causare una perdita irreversibile di dati. Tuttavia, dopo un certo periodo di tempo, Git potrebbe eseguire una pulizia automatica dei commit non più raggiungibili, quindi è sempre meglio agire con cautela quando si utilizzano comandi che modificano la storia del repository.

Se per assurdo volessimo procedere immediatamente alla sua rimozione dovremmo eseguire il ricalcolo dei commit raggiungibili e forzare la pulizia del database con:

```bash
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

Ma questo è un caso limite che difficilmente si presenterà durante il normale utilizzo di Git.

== Linee temporali (quasi) parallele: i branch

Un altro concetto fondamentale in Git è quello dei branch, che permettono di creare linee temporali parallele all'interno dello stesso repository. I branch sono utili per sviluppare nuove funzionalità, correggere bug o sperimentare idee senza interferire con il lavoro principale svolto sul branch `main`.

Immaginiamo ad esempio il caso in cui stiamo lavorando su una nuova funzionalità per il nostro progetto. Invece di apportare modifiche direttamente al branch `main` e rischiare di interferire con il lavoro dei colleghi, possiamo creare un nuovo branch dedicato a questa funzionalità e spostarci su di esso:

```bash
git branch test
git checkout test
```

#align(center)[
  #image("./images/10-branches01.png", width: 60%)
]

In questo modo, da questo momento in avanti tutti i commit che faremo seguiranno una nuova timeline parallela, originatasi dal commit in cui ci trovavamo quando abbiamo fatto il branching:

#align(center)[
  #image("./images/11-branches02.png", width: 60%)
]

In ogni momento possiamo poi decidere di far riconfluire il branch `test` all'interno di `main` utilizzando il comando `git merge`, che, trattandosi questo caso di un semplice avanzamento della linea temporale, corrisponde 1:1 all'esecuzione di `git reset --hard test`:

#align(center)[
  #image("./images/12-branches03.png", width: 60%)
]

Questo ovviamente è il caso più banale di merge possibile, in cui il branch `test` si trova "in avanti" rispetto a `main` senza che vi siano state modifiche concorrenti. E se volessimo invece unire due branch che hanno apportato modifiche differenti allo stesso file?

#align(center)[
  #image("./images/13-branches04.png", width: 60%)
]

Anche in questo caso, Git sarà in grado di combinare automaticamente le modifiche a fronte del comando `git merge`, fondendo le due linee temporali in un unico flusso attraverso un commit di giunzione (_merge commit_):

#align(center)[
  #image("./images/14-branches05.png", width: 60%)
]

== Anomalie spazio-temporali: i merge conflict

Ma cosa accadrebbe se, mentre stiamo lavorando sul branch `test`, un nostro collega apportasse involontariamente delle modifiche al branch `main` che vanno in conflitto con le nostre? Immaginiamo ad esempio che entrambi abbiamo modificato lo stesso file `Io.txt` in modi differenti:

```bash
# == Modifica su main: ==
echo "Modifica 1" >> Io.txt

# == Modifica su test: ==
echo "Modifica 2" >> Io.txt
```

In questo caso, quando tenteremo di fare il merge del branch `test` in `main`, Git ci segnalerà un *merge conflict*:

```
Auto-merging Io.txt
CONFLICT (content): Merge conflict in Io.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Git non sarà in grado di risolvere automaticamente il conflitto, poiché non sa quale delle due modifiche debba prevalere (e, come già ripetuto altre volte, farà di tutto per non farci perdere dati).

Sarà quindi nostro compito aprire il file `Io.txt`, individuare le sezioni in conflitto (segnalate da Git con appositi marcatori) e decidere manualmente come risolverle, scegliendo quale versione mantenere o combinando le modifiche in modo appropriato prima di procedere con un nuovo commit per finalizzare il merge:

```
Riccardo Sacchetto
<<<<<<< HEAD
Modifica 1
=======
Modifica 2
>>>>>>> test
```

== Traslare la divergenza: il rebase

Pensiamo ora ad un altro caso comune nel lavoro quotidiano: una volta creato un nuovo branch e lavorato per qualche giorno a una feature facendo commit su di esso, notiamo che su `main` i nostri colleghi hanno apportato delle modifiche importanti che vorremmo integrare nel nostro branch prima di procedere con il merge, un po' per evitare conflitti e un po' per testare la nostra feature con il codice più aggiornato possibile:

#align(center)[
  #image("./images/15-branches06.png", width: 60%)
]

Sicuramente potremmo fare un semplice merge di `main` in `test`, ma in questo modo la storia del progetto diventerebbe più complessa e difficile da seguire, con commit di merge che potrebbero confondere chiunque stia cercando di capire l'evoluzione del codice.

In questi casi, una strategia più pulita è quella del *rebase*, che consiste nel "traslare" la nostra serie di commit su `test` in cima alla storia di `main`, come se avessimo iniziato a lavorare sulla nostra feature partendo dall'ultima versione di `main`:

#align(center)[
  #image("./images/16-branches07.png", width: 60%)
]

Si noti come eseguire il rebase non cancelli la storia originale del branch `test`, ma ne crei una che riflette la nuova base su cui sono state applicate le modifiche; trascorso un certo periodo di tempo, se non dovessimo adoperarci per recuperarla, questa verrà eliminata automaticamente dal garbage collector.

#pagebreak()

= Collaborare con Git

L'ultimo pilastro fondamentale di Git è la sua capacità di facilitare la collaborazione tra più sviluppatori su uno stesso progetto, sincronizzando le modifiche apportate localmente con repository su altri dispositivi.

Immaginiamo ad esempio il caso seguente:

#align(center)[
  #image("./images/17-collaboration01.png", width: 60%)
]

Come si può vedere, in questa situazione ci ritroviamo con due repo separate: la nostra (in basso), fornita esclusivamente del root-commit, e quella del nostro amico (in alto), a cui è stato aggiunto un secondo commit.

== Scaricare modifiche da una repo remota

Il primo passo che vorremo eseguire in questa situazione è sicuramente quello di sincronizzare la nostra repo con quella del nostro amico, scaricando le modifiche apportate da quest'ultimo. Per fare ciò, utilizziamo innanzitutto il comando `git fetch`, che recupera i nuovi commit dalla repository remota senza modificare lo stato attuale del nostro database locale:

```
From /path/to/remote/repo
   4eb5522..4502330  main -> friend/main
```

#align(center)[
  #image("./images/18-collaboration02.png", width: 60%)
]

In questo modo abbiamo scaricato i nuovi commit dalla repo del nostro amico, che si presentano ora come un branch separato rispetto al nostro main (_remote branch_). Per fare in modo che il nostro `main` rifletta queste modifiche, non ci rimane che eseguire il comando `git pull`, il quale andrà essenzialmente a effettuare un merge tra il branch remoto e quello locale:

```
Updating 9f475a3..b0db7f1
Fast-forward
 Io.txt | 1 +
 1 file changed, 1 insertion(+)
```

#align(center)[
  #image("./images/19-collaboration03.png", width: 60%)
]

== Spedire modifiche ad una repo remota

Supponiamo ora di trovarci nel caso opposto: dopo aver scaricato le modifiche del nostro amico, abbiamo apportato degli aggiornamenti al codice e vogliamo condividerli con lui:

#align(center)[
  #image("./images/20-collaboration04.png", width: 60%)
]

Per fare ciò, utilizziamo il comando `git push`, che invia i nostri commit locali alla repository remota:

```
To /path/to/remote/repo
   b0db7f1..c8844c1  main -> main
```

#align(center)[
  #image("./images/21-collaboration05.png", width: 60%)
]
