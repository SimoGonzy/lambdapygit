class dipendenti:
    def __init__(self, nome: str, cognome: str, codicefiscale: str, paga_oraria: float):
        self.nome: str = nome
        self.cognome: str = cognome 
        self.codicef: str = codicefiscale
        self.paga_oraria: int = paga_oraria
    
    def __eq__(self, other):
        return self.paga_oraria == other.paga_oraria         
    
    def __lt__(self, other):
        return self.paga_oraria < other.paga_oraria
    
    def __str__(self):
        return f"{self.nome}, {self.cognome}, {self.codicef}, e la paga è: {self.paga_oraria}"

class Manager(dipendenti):
    def __init__(self, nome: str, cognome: str, codicefiscale: str, paga_oraria: float, num_sottoposti: int):
        super().__init__(nome, cognome, codicefiscale, paga_oraria)
        self.num_sottoposti = num_sottoposti
        self.paga_oraria = paga_oraria + (self.num_sottoposti * 3)

    def __eq__(self, other):
        return self.paga_oraria == other.paga_oraria         
    
    def __lt__(self, other):
        return self.paga_oraria < other.paga_oraria
    
    def __str__(self):
        return f"{self.nome}, {self.cognome}, {self.codicef}, e la paga è: {self.paga_oraria}"

    

class Commerciale(dipendenti):
    def __init__(self, nome: str, cognome: str, codicefiscale: str, paga_oraria: float, fatturato: float):
        super().__init__(nome, cognome, codicefiscale, paga_oraria)
        self.fatturato = fatturato
        self.paga_oraria = paga_oraria * (self.fatturato / 100)
    
    def __eq__(self, other):
        return self.paga_oraria == other.paga_oraria         
    
    def __lt__(self, other):
        return self.paga_oraria < other.paga_oraria
    
    def __str__(self):
        return f"{self.nome}, {self.cognome}, {self.codicef}, la paga è: {self.paga_oraria}"

    
class Azienda:
    def __init__(self, nome: str, num_dipendenti: list[dipendenti]):
        self.nome = nome
        self.num_dipendenti = num_dipendenti
    
    def aggiungi_dip(self, dipendente: dipendenti):
        self.num_dipendenti.append(dipendente)

    def __str__(self):
        listadipendenti = ""
        for i in range(len(self.num_dipendenti)):
            listadipendenti = listadipendenti + str(self.num_dipendenti[i]) + f'\n\n'
        return f"{self.nome}: {listadipendenti}"
    
    def costo_tot(self):
        costo_totale = 0
        for i in range(len(self.num_dipendenti)):
            costo_totale = costo_totale + self.num_dipendenti[i].paga_oraria * 160
        return costo_totale
    
        
    def commerciale(self):
        top = 0
        nome = ""
        for dipendente in self.num_dipendenti:
            if type(dipendente) == Commerciale:
                if dipendente.fatturato > top:
                    top = dipendente.fatturato
                    nome = dipendente.nome
                
        return nome



Crocco = Azienda('Crocco', [])


Toldo = dipendenti('Giorgio', 'Bau', 'bwibr', 8.0)
Tolda = dipendenti('Fulvio', 'Nanni', 'Ggefyu', 7.0)
Gigio = Manager('Mario', 'Ceolato', 'bbubow', 8.0, 7)
Mimmo = Commerciale('Manolo', 'Mammolo', 'ygeieb', 9.0, 8000)
Gustavo = Commerciale('Gustavo', 'La Mela', 'rbrfd', 9.0, 12000)

Crocco.aggiungi_dip(Toldo)
Crocco.aggiungi_dip(Gigio)
Crocco.aggiungi_dip(Mimmo)
Crocco.aggiungi_dip(Gustavo)
print(Toldo)
print(Tolda)
print(Toldo < Tolda)
print(Gigio)
print(Mimmo)
print(Tolda < Gigio)
print(Crocco)
print(Crocco.costo_tot())
print(Crocco.commerciale())