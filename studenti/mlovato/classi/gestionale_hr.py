from rich import print

class Dipendente:
    def __init__(self, nome: str, cognome: str, codice_fiscale: str, paga_oraria: float) -> None:
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.paga_oraria = paga_oraria
        lista_dipendenti.append(self)
    def aggiungi_ore_lavorate(self, ore_lavorate: int):
        self.ore_lavorate = ore_lavorate
    def calcola_stipendio(self) -> float:
        return self.paga_oraria * self.ore_lavorate
    def __str__(self):
        return f"{self.nome} {self.cognome} paga oraria: {self.paga_oraria}"
    def __gt__(self, dipendente: Dipendente):
        return True if self.calcola_stipendio() > dipendente.calcola_stipendio() else False
    def __lt__(self, dipendente: Dipendente):
        return True if self.calcola_stipendio() < dipendente.calcola_stipendio() else False
    def __eq__(self, dipendente: object) -> bool:
        return type(dipendente) is Dipendente and self.calcola_stipendio() == dipendente.calcola_stipendio()

class Manager(Dipendente):
    def __init__(self, nome: str, cognome: str, codice_fiscale: str, paga_oraria: float, bonus_sottoposti: int) -> None:
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.bonus_sottoposti = bonus_sottoposti # bonus per ogni sottoposto
        self.sottoposti = []
    def calcola_stipendio(self) -> float:
        base = super().calcola_stipendio()
        bonus = self.bonus_sottoposti * len(self.sottoposti)
        return base + bonus
    
    def aggiungi_sottoposto(self, dipendente: Dipendente):
        self.sottoposti.append(dipendente)
    
    def __str__(self):
        return f"{super().__str__()}\nNumero sottoposti: {len(self.sottoposti)}\nStipendio: {self.calcola_stipendio()} "
    
class Commerciale(Dipendente):
    def __init__(self, nome: str, cognome: str, codice_fiscale: str, paga_oraria: float, provvigione_percentuale: float, fatturato: int) -> None:
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.provvigione_percentuale = provvigione_percentuale
        self.fatturato = fatturato
    
    def calcola_stipendio(self) -> float:
        base = super().calcola_stipendio()
        bonus = self.provvigione_percentuale * self.fatturato / 100
        return base + bonus
    def __str__(self):
        return f"{super().__str__()}\nProvvigione: {self.provvigione_percentuale}%\nStipendio: {self.calcola_stipendio()}"

lista_dipendenti = []

dipendente = Dipendente("Matteo", "Lovato", "LVTMTT", 100)
dipendente.aggiungi_ore_lavorate(10)
dipendente2 = Dipendente("Tizio", "Cognome", "tzcm", 25)
dipendente2.aggiungi_ore_lavorate(15)
print(f"[cyan]{dipendente}[/cyan]")
print(dipendente>dipendente2)
print(dipendente<dipendente2)
print(dipendente == dipendente)
manager = Manager("manager1", "cognome", "mngcng", 150, 30)
manager.aggiungi_ore_lavorate(4)
manager.aggiungi_sottoposto(dipendente)
manager.aggiungi_sottoposto(dipendente2)
print(manager)

commerciale = Commerciale("commerciale", "valdagno", "cmgsda", 20, 3, 10_000)
commerciale.aggiungi_ore_lavorate(20)
print(commerciale)

commerciale2 = Commerciale("prova","prova","prova", 15, 5, 15_000)
commerciale.aggiungi_ore_lavorate(15)

totale_da_sborsare = 0
for dipendente in lista_dipendenti.copy():
    dipendente.aggiungi_ore_lavorate(40)
    totale_da_sborsare += dipendente.calcola_stipendio()
    
print(f"[green]Totale da sborsare [/green][bright_black](considerando 40 ore di lavoro)[/bright_black][green]: €{totale_da_sborsare}[/green]")

miglior_commerciale: Commerciale | None = None
for dipendente in lista_dipendenti:
    if type(dipendente) is Commerciale:
        if miglior_commerciale is None or dipendente.fatturato > miglior_commerciale.fatturato:
            miglior_commerciale = dipendente

print("[cyan]Miglior commerciale:[/cyan]")
print(miglior_commerciale)