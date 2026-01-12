class Dipendente:
    def __init__(self, nome, cognome, codice_fiscale, paga):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.paga = paga

    def stipendio(self, ore):
        return self.paga * ore

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.codice_fiscale})"

    def __gt__(self, other) -> bool:
        return self.paga > other.paga

    def __lt__(self, other) -> bool:
        return self.paga < other.paga

    def __eq__(self, other) -> bool:
        return self.paga == other.paga


class Manager(Dipendente):
    def __init__(self, nome, cognome, codice_fiscale, paga, sottoposti):
        super().__init__(nome, cognome, codice_fiscale, paga)
        self.sottoposti = sottoposti

    def stipendio(self, ore):
        return super().stipendio(ore) + self.sottoposti * self.paga * 0.02

    def __str__(self):
        return f"{super().__str__()} ha {self.sottoposti} sottoposti"

    def __gt__(self, other) -> bool:
        return self.stipendio(1) > other.stipendio(1)

    def __lt__(self, other) -> bool:
        return self.stipendio(1) < other.stipendio(1)

    def __eq__(self, other) -> bool:
        return self.stipendio(1) == other.stipendio(1)


class Commerciale(Dipendente):
    def __init__(self, nome, cognome, codice_fiscale, paga, vendite):
        super().__init__(nome, cognome, codice_fiscale, paga)
        self.vendite = vendite

    def stipendio(self, ore):
        return super().stipendio(ore) + self.vendite * 0.05

    def __str__(self):
        return f"{super().__str__()} ha fatturato {self.vendite}"

    def __gt__(self, other) -> bool:
        return self.stipendio(1) > other.stipendio(1)

    def __lt__(self, other) -> bool:
        return self.stipendio(1) < other.stipendio(1)

    def __eq__(self, other) -> bool:
        return self.stipendio(1) == other.stipendio(1)


azienda: list[Dipendente] = []


def aggiungi_dipendente(dipendente: Dipendente):
    azienda.append(dipendente)


def rimuovi_dipendente(dipendente: Dipendente):
    azienda.remove(dipendente)


def stipendi_totali():
    return sum(dipendente.stipendio(1) for dipendente in azienda)


def best_commerciale():
    commerciali: list[Commerciale] = list(
        filter(lambda x: type(x) is Commerciale, azienda)
    )  # pyright:ignore
    return max(commerciali, key=lambda x: x.vendite)
