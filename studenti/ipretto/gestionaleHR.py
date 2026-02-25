class Dipendente:    
    def __init__ (self, nome: str, cognome: str, codice_fiscale: str, paga_oraria: int):
        self.nome: str = nome
        self.cognome: str = cognome
        self.codice_fiscale = codice_fiscale
        self.paga_oraria: int = paga_oraria

    def stipendio(self, ore: int) -> int:
        return self.paga_oraria*ore
    
    def __str__(self):
        return f"Nome: {self.nome}\nCognome: {self.cognome}\nCodice fiscale: {self.codice_fiscale}\nPaga oraria: {self.paga_oraria}"
    
    def __gt__(self, altro_dipendente):
        """Gestisce il simbolo '>' (Maggiore di)"""
        return self.paga_oraria > altro_dipendente.paga_oraria

    def __lt__(self, altro_dipendente):
        """Gestisce il simbolo '<' (Minore di)"""
        return self.paga_oraria < altro_dipendente.paga_oraria
    

class Manager(Dipendente):
    def __init__ (self, nome: str, cognome: str, codice_fiscale: str, paga_oraria: int, sottoposti: int):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.sottoposti = sottoposti

    def stipendio(self, ore: int) -> int:
        return super().stipendio(ore)+100*self.sottoposti//10
    

class Commerciale(Dipendente):
    def __init__ (self, nome: str, cognome: str, codice_fiscale: str, paga_oraria: int, fatturato: int):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.fatturato = fatturato

    def stipendio(self, ore: int) -> int:
        return super().stipendio(ore)+(self.fatturato*0.05)
    

class Azienda:
    def __init__(self, nome):
        self.nome = nome
        self.lista_dipendenti = []

    def aggiungi_dipendente(self, dipendente):
        self.lista_dipendenti.append(dipendente)
    
    def calcola_costi_totali(self, ore_standard=160):
        totale = 0
        for d in self.lista_dipendenti:
            totale += d.calcola_stipendio(ore_standard)
        return totale
    
    def commerciale_migliore(self):
        migliore = None
        max_fatturato = -1
        
        for d in self.lista_dipendenti:
            if isinstance(d, Commerciale):
                if d.fatturato > max_fatturato:
                    max_fatturato = d.fatturato
                    migliore = d
        return migliore




prova: Dipendente = Dipendente("Ciao", "Ciaooo", "PROVA", 21)

print(prova.print())

        

    


    