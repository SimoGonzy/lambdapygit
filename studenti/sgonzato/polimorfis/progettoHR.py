class Dipendente():
    def __init__ (self, nome: str, cognome: str, cod_fisc: str, paga_oraria: float):
        self.nome = nome
        self.cognome = cognome
        self.cod_fisc = cod_fisc
        self.paga_oraria = paga_oraria

    def calcola_stipendio(self, tot_ore: int) -> float:
        return self.paga_oraria * tot_ore
    
    def __str__ (self) -> str:
        return f'Dipendente: {self.nome} {self.cognome}, Codice Fiscale: {self.cod_fisc}, Paga Oraria: {self.paga_oraria}, Stipendio Mensile: {self.calcola_stipendio(160)} euro'
    
    def __gt__ (self, other: 'Dipendente') -> bool:
        return self.calcola_stipendio(160) > other.calcola_stipendio(160)
    
    def __lt__ (self, other: 'Dipendente') -> bool:
        return self.calcola_stipendio(160) < other.calcola_stipendio(160)
    
class Manager(Dipendente):
    def __init__ (self, nome: str, cognome: str, cod_fisc:str, paga_oraria: float, n_sottoposti: int):
        super().__init__(nome, cognome, cod_fisc, paga_oraria)
        self.n_sottoposti = n_sottoposti

    def calcola_stipendio(self, tot_ore: int) -> float:
        stipendio = super().calcola_stipendio(tot_ore)
        bonus = self.n_sottoposti * 100
        return stipendio + bonus
    
class Commerciale(Dipendente):
    def __init__ (self, nome: str, cognome: str, cod_fisc:str, paga_oraria: float, provvigioni: float):
        super().__init__(nome, cognome, cod_fisc, paga_oraria)
        self.provvigioni = provvigioni

    def calcola_stipendio(self, tot_ore: int) -> float:
        return super().calcola_stipendio(tot_ore) + ((self.provvigioni / 100) * 5)
        
class Azienda:
    def __init__ (self, nome: str, indirizzo: str):
        self.nome = nome
        self.indirizzo = indirizzo
        self.listaDipendenti: list[Dipendente] = []
        
    def costo_totale(self, tot_ore: int) -> float:
        costo = 0
        for dipendente in self.listaDipendenti:
            costo += dipendente.calcola_stipendio(tot_ore)
        return costo
    
    def comm_perfomance(self):
        com = ""
        for dipendente in self.listaDipendenti:
            if type(dipendente) is Commerciale:
                if com == "":
                    com = dipendente
                else:
                    if dipendente > com:
                        com = dipendente
        if com != "":
            return com
        else:
            return "Nessun commerciale presente" 


# Creazione dell'azienda
azienda = Azienda("TechSolutions SRL", "Via Roma 10, Milano")

# Creazione dipendenti
d1 = Dipendente("Mario", "Rossi", "RSSMRA80A01F205X", 15)
d2 = Dipendente("Luigi", "Bianchi", "BNCLGU85B12F205Y", 18)

m1 = Manager("Anna", "Verdi", "VRDANN75C22F205Z", 25, 5)     # 5 sottoposti
m2 = Manager("Paolo", "Neri", "NRIPLL70D10F205K", 30, 3)    # 3 sottoposti

c1 = Commerciale("Sara", "Blu", "BLUSRA90E11F205M", 20, 10)   # 10% provvigioni
c2 = Commerciale("Luca", "Gialli", "GLLLCU88F20F205N", 22, 25) # 25% provvigioni
c3 = Commerciale("Marta", "Viola", "VIOMRT92A15F205P", 18, 40) # 40% provvigioni

# Inserimento dipendenti nell'azienda
azienda.listaDipendenti.append(d1)
azienda.listaDipendenti.append(d2)
azienda.listaDipendenti.append(m1)
azienda.listaDipendenti.append(m2)
azienda.listaDipendenti.append(c1)
azienda.listaDipendenti.append(c2)
azienda.listaDipendenti.append(c3)

# ================= TEST =================

print("ELENCO DIPENDENTI:")
for d in azienda.listaDipendenti:
    print(d)

print("\nCALCOLO STIPENDI (160 ore):")
for d in azienda.listaDipendenti:
    print(d.nome, d.cognome, "->", d.calcola_stipendio(160), "euro")

print("\nCONFRONTO TRA DUE DIPENDENTI:")
print("Mario Rossi > Luigi Bianchi ?", d1 > d2)
print("Luca Gialli > Sara Blu ?", c2 > c1)

print("\nCOSTO TOTALE AZIENDA (160 ore):")
print(azienda.costo_totale(160), "euro")

print("\nCOMMERCIALE CON MIGLIOR PERFORMANCE:")
print(azienda.comm_perfomance())