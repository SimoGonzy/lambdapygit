# pyright: reportRedeclaration=false,reportUnreachable=false,reportUnnecessaryComparison=false

# 01 - Tipi di Dato e Controllo del Flusso
# Esempi tratti dalla dispensa

# Esempio 1: Dichiarazione di variabili
# In questo esempio, dichiariamo tre variabili con tipi di dato specifici:
# - nome: una stringa che rappresenta un nome
# - eta: un intero che rappresenta l'età
# - patente_b: un booleano che indica se la persona ha la patente di guida di tipo B
nome: str = "Riccardo"
eta: int = 22
patente_b: bool = True

# Esempio 2: Utilizzo di una variabile
# Qui stampiamo il valore della variabile 'username' che contiene una stringa,
# fornendo a print() la variabile come argomento.
username: str = "rsacchetto"
print(username)

# Esempio 3: Aggiornamento di variabile
# In questo esempio, mostriamo come aggiornare il valore di una variabile.
# Inizialmente, la variabile 'nome' contiene solo il nome "Riccardo".
# Successivamente, aggiorniamo 'nome' per includere anche il cognome "Sacchetto"
# e stampiamo il nuovo valore.
nome: str = "Riccardo"
print(nome)
nome = "Riccardo Sacchetto"
print(nome)

# Esempio 4: Tipi di numero
# In questo esempio, dichiariamo variabili di diversi tipi numerici:
# - intero: un numero intero
# - reale: un numero a virgola mobile (float)
# - complesso: un numero complesso con parte reale e immaginaria
intero: int = 5
reale: float = 2.5
complesso: complex = complex(5, 2.5) # 5+2.5j

# Esempio 5: Operazioni tra numeri
# Qui mostriamo alcune operazioni aritmetiche tra i numeri dichiarati sopra.
print(intero - 1)         # 4
print(intero / intero)    # 1.0
print(intero * reale)     # 12.5
print(intero + complesso) # 10+2.5j

# Esempio 6: Imprecisione dei float
# Questo esempio dimostra l'imprecisione dei numeri a virgola mobile (float) in Python.
# A causa del modo in cui i numeri float sono rappresentati in memoria, alcune operazioni
# possono produrre risultati inaspettati. Ad esempio, la somma di 0.1 e 0.2 non è esattamente 0.3.
print(0.1 + 0.2)
print(3 * 0.1)

# Esempio 7: Definizione di stringhe con virgolette singole e doppie
# In questo esempio, mostriamo come definire stringhe utilizzando sia virgolette singole
# che doppie. Entrambi i metodi sono validi in Python e possono essere usati in base alle esigenze.
test: str = "Ciao, come va?"
test: str = 'Io tutto bene, grazie. E tu?'
test: str = "Lo sapevi che ho iniziato a studiare il linguaggio 'Python'?"
test: str = 'Ieri è uscito un nuovo episodio di "The Pitt"!'
test: str = "Ieri è uscito un nuovo episodio di \"The Pitt\"!"
test: str = 'Cosa stai guardando in questi giorni?\nI nuovi episodi di "The Pitt"!'

# Esempio 8: Concatenazione di stringhe
# In questo esempio, mostriamo come concatenare (unire) più stringhe insieme
message: str = "Hello" + " " + "World"
print(message)
greeting: str = "Hello"
target: str = "World"
print(greeting + " " + target)

# Esempio 9: Cambio del casing
# Qui mostriamo come modificare il casing (maiuscole/minuscole) di una stringa
nome: str = "riccardo sacchetto"
nome = nome.title()
print(nome)            # Riccardo Sacchetto
print(nome.lower())    # riccardo sacchetto
print(nome.upper())    # RICCARDO SACCHETTO

# Esempio 10: Stripping
# In questo esempio, mostriamo come rimuovere gli spazi bianchi iniziali e finali
# di una stringa utilizzando i metodi rstrip(), lstrip() e strip()
linguaggio: str = "  python  "
print(linguaggio.rstrip())    # "  python"
print(linguaggio.lstrip())    # "python  "
print(linguaggio.strip())     # "python"

# Esempio 11: Rimozione di prefissi e suffissi
# Qui mostriamo come rimuovere specifici prefissi e suffissi da una stringa
its: str = "https://itsdigitalacademy.com"
print(its.removeprefix("https://"))    # itsdigitalacademy.com
print(its.removesuffix(".it"))         # https://itsdigitalacademy

# Esempio 12: Format strings
# In questo esempio, mostriamo come utilizzare le format string (f-string) per creare stringhe con dati dinamici
nome: str = "Riccardo"
eta: int = 2025 - 2003
output: str = f"Sono Riccardo e ho {eta} anni"
print(output)

# Esempio 13: Lettura da riga di comando
# Qui mostriamo come leggere l'input dell'utente dalla riga di comando utilizzando la funzione input()
print("Come ti chiami?")
nome: str = input("Nome: ")
print(f"Ciao, {nome}!")

# Esempio 14: Dichiarazione di booleani
# In questo esempio, dichiariamo due variabili booleane:
# - sta_piovendo: indica se sta piovendo
# - ombrello_aperto: indica se l'ombrello è aperto
# Inoltre, definiamo una terza variabile 'mi_bagno' calcata in base alle altre due
sta_piovendo: bool = True
ombrello_aperto: bool = False
mi_bagno: bool = sta_piovendo and not ombrello_aperto # True

# Esempio 15: Confronti tra numeri
# In questo esempio, mostriamo come effettuare confronti tra numeri utilizzando operatori relazionali
# e come memorizzare il risultato in variabili booleane.
eta: int = 2025 - 2003
maggiore_eta: int = 18
posso_bere: bool = eta >= maggiore_eta # True

# Esempio 16: Controllo del flusso con if-else
# Qui mostriamo come utilizzare una struttura di controllo del flusso if-else
# per eseguire codice condizionale in base al valore di una variabile booleana.
if sta_piovendo and not ombrello_aperto:
  print("Mi bagno!")
else:
  print("Resto asciutto!")

# Esempio 17: Controllo del flusso con if-elif-else
# In questo esempio, mostriamo come utilizzare una struttura di controllo del flusso
# if-elif-else per gestire più condizioni basate sul valore di una variabile numerica.
eta: int = 2025 - 2003
if eta < maggiore_eta:
  print("Sei minorenne, non puoi bere!")
elif eta == maggiore_eta:
  print("Sei appena maggiorenne, bevi con moderazione!")
else:
  print("Sei maggiorenne, puoi bere liberamente!")

# Esempio 18: Controllo del flusso con if indipendenti
# Qui mostriamo come utilizzare più istruzioni if indipendenti per eseguire codice
# condizionale basato su condizioni non correlate tra loro.
if sta_piovendo:
  print("Oggi non è una bella giornata...")
if eta >= 18:
  print("Puoi bere liberamente!")

# Esempio 19: Il ciclo while
# In questo esempio, mostriamo come utilizzare un ciclo while per eseguire
# un blocco di codice ripetutamente fintantoché una condizione è vera.
energia: int = 100
while energia != 0:
  print("Sono carico! Continuiamo a studiare Python!")
  energia = energia - 1
print("Ora sono stanco...")

# Esempio 20: Trasformazioni arbitrarie della guardia
# Qui mostriamo come modificare una variabile di controllo all'interno del ciclo while
# per influenzare la durata del ciclo stesso.
abbiamo_caffe: bool = True
energia: int = 100
while energia != 0:
  print("Sono carico! Continuiamo a studiare Python!")
  if energia <= 50 and abbiamo_caffe:
    abbiamo_caffe = False
    energia = energia + 10
  else:
    energia = energia - 1
print("Ora sono stanco...")

# Esempio 21: Il ciclo for
# In questo esempio, mostriamo come utilizzare un ciclo for per iterare su una sequenza di numeri
# generata dalla funzione range(). Il ciclo stampa i numeri da 0 a 9.
for num in range(0, 10):
  print(num)

# Esempio 22: Ciclo for su stringhe
# Qui mostriamo come utilizzare un ciclo for per iterare su ogni carattere di una stringa
# e stampare ciascun carattere singolarmente.
for char in "Ciao!":
  print(char)
