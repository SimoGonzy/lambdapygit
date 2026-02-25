"""Il tipo di lavoratore più semplice che deve essere gestito è il
Dipendente:
• Trovare una rappresentazione adatta per gestirne dati
anagrafici (nome, cognome, codice fiscale) e paga oraria;
• Scrivere un metodo che, dato un numero di ore di lavoro solte,
ne calcoli lo stipendio;
• Fare in modo che la print() del Dipendente mostri dati utili e
che il confronto tra Dipendenti (<, >, …) dipenda dalla paga"""
class Dipendente:
    def __init__(self, nome, cognome, codice_fiscale, paga_oraria):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.paga_oraria = paga_oraria

    def calcola_stipendio(self, ore_lavorate):
        return self.paga_oraria * ore_lavorate

    def __str__(self):
        return f"Dipendente: {self.nome} {self.cognome}, Codice Fiscale: {self.codice_fiscale}, Paga Oraria: {self.paga_oraria}€"

    def __lt__(self, other):
        return self.paga_oraria < other.paga_oraria

    def __le__(self, other):
        return self.paga_oraria <= other.paga_oraria

    def __eq__(self, other):
        return self.paga_oraria == other.paga_oraria

    def __ne__(self, other):
        return self.paga_oraria != other.paga_oraria

    def __gt__(self, other):
        return self.paga_oraria > other.paga_oraria

    def __ge__(self, other):
        return self.paga_oraria >= other.paga_oraria
"""Il Manager e il Commerciale sono diversi tipi di Dipendenti il cui
stipendio è aumentato in base al rendimento:
• Fare in modo che lo stipendio del Manager abbia un bonus
calcolato sulla base del numero di sottoposti;
• Fare in modo che lo stipendio del Commerciale includa una
provvigione percentuale sul fatturato generato;
• Assicurarsi che print() e confronti continiuno a operare
correttamente."""
class Manager(Dipendente):
    def __init__(self, nome, cognome, codice_fiscale, paga_oraria, numero_sottoposti):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.numero_sottoposti = numero_sottoposti
        
    def calcola_stipendio(self, ore_lavorate):
        stipendio_base = super().calcola_stipendio(ore_lavorate)
        bonus = 100 * self.numero_sottoposti  # Esempio: 100€ per ogni sottoposto
        return stipendio_base + bonus
class Commerciale(Dipendente):
    def __init__(self, nome, cognome, codice_fiscale, paga_oraria, provvigione_percentuale):
        super().__init__(nome, cognome, codice_fiscale, paga_oraria)
        self.provvigione_percentuale = provvigione_percentuale

    def calcola_stipendio(self, ore_lavorate, fatturato_generato):
        stipendio_base = super().calcola_stipendio(ore_lavorate)
        provvigione = (self.provvigione_percentuale / 100) * fatturato_generato
        return stipendio_base + provvigione
    
"""Per consentire ad HR di svolgere analisi BI, ci viene chiesto di:
• Trovare una rappresentazione dell’Azienda in modo da
raggrupparvi all’interno i Dipendenti;
• Definire un metodo per calcolare il costo totale di tutti gli
stipendi (assumendo un numero standard di ore di lavoro);
• Definire un metodo per trovare il Commerciale più
performante (ovvero con più fatturato)."""
class Azienda:
    def __init__(self, nome):
        self.nome = nome
        self.dipendenti = []

    def aggiungi_dipendente(self, dipendente):
        self.dipendenti.append(dipendente)

    def calcola_costo_totale_stipendi(self, ore_lavorate_standard):
        costo_totale = 0
        for dipendente in self.dipendenti:
            if isinstance(dipendente, Commerciale):
                # Supponiamo un fatturato generato standard per il calcolo
                fatturato_generato_standard = 10000  
                costo_totale += dipendente.calcola_stipendio(ore_lavorate_standard, fatturato_generato_standard)
           
            else:
                costo_totale += dipendente.calcola_stipendio(ore_lavorate_standard)
        return costo_totale

    def trova_commerciale_piu_performante(self, fatturati):
        commerciale_performante = None
        max_fatturato = -1
        for dipendente in self.dipendenti:
            if isinstance(dipendente, Commerciale):
                fatturato = fatturati.get(dipendente.codice_fiscale)
                if fatturato > max_fatturato:
                    max_fatturato = fatturato
                    commerciale_performante = dipendente
        return commerciale_performante
    
# Esempio di utilizzo delle classi definite sopra

azienda = Azienda("Tech Solutions")

dip1 = Dipendente("Mario", "Rossi", "MRARSS80A01H501U", 20)
dip2 = Manager("Luigi", "Bianchi", "LGBNCH75B02H501U", 30, 5)
dip3 = Commerciale("Anna", "Verdi", "ANVRDI90C03H501U", 25, 10)

azienda.aggiungi_dipendente(dip1)
azienda.aggiungi_dipendente(dip2)
azienda.aggiungi_dipendente(dip3)

ore_lavorate_standard = 160  # Esempio: 160 ore al mese
costo_totale = azienda.calcola_costo_totale_stipendi(ore_lavorate_standard)
print(f"Costo totale stipendi: {costo_totale}€")

fatturati = {
      "ANVRDI90C03H501U": 50000,  # Fatturato generato da Anna Verdi
  }
commerciale_top = azienda.trova_commerciale_piu_performante(fatturati)
print(f"Commerciale più performante: {commerciale_top}")
print(dip1 > dip2)
