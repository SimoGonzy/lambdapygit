class Dipendente:
    def __init__(self, nome: str, cognome: str, codice_dipendente: int, paga_base: int):
        self.nome = nome
        self.cognome = cognome
        self.codice_dipendente = codice_dipendente
        self.paga_base = paga_base

    def stipendio_dipendente(self, ore_lavoro: int) -> int:
        return ore_lavoro * self.paga_base


class Manager(Dipendente):
    def __init__(
        self,
        nome: str,
        cognome: str,
        codice_dipendente: int,
        paga_base: int,
        sottoposti: int,
    ):
        super().__init__(nome, cognome, codice_dipendente, paga_base)
        self.sottoposti: int = sottoposti

    def stipendio_manager(self, bonus: int) -> int:
        return (bonus * self.sottoposti) + self.paga_base


class Commerciale(Dipendente):
    def __init__(
        self,
        nome: str,
        cognome: str,
        codice_dipendente: int,
        paga_base: int,
        percentuale: int,
    ):
        super().__init__(nome, cognome, codice_dipendente, paga_base)
        self.percentuale: int = percentuale

    def stipendio_commerciale(self, fattura: int) -> float:
        return ((self.percentuale / 100) * fattura) + self.paga_base

class Azienda:
    def __init__(self, nome: str):
        self.nome = nome
        self.dipendenti: list[Dipendente] = []

    def aggiungi_dipendente(self, dipendente: Dipendente):
        self.dipendenti.append(dipendente)

    def commerciale_piu_performante(self, fatturati: dict[Commerciale, int]) -> Commerciale:
        return max(fatturati)


dipendente1 = Dipendente("Mario", "Rossi", 1, 12)
dipendente2 = Dipendente("Valentino", "Menegatti", 2, 10)
dipendente3 = Dipendente("Gaia", "Verdi", 3, 11)

manager1 = Manager("Alessandra", "Gatti", 101, 1500, 20)
manager2 = Manager("Giovanni", "Vicentino", 102, 1800, 13)
manager3 = Manager("Francesco", "Bonnucci", 103, 1100, 7)

commerciale1 = Commerciale("Samuele", "Santo", 201, 1600, 8)
commerciale2 = Commerciale("Emanuela", "Carraro", 202, 1700, 10)
commerciale3 = Commerciale("Matteo", "Salvatore", 203, 1300, 4)


print(dipendente1.stipendio_dipendente(120))
print(dipendente2.stipendio_dipendente(100))
print(dipendente3.stipendio_dipendente(110))

print(manager1.stipendio_manager(10))
print(manager2.stipendio_manager(20))
print(manager3.stipendio_manager(15))

print(commerciale1.stipendio_commerciale(18268))
print(commerciale2.stipendio_commerciale(39883))
print(commerciale3.stipendio_commerciale(9265))

azienda = Azienda("Tech SPA")

azienda.aggiungi_dipendente(dipendente1)
azienda.aggiungi_dipendente(dipendente2)
azienda.aggiungi_dipendente(dipendente3)
azienda.aggiungi_dipendente(manager1)
azienda.aggiungi_dipendente(manager2)
azienda.aggiungi_dipendente(manager3)
azienda.aggiungi_dipendente(commerciale1)
azienda.aggiungi_dipendente(commerciale2)
azienda.aggiungi_dipendente(commerciale3)

print("Commerciale piu fatturato": commerciale2)
