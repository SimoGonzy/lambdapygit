from functools import total_ordering

@total_ordering
class Dipendente:
    def __init__(self, nome: str, cognome: str, codice_fiscale: str, paga_oraria: float):
        self.nome: str = nome
        self.cognome: str = cognome
        self.codice_fiscale: str = codice_fiscale
        self.paga_oraria: float = paga_oraria
    
    def __eq__(self, other):
        return self.paga_oraria == other.paga_oraria
    
    def __lt__(self, other):
        return self.paga_oraria < other.paga_oraria
    
    def __str__(self) -> str:
        return f"{self.nome}, {self.cognome}, {self.codice_fiscale}, {self.paga_oraria}"

class Manager(Dipendente):
    def __init__(self, nome, cognome, codice_fiscale, paga_oraria, sottoposti: int):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.sottoposti: int = sottoposti
        self.paga_oraria = paga_oraria + (self.sottoposti * 5)   #il numero 5 è il bonus
    
    def __eq__(self, other):
        return self.paga_oraria == other.paga_oraria
    
    def __lt__(self, other):
        return self.paga_oraria < other.paga_oraria

    def __str__(self):
        return f"{self.nome}, {self.cognome}, {self.codice_fiscale}, {self.paga_oraria}, {self.sottoposti}"

class Commerciale(Dipendente):
    def __init__(self, nome, cognome, codice_fiscale, paga_oraria, provvigione: float, fatturato: float):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.provvigione: float = provvigione
        self.fatturato: float = fatturato
        self.paga_oraria = paga_oraria + ((self.provvigione * self.fatturato) / 100)

    def __eq__(self, other):
        return self.paga_oraria == other.paga_oraria
    
    def __lt__(self, other):
        return self.paga_oraria < other.paga_oraria

    def __str__(self):
        return f"{self.nome}, {self.cognome}, {self.codice_fiscale}, {self.paga_oraria}, {self.provvigione}, {self.fatturato}"
    
class Azienda:
    def __init__(self, nome: str, lista_dipendenti: list[Dipendente]):
        self.nome: str = nome
        self.lista_dipendenti = lista_dipendenti
    
    def aggiungi_dipendente(self, dipendente: Dipendente):
        self.lista_dipendenti.append(dipendente)

    def __str__(self):
        listadeidipendenti = ""
        for i in range(len(self.lista_dipendenti)):
            listadeidipendenti = listadeidipendenti + str(self.lista_dipendenti[i]) + f"\n\n"
        return f"{self.nome}: \n {listadeidipendenti}"
    
    def costo_totale(self):
        costo = 0
        for i in range(len(self.lista_dipendenti)):
            costo = costo + self.lista_dipendenti[i].paga_oraria
        return costo

    def magg_commerciale(self):
        top = 0
        toppone = ""
        for dipendete in self.lista_dipendenti:
            if type(dipendete) is Commerciale:
                if dipendete.fatturato > top:
                    top = dipendete.fatturato
                    toppone = dipendete
        return toppone

mario = Dipendente("mario", "rossi", "AS877asfasf", 54.0)
giorgio = Dipendente("giorgio", "verdi", "UHASF78", 190.0)
brodo = Manager("brodo", "noodle", "NJ70", 30000000000000000000000, 500)
Frodo = Commerciale("Frodo", "Beggins", "IBJA123", 30, 5, 1000)
argiorgio = Commerciale("Agrio", "Buono", "ASIJBG", 500, 10, 900000)
Magiungio = Commerciale("Mag", "Giungio", "ASFAFS", 24, 2, 900)

Amer = Azienda("Amer", [])
Amer.aggiungi_dipendente(mario)
Amer.aggiungi_dipendente(giorgio)
Amer.aggiungi_dipendente(brodo)
Amer.aggiungi_dipendente(argiorgio)
Amer.aggiungi_dipendente(Magiungio)

print(Amer)
print(Amer.costo_totale())
print(Amer.magg_commerciale())