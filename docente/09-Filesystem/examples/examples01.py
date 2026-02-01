# 09 - Lavorare con il filesystem
# Esempi tratti dalla dispensa

# Esempio 1: Lettura e scrittura con approccio imperativo
# In questo esempio, gestiamo un portafoglio di transazioni finanziarie
# leggendo e scrivendo direttamente su un file CSV senza utilizzare
# metodi di (de)serializzazione all'interno delle classi.


from pathlib import Path


class Transazione:
    def __init__(self, importo: float, data: str, categoria: str):
        self.importo: float = importo
        self.data: str = data
        self.categoria: str = categoria

class Portafoglio:
    def __init__(self):
        self.transazioni: list[Transazione] = []

    def aggiungi_transazione(self, transazione: Transazione):
        self.transazioni.append(transazione)

    def calcola_saldo(self) -> float:
        return sum([ t.importo for t in self.transazioni ])

portafoglio: Portafoglio = Portafoglio()
file: Path = Path("./transazioni.csv")
with file.open("r", encoding="utf-8") as transazioni:
    next(transazioni)  # Salta l'header
    for riga in transazioni:
        campi: list[str] = riga.strip().split(",")

        importo: float = float(campi[0])
        data: str = campi[1]
        categoria: str = campi[2]
        portafoglio.aggiungi_transazione(Transazione(importo, data, categoria))

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
    transazioni.write("importo,data,categoria\n")  # Scriviamo l'header
    for t in portafoglio.transazioni:
        transazioni.write(f"{t.importo},{t.data},{t.categoria}\n")
