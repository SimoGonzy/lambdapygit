import os
class Azienda:
    def __init__(self, nome_azienda: str, fatturato: float):
        self.nome_azienda: str = nome_azienda
        self.fatturato: float = fatturato
        self.l_Dip = []

    def set_Persone_totali(self,lista_dipendenti,lista_commerciati, lista_menager):
        self.l_Dip = lista_dipendenti + lista_commerciati + lista_menager

    def stampa_dip(self):
        for dipendente in self.l_Dip:
            print(dipendente)

    def costo_stipendi_totali(self,c_dipendenti: float, c_commerciati: float, c_menager: float):
        return c_dipendenti + c_commerciati + c_menager





class Dipendente():
    def  __init__(self, codice_fiscale: str, nome_dipendente: str, cognome_dipendente: str, paga_oraria: float):
        self.codice_fiscale: str = codice_fiscale
        self.nome = nome_dipendente
        self.cognome = cognome_dipendente
        self.paga_oraria: float = paga_oraria

    def calcola_paga_oraria(self, ore: float) -> float:
        return self.paga_oraria * ore

    #stampa dei dipendenti in ordine di paga oraria
    def __str__(self) -> str:
        return f"{self.codice_fiscale} - {self.nome} {self.cognome} - {self.paga_oraria}"

    def stampa_dipendenti(lista_dipendenti, ore: float):
        lista_dipendenti.sort(key=lambda x: x.calcola_paga_oraria(ore))
        for dipendente in lista_dipendenti:
            print(dipendente)

    def __gt__(self, altro_dipendente):
        return self.paga_oraria > altro_dipendente.paga_oraria
    
    def __lt__(self, altro_dipendente):
        return self.paga_oraria < altro_dipendente.paga_oraria
    
    def __eq__(self, altro_dipendente):
        return self.paga_oraria == altro_dipendente.paga_oraria
    
    def costo_stipendi_totali(lista_dipendenti):
        costo = 0
        for dipendente in lista_dipendenti:
            costo += dipendente.calcola_paga_oraria(10)
        return costo
    
class Menager(Dipendente):
    def __init__(self, codice_fiscale: str, nome_dipendente: str, cognome_dipendente: str, paga_oraria: float, numero_sottoposti: int):
        super().__init__(codice_fiscale, nome_dipendente, cognome_dipendente, paga_oraria)
        self.numero_sottoposti: int = numero_sottoposti

    def calcola_paga_oraria(self, ore: float) -> float:
        return super().calcola_paga_oraria(ore) * self.numero_sottoposti
    
    def __str__(self) -> str:
        return f"{self.codice_fiscale} - {self.nome} {self.cognome} - {self.paga_oraria} - {self.numero_sottoposti}"
    
    def __gt__(self, altro_Menager):
        return self.calcola_paga_oraria(10) > altro_Menager.calcola_paga_oraria(10)
    
    def __lt__(self, altro_Menager):
        return self.calcola_paga_oraria(10) < altro_Menager.calcola_paga_oraria(10)
    
    def __eq__(self, altro_Menager):
        return self.calcola_paga_oraria(10) == altro_Menager.calcola_paga_oraria(10)
    
    def costio_stipendi_totali(lista_menager):
        costo = 0
        for menager in lista_menager:
            costo += menager.calcola_paga_oraria(10)
        return costo
    
class Commerciale(Dipendente):
    def __init__(self, codice_fiscale, nome_dipendente, cognome_dipendente, paga_oraria):
        super().__init__(codice_fiscale, nome_dipendente, cognome_dipendente, paga_oraria)
        self.azienda = Azienda("", 0)

    def set_azienda(self, n_a: str, f: float):
        self.azienda.nome_azienda = n_a
        self.azienda.fatturato = f
    def calcola_paga_oraria(self, ore):
        return super().calcola_paga_oraria(ore) * self.azienda.fatturato * 0.001
    
    def get_fatturato(self):
        return self.azienda.fatturato
    
    def __str__(self) -> str:
        return f"{self.codice_fiscale} - {self.nome} {self.cognome} - {self.paga_oraria} - {self.azienda.nome_azienda} - {self.azienda.fatturato}"
    
    def __gt__(self, altro_Commerciale):
        return self.calcola_paga_oraria(10) > altro_Commerciale.calcola_paga_oraria(10)
    
    def __lt__(self, altro_Commerciale):
        return self.calcola_paga_oraria(10) < altro_Commerciale.calcola_paga_oraria(10)
    
    def __eq__(self, altro_Commerciale):
        return self.calcola_paga_oraria(10) == altro_Commerciale.calcola_paga_oraria(10)

    def costo_stipendi_totali(lista_commerciati):
        costo = 0
        for commerciale in lista_commerciati:
            costo += commerciale.calcola_paga_oraria(10)
        return costo
    
    def performance(lista_commerciati):
        lista_commerciati.sort(key=lambda x: x.get_fatturato())
        print(lista_commerciati[-1])

    

    

D1 = Dipendente("CO123456A","Matteo","Bianchi",16)
D2 = Dipendente("FI123456A", "Federico", "Rossi", 10)

D3 = Dipendente("WE123456A", "Walter", "White", 20)
D4 = Dipendente("RI123456A", "Rick", "Sanchez", 9)
D5 = Dipendente("BO123456A", "Bob", "Saget", 15)

l_D2: list[Dipendente] = [D3,D4,D5]

l_D1: list[Dipendente] = [D1,D2] 

print(D1)
print(D2)

input()
os.system('clear')

print(D1.calcola_paga_oraria(10))
print(D2.calcola_paga_oraria(10))

input()
os.system('clear')

#Dipendente.stampa_dipendenti(l_D, 10)

if(D1 > D2):
    print(f"{D1.nome} {D1.cognome} è più ricco di {D2.nome} {D2.cognome}")
else:
    print(f"{D2.nome} {D2.cognome} è più ricco di {D1.nome} {D1.cognome}")

input()
os.system('clear')

M1 = Menager("EN123456A", "Enrico", "Verdi", 20, len(l_D1))
M2 = Menager("FI123456A", "Federico", "Rossi", 15, len(l_D2))

C1 = Commerciale("TO123456A", "Tom", "Hanks", 15)
C2 = Commerciale("CA123456A", "Cameron", "Diaz", 10)

C3 = Commerciale("BO123456A", "Bob", "Saget", 15)
C4 = Commerciale("MI123456A", "Micheal", "Jordan", 9)


print(M1.calcola_paga_oraria(10))
print(M2.calcola_paga_oraria(10))


if(M1 > M2):
    print(f"{M1.nome} {M1.cognome} è più ricco di {M2.nome} {M2.cognome}")
else:
    print(f"{M2.nome} {M2.cognome} è più ricco di {M1.nome} {M1.cognome}")


input()
os.system('clear')

#print(C1)
C1.set_azienda("Netflix", 1000000000)
C2.set_azienda("Netflix", 1000000000)
C3.set_azienda("Dysney", 1000)
C4.set_azienda("Caravan", 10000200)

lista_c_tot=[C1,C2,C3,C4]
#print(C1)


print(C1.calcola_paga_oraria(10))
print(C2.calcola_paga_oraria(10))

if(C1 == C2):
    print(f"{C1.nome} {C1.cognome} è più ricco di {C2.nome} {C2.cognome}")
else:
    print(f"{C2.nome} {C2.cognome} è più ricco di {C1.nome} {C1.cognome}")
     
lista_commerciali = [C1,C2]
lista_menager = [M1,M2]

Netflix = Azienda("Netflix", 1000000000)

Netflix.set_Persone_totali(l_D1, lista_commerciali, lista_menager)

Netflix.stampa_dip()

input()
os.system('clear')

print(Netflix.costo_stipendi_totali(Menager.costo_stipendi_totali(lista_menager), Commerciale.costo_stipendi_totali(lista_commerciali), Dipendente.costo_stipendi_totali(l_D1)))

input()
os.system('clear')

Commerciale.performance(lista_c_tot)





