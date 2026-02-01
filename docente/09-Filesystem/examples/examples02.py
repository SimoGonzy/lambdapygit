# 09 - Lavorare con il filesystem
# Esempi tratti dalla dispensa

# Esempio 2: Lettura e scrittura con approccio OOP
# In questo esempio, gestiamo un portafoglio di transazioni finanziarie
# utilizzando metodi di (de)serializzazione all'interno delle classi
# per leggere e scrivere su un file CSV.


from __future__ import annotations
from pathlib import Path


class Transazione:
    def __init__(self, importo: float, data: str, categoria: str):
        self.importo: float = importo
        self.data: str = data
        self.categoria: str = categoria

    @classmethod
    def from_csv(cls, csv_string: str) -> Transazione:
        campi: list[str] = csv_string.strip().split(",")

        importo: float = float(campi[0])
        data: str = campi[1]
        categoria: str = campi[2]
        return cls(importo, data, categoria)

    def to_csv(self) -> str:
        return f"{self.importo},{self.data},{self.categoria}"

class Portafoglio:
    def __init__(self):
        self.transazioni: list[Transazione] = []

    @classmethod
    def from_csv(cls, csv_string: str) -> Portafoglio:
        portafoglio: Portafoglio = cls()
        righe: list[str] = csv_string.strip().split("\n")
        for riga in righe[1:]:
            transazione: Transazione = Transazione.from_csv(riga)
            portafoglio.aggiungi_transazione(transazione)
        return portafoglio

    def aggiungi_transazione(self, transazione: Transazione):
        self.transazioni.append(transazione)

    def calcola_saldo(self) -> float:
        return sum([ t.importo for t in self.transazioni ])

    def to_csv(self) -> str:
        righe: list[str] = [ "importo,data,categoria" ]  # Header
        for t in self.transazioni:
            righe.append(t.to_csv())
        return "\n".join(righe)

file: Path = Path("./transazioni.csv")
with file.open("r", encoding="utf-8") as transazioni:
    contenuto: str = transazioni.read()
    portafoglio: Portafoglio = Portafoglio.from_csv(contenuto)

while True:
    print(f"Saldo attuale: {portafoglio.calcola_saldo()}€")

    continua: str = input("Vuoi aggiungere una nuova transazione? (S/n) ").strip().lower()
    if continua == "n":
        break

    importo_in: float = float(input("Inserisci l'importo della transazione (positivo per entrate, negativo per uscite): "))
    data_in: str = input("Inserisci la data della transazione (YYYY-MM-DD): ")
    categoria_in: str = input("Inserisci la categoria della transazione: ")
    portafoglio.aggiungi_transazione(Transazione(importo_in, data_in, categoria_in))

with file.open("w", encoding="utf-8") as transazioni:
    transazioni.write(portafoglio.to_csv())
