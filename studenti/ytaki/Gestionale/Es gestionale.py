class Dipendente:
    def __init__(self, nome, cognome, codice_fiscale, paga_oraria):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.paga_oraria = paga_oraria

    def stipendio(self, numero_ore):
        return numero_ore * self.paga_oraria

    def __str__(self):
        return f"Nome: {self.nome} | Cognome: {self.cognome} | CF: {self.codice_fiscale} | Paga Oraria: {self.paga_oraria}"

    def __gt__(self, dipendente2):
        return self.paga_oraria > dipendente2.paga_oraria


class Manager(Dipendente):
    def __init__(self, nome, cognome, codice_fiscale, paga_oraria, numero_sottoposti):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.numero_sottoposti = numero_sottoposti

    def stipendio(self, numero_ore):
        bonus = self.numero_sottoposti * 40
        return (numero_ore * self.paga_oraria) + bonus


class Commerciale(Dipendente):
    def __init__(self, nome, cognome, codice_fiscale, paga_oraria):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)

    def stipendio(self, numero_ore):
        p = 8
        stipendio = numero_ore * self.paga_oraria
        return stipendio + (stipendio * (p / 100))


class Azienda:
    def __init__(self, dipendenti):
        self.dipendenti = dipendenti

    def totale_stipendi(self):
        somma = 0
        for dipendente in self.dipendenti:
            somma += dipendente.stipendio(40)
        return somma

    def miglior_commerciale(self):
        max = 0
        nome = ""
        for dipendente in self.dipendenti:
            if type(dipendente) == Commerciale:
                if dipendente.stipendio(40) > max:
                    max += dipendente.stipendio(40)
                    nome = dipendente.nome
        return nome

    def __str__(self):
        boh = "\n-------------------\n"
        for dipendente in self.dipendenti:
            if type(dipendente) == Commerciale:
                boh = boh + "Classe: Commerciale | " + str(dipendente) + "\n"
            elif type(dipendente) == Dipendente:
                boh = boh + "Classe: Dipendente | " + str(dipendente) + "\n"
            elif type(dipendente) == Manager:
                boh = boh + "Classe: Manager | " + str(dipendente) + "\n"
        boh += "-------------------\n"
        return boh


manager = Manager("Giovanni", "Rossi", "abcdefg123", 20, 30)
commerciale = Commerciale("Mario", "Rossi", "abcdefg123", 40)
dipendente1 = Dipendente("Luigi", "Verdi", "abcdefg123", 20)
dipendente2 = Dipendente("Luca", "Pelato", "abcdefg123", 20)
commerciale1 = Commerciale("Mario", "Rossi", "abcdefg123", 40)
commerciale2 = Commerciale("Luigi", "Verdi", "abcdefg123", 100)
commerciale3 = Commerciale("Luca", "Pelato", "abcdefg123", 20)

print(f"\n{dipendente1}")
print(f"Stipendio: {dipendente1.stipendio(20)}")
print(dipendente1 > dipendente2)
print(commerciale > manager)

dipendenti = [
    manager,
    commerciale,
    dipendente1,
    dipendente2,
    commerciale1,
    commerciale2,
    commerciale3,
]
azienda1 = Azienda(dipendenti)

print("\nAzienda1:", azienda1)
print("Totale stipendi dei dipendenti:", f"{azienda1.totale_stipendi():.0f}")


print("Miglior commerciale:", azienda1.miglior_commerciale())
