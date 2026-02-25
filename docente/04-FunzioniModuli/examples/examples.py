# 04 - Funzioni e Moduli
# Esempi tratti dalla dispensa

# Esempio 1: Definizione di funzioni semplici
# In questo esempio definiamo quattro funzioni per eseguire operazioni aritmetiche di base:
# - addizione: somma due numeri che l'utente inserisce
# - sottrazione: sottrae due numeri che l'utente inserisce
# - moltiplicazione: moltiplica due numeri che l'utente inserisce
# - divisione: divide due numeri che l'utente inserisce e calcola quoziente, quoto e resto

def addizione():
    val1: int = int(input("Primo addendo: "))
    val2: int = int(input("Secondo addendo: "))
    somma: int = val1 + val2
    print(f"Somma: {somma}")

def sottrazione():
    val1: int = int(input("Minuendo: "))
    val2: int = int(input("Sottraendo: "))
    differenza: int = val1 - val2
    print(f"Differenza: {differenza}")

def moltiplicazione():
    val1: int = int(input("Primo fattore: "))
    val2: int = int(input("Secondo fattore: "))
    prodotto: int = val1 * val2
    print(f"Prodotto: {prodotto}")

def divisione():
    val1: int = int(input("Dividendo: "))
    val2: int = int(input("Divisore: "))
    quoziente: float = val1 / val2
    quoto: int = val1 // val2
    resto: int = val1 % val2
    print(f"Quoziente: {quoziente}")
    print(f"Quoto: {quoto}")
    print(f"Resto: {resto}")

operazione: str = input("Operazione da eseguire [+, -, *, /]: ")
if operazione == "+":
    addizione()
elif operazione == "-":
    sottrazione()
elif operazione == "*":
    moltiplicazione()
elif operazione == "/":
    divisione()
else:
    print("Operazione non valida.")


# Esempio 2: Funzioni con parametri e valori di ritorno
# Qui definiamo una funzione che accetta due parametri (il nome e l'anno di nascita)
# e restituisce una stringa di presentazione. La chiamata della funzione avviene
# in due modi: con parametri posizionali e con parametri nominativi.

def presentazione(nome: str, anno_nascita: int) -> str:
    eta: int = 2025 - anno_nascita
    presentazione: str = f'''
    Ciao, il mio nome è {nome}!
    Sono nato nel {anno_nascita} e ho {eta} anni.
    '''
    return presentazione

nome_utente: str = input("Inserisci il tuo nome: ")
anno_nascita_utente: int = int(input("Inserisci il tuo anno di nascita: "))

messaggio_presentazione: str = presentazione(nome_utente, anno_nascita_utente)
print(messaggio_presentazione)

messaggio_presentazione = presentazione(
    nome=nome_utente,
    anno_nascita=anno_nascita_utente
)
print(messaggio_presentazione)


# Esempio 3: Funzioni con parametri opzionali
# In questo esempio definiamo una funzione per calcolare l'area di un rettangolo, permettendo
# di specificare se l'area deve essere restituita in centimetri quadrati tramite un parametro opzionale.

def area_rettangolo_conv(lunghezza: float, larghezza: float, in_centimetri: bool = False) -> float:
    area: float = lunghezza * larghezza
    if in_centimetri:
        area = area * 10000  # Converti da m² a cm²
    return area


# Esempio 4: Funzioni con più valori di ritorno
# Qui definiamo una funzione che esegue una divisione e restituisce
# tre valori: il quoziente come float, il quoto come int e il resto come int.

def divisione_completa(dividendo: int, divisore: int) -> tuple[float, int, int]:
    quoziente: float = dividendo / divisore
    quoto: int = dividendo // divisore
    resto: int = dividendo % divisore
    return quoziente, quoto, resto

dividendo_utente: int = int(input("Dividendo: "))
divisore_utente: int = int(input("Divisore: "))
quoziente_utente, quoto_utente, resto_utente = divisione_completa(
    dividendo_utente, divisore_utente
)
print(f"Quoziente: {quoziente_utente}")
print(f"Quoto: {quoto_utente}")
print(f"Resto: {resto_utente}")


# Esempio 5: Funzioni che modificano liste
# In questo esempio definiamo una funzione che accetta una lista di numeri interi,
# calcola la somma degli elementi e aggiunge la somma stessa alla fine della lista.
# Nel chiamante mostriamo come la lista originale viene modificata e come questa
# possa essere preservata utilizzando una copia della lista.

def aggiungi_somma(numeri: list[int]) -> list[int]:
    somma: int = sum(numeri)
    numeri.append(somma)
    return numeri

numeri_utente: list[int] = [1, 2, 3]
numeri_aggiornato: list[int] = aggiungi_somma(numeri_utente)
print(numeri_utente)  # Output: [1, 2, 3, 6]

numeri_utente_1: list[int] = [1, 2, 3]
numeri_aggiornato_1: list[int] = aggiungi_somma(numeri_utente_1.copy())
print(numeri_utente_1)        # Output: [1, 2, 3]
print(numeri_aggiornato_1)    # Output: [1, 2, 3, 6]


# Esempio 6 (vedi anche file `operazioni.py`): Importazione da moduli
# Qui mostriamo due modi diversi per importare ed utilizzare una funzione
# definita in un modulo esterno. Nel file `operazioni.py` è definita
# la funzione `area_rettangolo()` che calcola l'area di un rettangolo.

if True:
    import operazioni

    lunghezza_utente: float = float(input("Lunghezza del rettangolo (m): "))
    larghezza_utente: float = float(input("Larghezza del rettangolo (m): "))
    area: float = operazioni.area_rettangolo(lunghezza_utente, larghezza_utente)
    print(f"Area del rettangolo: {area} m²")

if True:
    from operazioni import area_rettangolo

    lunghezza_utente_1: float = float(input("Lunghezza del rettangolo (m): "))
    larghezza_utente_1: float = float(input("Larghezza del rettangolo (m): "))
    area_1: float = area_rettangolo(lunghezza_utente_1, larghezza_utente_1)
    print(f"Area del rettangolo: {area_1} m²")


# Esempio 7 (vedi anche carella `geometria`): Importazione da package
# In questo esempio mostriamo come importare ed utilizzare più funzioni
# da un modulo all'interno di un package. Nel package `geometria` è
# definito il modulo `rettangolo` che contiene le funzioni `area()`
# e `perimetro()` per calcolare rispettivamente l'area e il perimetro
# di un rettangolo.

if True:
    from geometria.rettangolo import area as area_rettangolo, perimetro as perimetro_rettangolo

    lunghezza_utente_2: float = float(input("Lunghezza del rettangolo (m): "))
    larghezza_utente_2: float = float(input("Larghezza del rettangolo (m): "))
    area_2: float = area_rettangolo(lunghezza_utente_2, larghezza_utente_2)
    perimetro_2: float = perimetro_rettangolo(lunghezza_utente_2, larghezza_utente_2)
    print(f"Area del rettangolo: {area_2} m²")
    print(f"Perimetro del rettangolo: {perimetro_2} m")
