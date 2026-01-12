from typing import Optional


class dipendente:
    def __init__(self, nome: str, cognome: str, codice_fiscale: str, paga_oraria: int):
        self.nome: str = nome
        self.cognome: str = cognome
        self.codice_fiscale = codice_fiscale
        self.paga_oraria = paga_oraria

    def calcola_stipendio(self, N_ore: int) -> float:
        return self.paga_oraria * N_ore

    def __str__(self) -> str:
        return f"Nome:{self.nome} \nCognome:{self.cognome} \ncodice_fiscale:{self.codice_fiscale}"

    def __gt__(self, other) -> bool:
        return self.calcola_stipendio(160) > other.calcola_stipendio(160)


class Manager(dipendente):
    def __init__(
        self,
        nome: str,
        cognome: str,
        codice_fiscale: str,
        paga_oraria: int,
        N_sottoposti: int,
    ):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.N_sottoposti: int = N_sottoposti

    def calcola_stipendio(self, N_ore: int) -> float:
        return super().calcola_stipendio(N_ore) + (self.N_sottoposti * 100)


class Commerciale(dipendente):
    def __init__(
        self,
        nome: str,
        cognome: str,
        codice_fiscale: str,
        paga_oraria: int,
        provvigioni: float,
    ):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.provvigioni = provvigioni

    def calcola_stipendio(self, N_ore: int) -> float:
        return super().calcola_stipendio(N_ore) + ((self.provvigioni / 100) * 5)


class Azienda:
    def __init__(self, nome: str, indirozzo: str):
        self.nome = nome
        self.indirizzo = indirozzo
        self.dipendenti: list[dipendente] = []

    def costo_totale(self, N_ore: int) -> float:
        costo: float = 0
        for dipendente in self.dipendenti:
            costo += dipendente.calcola_stipendio(N_ore)
        return costo

    def Commerciale_performante(self) -> Optional[Commerciale]:
        CommercialeP = ""
        for dipendente in self.dipendenti:
            if type(dipendente) is Commerciale:
                if CommercialeP == "":
                    CommercialeP = dipendente
                else:
                    if dipendente > CommercialeP:
                        CommercialeP = dipendente
        if CommercialeP != "":
            return CommercialeP
        else:
            return None


# Dipendenti base
d1 = dipendente("Mario", "Rossi", "RSSMRA80A01H501U", 15)
d2 = dipendente("Luigi", "Bianchi", "BNCLGU85B22F205X", 18)

# Manager
m1 = Manager("Anna", "Verdi", "VRDNNA75C10H501Z", 25, 5)
m2 = Manager("Paolo", "Neri", "NRIPLA70D15F205Y", 30, 10)

# Commerciali
c1 = Commerciale("Sara", "Gialli", "GLLSRA90E40H501W", 12, 2000)
c2 = Commerciale("Marco", "Blu", "BLUMRC88F12F205K", 14, 3500)

# Azienda
azienda = Azienda("Tech Srl", "Via Roma 10")

# Aggiunta dipendenti all'azienda
azienda.dipendenti = [d1, d2, m1, m2, c1, c2]

# Esempi di utilizzo
print("Costo totale azienda (160 ore):", azienda.costo_totale(160))
print("Commerciale più performante:", azienda.Commerciale_performante())
