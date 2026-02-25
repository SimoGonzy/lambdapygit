class Persona:
    def __init__(self, nome_azienda: str, nome: str, cognome: str, codice_fiscale: str, paga_oraria: float, ore: float):
        self.nome_azienda: str = nome_azienda
        self.nome: str = nome
        self.cognome: str = cognome
        self.codice_fiscale: str = codice_fiscale.upper()
        self.paga_oraria: float = paga_oraria
        self.ore: float = ore

    def stipendio(self) -> float:
        return self.paga_oraria * self.ore
    
    def confronto_dipendenti(self, altro_dipendente: "Persona") -> str:
        if self.stipendio() > altro_dipendente.stipendio():
            return f"{self.nome} {self.cognome} ha uno stipendio maggiore di {altro_dipendente.nome} {altro_dipendente.cognome}."
        elif self.stipendio() < altro_dipendente.stipendio():
            return f"{altro_dipendente.nome} {altro_dipendente.cognome} ha uno stipendio maggiore di {self.nome} {self.cognome}."
        else:
            return f"{self.nome} {self.cognome} e {altro_dipendente.nome} {altro_dipendente.cognome} hanno lo stesso stipendio."

    def dettagli_dipendenti(self) -> str:
        return f"Azienda: {self.nome_azienda} - {self.nome} {self.cognome} - CF: {self.codice_fiscale} - Dipendente - Stipendio: {self.stipendio()} EUR"


class Manager(Persona):
    def __init__(self, nome_azienda: str, nome: str, cognome: str, codice_fiscale: str, paga_oraria: float, ore: float, sottoposti: int = 0):
        super().__init__(nome_azienda, nome, cognome, codice_fiscale, paga_oraria, ore) 
        self.sottoposti: int = sottoposti

    def dettagli_manager(self) -> str:
        return f"Azienda: {self.nome_azienda} - {self.nome} {self.cognome} - CF: {self.codice_fiscale} - Manager - Stipendio: {self.stipendio()} EUR - Sottoposti: {self.sottoposti}"
    
    def bonus_manager(self, sottoposti: int) -> float:
        return super().stipendio() * sottoposti * 0.05


class Commerciale(Persona):
    def __init__(self, nome_azienda: str, nome: str, cognome: str, codice_fiscale: str, paga_oraria: float, ore: float, fatturato: int):
        super().__init__(nome_azienda, nome, cognome, codice_fiscale, paga_oraria, ore)
        self.fatturato: int = fatturato

    def bonus_commerciale(self) -> float:
        return self.fatturato * 0.02
    
    def dettagli_commerciale(self) -> str:
        return f"Azienda: {self.nome_azienda} - {self.nome} {self.cognome} - CF: {self.codice_fiscale} - Commerciale - Stipendio: {self.stipendio()} EUR - Fatturato: {self.fatturato} EUR"
    
    def commerciale_piu_performante(self, altro_commerciale: "Commerciale") -> str:
        if self.fatturato > altro_commerciale.fatturato:
            return f"{self.nome} {self.cognome} ha un fatturato maggiore di {altro_commerciale.nome} {altro_commerciale.cognome}."
        elif self.fatturato < altro_commerciale.fatturato:
            return f"{altro_commerciale.nome} {altro_commerciale.cognome} ha un fatturato maggiore di {self.nome} {self.cognome}."
        else:
            return f"{self.nome} {self.cognome} e {altro_commerciale.nome} {altro_commerciale.cognome} hanno lo stesso fatturato."


class Azienda:
    def __init__(self, nome: str, dipendenti: list, fatturato: int):
        self.nome: str = nome
        self.dipendenti: list = dipendenti
        self.fatturato: int = fatturato

    def totale_stipendi(self) -> float:
        return sum(dipendente.stipendio() for dipendente in self.dipendenti)


Mario = Persona("Azienda S.r.l.", "Mario", "Rossi", "RSSMRA80A01H501Z", 20.0, 40.0)
Rocco = Persona("Azienda S.r.l.", "Rocco", "Bianchi", "BNCRCC85B02F205X", 22.0, 38.0)
Gianfranco = Manager("Azienda S.r.l.", "Gianfranco", "Verdi", "VRDGFR90C03D325Y", 25.0, 45.0, sottoposti=2)
Giancarlo = Commerciale("Azienda S.r.l.", "Giancarlo", "Neri", "NRRGCL95D04E415W", 30.0, 35.0, fatturato=50000)

Stuart = Persona("Impresa di Esempio S.p.A.", "Stuart", "Little", "LTSSTU90C03D325Y", 25.0, 45.0)
Riccardo = Persona("Impresa di Esempio S.p.A.", "Riccardo", "Verdi", "VRDRCD95D04E415W", 30.0, 35.0)
Gianpietro = Manager("Impresa di Esempio S.p.A.", "Gianpietro", "Neri", "NRRGNP85E05F505V", 28.0, 42.0, sottoposti=2)
Gianmarco = Commerciale("Impresa di Esempio S.p.A.", "Gianmarco", "Bianchi", "BNCRGM75F06G605U", 26.0, 40.0, fatturato=60000)

Giovanni = Persona("Bombo Solutions S.r.l.", "Giovanni", "Neri", "NRRGNN70E05F505V", 28.0, 42.0)
Adolfo = Persona("Bombo Solutions S.r.l.", "Adolfo", "Gialli", "GLLADF75F06G605U", 26.0, 40.0)
Winston = Manager("Bombo Solutions S.r.l.", "Winston", "Smith", "SMTWNS80G07H705T", 32.0, 36.0, sottoposti=2)
Gianmaria = Commerciale("Bombo Solutions S.r.l.", "Gianmaria", "Rossi", "RSSGMR85H08I805S", 24.0, 44.0, fatturato=55000)



azienda_srl = Azienda("Azienda S.r.l.", [Mario, Rocco, Gianfranco, Giancarlo], 10000)
impresa_di_esempio_spa = Azienda("Impresa di Esempio S.p.A.", [Stuart, Riccardo, Gianpietro, Gianmarco], 18000)
bombo_solutions_srl = Azienda("Bombo Solutions S.r.l.", [Giovanni, Adolfo, Winston, Gianmaria], 12000)

lista_aziende: list = [azienda_srl, impresa_di_esempio_spa, bombo_solutions_srl]


print(Mario.dettagli_dipendenti())
print(Rocco.dettagli_dipendenti())
print(Winston.dettagli_manager())
print(Gianmaria.dettagli_commerciale())
print(Mario.confronto_dipendenti(Rocco))
print(Gianfranco.bonus_manager(Gianfranco.sottoposti))
print(Gianmarco.bonus_commerciale())
print(f"Azienda: {azienda_srl.nome}, Numero Dipendenti: {azienda_srl.dipendenti.__len__()}")
print(f"Totale Stipendi Azienda S.r.l.: {azienda_srl.totale_stipendi()} EUR")
for azienda in lista_aziende:
    print(f"Azienda: {azienda.nome}, Numero Dipendenti: {len(azienda.dipendenti)}, Totale Stipendi: {azienda.totale_stipendi()} EUR")
