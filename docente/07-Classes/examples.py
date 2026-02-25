# 07 - Introduzione alle Classi
# Esempi tratti dalla dispensa


from __future__ import annotations


# Esempio 1: Funzione che accetta un dizionario utente
# In questo esempio definiamo una funzione 'mostra_eta' che accetta
# un dizionario rappresentante un utente con chiavi 'nome' e
# 'anno_nascita'. La funzione calcola l'età dell'utente e la stampa.

def mostra_eta(utente: dict[str, str | int]):
    eta = 2025 - utente["anno_nascita"]   # pyright: ignore
    print(f"{utente['nome']} ha {eta} anni")

utente = {
    "nome": "Riccardo",
    "anno_nascita": 2003
}
mostra_eta(utente)  # "Riccardo ha 22 anni"


# Esempio 2: Input di tipo errato
# In questo esempio chiamiamo la funzione 'mostra_eta' con
# un dizionario che rappresenta un'auto invece di un utente.

auto = {
    "modello": "Lancia Ypsilon",
    "immatricolazione": 2005
}
#mostra_eta(auto)   # Togli il commento per vedere l'errore di tipo


# Esempio 3: Refactoring con le classi
# In questo esempio definiamo una classe 'Utente' con
# attributi 'nome' e 'anno_nascita', e un metodo 'mostra_eta'
# che calcola e stampa l'età dell'utente.

class Utente:
    def __init__(self, nome: str, anno_nascita: int):
        self.nome: str = nome
        self.anno_nascita: int = anno_nascita

    def mostra_eta(self):
        eta = 2025 - self.anno_nascita
        print(f"{self.nome} ha {eta} anni")

utente = Utente("Riccardo", 2003)
utente.mostra_eta()


# Esempio 4: Gestione dello stato con le classi
# In questo esempio definiamo una classe 'Studente' che
# mantiene una lista di voti e fornisce metodi per aggiungere
# voti e calcolare la media.

class Studente:
    def __init__(self, matricola: str):
        self.matricola: str = matricola
        self.voti: list[int] = []

    def aggiungi_voto(self, voto: int):
        self.voti.append(voto)

    def media_voti(self) -> float:
        return sum(self.voti) / len(self.voti)

    def media_laurea(self) -> float:
        media = self.media_voti()
        return media * 110 / 30

studente1 = Studente("VR123456")

studente1.aggiungi_voto(28)
studente1.aggiungi_voto(30)
print(studente1.media_voti())
print(studente1.media_laurea())


# Esempio 6: Inapsulamento dei dati
# In questo esempio definiamo una classe 'Misura' che
# incapsula una misura in metri e fornisce metodi per
# convertire la misura in chilometri. Inoltre, definiamo
# funzioni che utilizzano la classe 'Misura' per calcolare
# l'area di una stanza e il tempo di viaggio.

class Misura:
    def __init__(self, metri: float):
        self.metri: float = metri

    def in_metri(self) -> float:
        return self.metri

    def in_chilometri(self) -> float:
        return self.metri / 1000

def calcola_area_stanza(lunghezza: Misura, larghezza: Misura) -> float:
    return lunghezza.in_metri() * larghezza.in_metri()

def calcola_tempo_viaggio(distanza: Misura) -> float:
    distanza_km = distanza.in_chilometri()
    velocita = 130  # km/h
    return distanza_km / velocita

stanza = calcola_area_stanza(Misura(5), Misura(3))
vrsud_valdagno = calcola_tempo_viaggio(Misura(55_000))
print(stanza)
print(vrsud_valdagno)


# Esempio 7: Miglioramento delle classi con Magic Methods
# In questo esempio miglioriamo le classi 'Studente' e 'Misura'
# aggiungendo metodi speciali (Magic Methods) per migliorare
# la loro usabilità, come la rappresentazione in stringa,
# il confronto di uguaglianza e l'operatore di somma.

class StudenteExt:
    def __init__(self, matricola: str):
        self.matricola: str = matricola
        self.voti: list[int] = []

    def aggiungi_voto(self, voto: int):
        self.voti.append(voto)

    def media_voti(self) -> float:
        return sum(self.voti) / len(self.voti)

    def media_laurea(self) -> float:
        media = self.media_voti()
        return media * 110 / 30

    def __str__(self) -> str:
        return f"Studente(matricola={self.matricola}, voti={self.voti})"

studente2 = StudenteExt("VR654321")
studente2.aggiungi_voto(27)
studente2.aggiungi_voto(29)
print(studente2)

class MisuraExt:
    def __init__(self, metri: float):
        self.metri: float = metri

    def in_metri(self) -> float:
        return self.metri

    def in_chilometri(self) -> float:
        return self.metri / 1000

    def __add__(self, other: MisuraExt) -> MisuraExt:
        return MisuraExt(self.metri + other.metri)

    def __eq__(self, other: object) -> bool:
        return type(other) is MisuraExt and self.metri == other.metri

m1 = MisuraExt(500)
m2 = MisuraExt(300)
m3 = m1 + m2
print(m3.in_chilometri())
print(MisuraExt(500) == MisuraExt(500))
