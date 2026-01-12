class Dipendente:
    def __init__(self, nome, cognome, cf, paga_oraria):
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.paga_oraria = paga_oraria

    def calcola_stipendio(self, ore_lavoro):
        return self.paga_oraria * ore_lavoro

    def __str__(self):
        return (f"Dipendente: {self.nome} {self.cognome}\n"
                f"CF: {self.cf}\n"
                f"Paga Oraria: {self.paga_oraria:.2f}€")

    def __lt__(self, other):
        if isinstance(other, Dipendente):
            return self.paga_oraria < other.paga_oraria
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Dipendente):
            return self.paga_oraria > other.paga_oraria
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Dipendente):
            return self.paga_oraria == other.paga_oraria
        return NotImplemented

class Manager(Dipendente):
    def __init__(self, nome, cognome, cf, paga_oraria, bonus_per_sottoposto, dipendenti=None):
        super().__init__(nome, cognome, cf, paga_oraria)
        self.bonus_per_sottoposto = bonus_per_sottoposto
        self.dipendenti = dipendenti if dipendenti is not None else []

    def aggiungi_dipendente(self, dipendente):
        self.dipendenti.append(dipendente)

    def calcola_stipendio(self, ore_lavoro):
        stipendio_base = super().calcola_stipendio(ore_lavoro)
        bonus = self.bonus_per_sottoposto * len(self.dipendenti)
        return stipendio_base + bonus

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Ruolo: Manager\n"
                f"Bonus per sottoposto: {self.bonus_per_sottoposto}€\n"
                f"Sottoposti: {len(self.dipendenti)}")


class Commerciale(Dipendente):
    def __init__(self, nome, cognome, cf, paga_oraria, fatturato, commissione_pct):
        super().__init__(nome, cognome, cf, paga_oraria)
        self.fatturato = fatturato
        self.commissione_pct = commissione_pct

    def calcola_stipendio(self, ore_lavoro):
        stipendio_base = super().calcola_stipendio(ore_lavoro)
        provvigione = self.fatturato * (self.commissione_pct / 100)
        return stipendio_base + provvigione

    def __str__(self):
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Ruolo: Commerciale\n"
                f"Fatturato: {self.fatturato}€\n"
                f"Commissione: {self.commissione_pct}%")


class Azienda:
    def __init__(self, nome, dipendenti=None):
        self.nome = nome
        self.dipendenti = dipendenti if dipendenti is not None else []

    def aggiungi_dipendente(self, dipendente):
        self.dipendenti.append(dipendente)

    def calcola_costo_totale_stipendi(self, ore_lavoro_standard=160):
        totale = 0
        for dipendente in self.dipendenti:
            totale += dipendente.calcola_stipendio(ore_lavoro_standard)
        return totale

    def trova_commerciale_migliore(self):
        migliore = None
        miglior_fatturato = -1
        
        for dipendente in self.dipendenti:
            if isinstance(dipendente, Commerciale):
                if dipendente.fatturato > miglior_fatturato:
                    miglior_fatturato = dipendente.fatturato
                    migliore = dipendente
        
        return migliore

    def __str__(self):
        return f"Azienda: {self.nome}, Dipendenti: {len(self.dipendenti)}"


# Test Rapido
if __name__ == "__main__":
    d1 = Dipendente("Mario", "Rossi", "MNRRSS...", 15.0)
    d2 = Dipendente("Luigi", "Verdi", "LGIVRD...", 20.0)

    print(d1)
    print(f"Stipendio per 160 ore: {d1.calcola_stipendio(160)}€")
    
    if d2 > d1:
        print(f"{d2.nome} guadagna più di {d1.nome}")


    # Test Level 2
    m1 = Manager("Paolo", "Bianchi", "PLBNCH...", 25.0, 50.0) # 50€ bonus per subordinate
    m1.aggiungi_dipendente(d1)
    m1.aggiungi_dipendente(d2)
    
    c1 = Commerciale("Anna", "Neri", "NNNR...", 18.0, 100000, 2.0) # 2% commission on 100k
    
    print("\n--- TEST LEVEL 2 ---")
    print(m1)
    print(f"Stipendio Manager (160h): {m1.calcola_stipendio(160)}€")
    
    print(c1)
    print(f"Stipendio Commerciale (160h): {c1.calcola_stipendio(160)}€")

    # Test Level 3
    print("\n--- TEST LEVEL 3 ---")
    azienda = Azienda("Tech Corp")
    azienda.aggiungi_dipendente(d1)
    azienda.aggiungi_dipendente(d2)
    azienda.aggiungi_dipendente(m1)
    azienda.aggiungi_dipendente(c1)
    
    c2 = Commerciale("Luca", "Gialli", "LCGLL...", 18.0, 150000, 2.0)
    azienda.aggiungi_dipendente(c2)

    print(azienda)
    print(f"Costo totale stipendi: {azienda.calcola_costo_totale_stipendi()}€")
    
    top_comm = azienda.trova_commerciale_migliore()
    if top_comm:
        print(f"Miglior Commerciale: {top_comm.nome} (Fatturato: {top_comm.fatturato}€)")