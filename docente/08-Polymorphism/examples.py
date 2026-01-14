# 08 - Gerarchia delle Classi & Polimorfismo
# Esempi tratti dalla dispensa


from __future__ import annotations
from typing import Optional


# Esempio 1: Una singola classe per veicoli diversi
# In questo esempio definiamo una classe 'VeicoloSemplice' che rappresenta sia autovetture che autocarri.
# La classe include attributi opzionali per la capacità di carico e il numero di posti a sedere
# e metodi per calcolare l'età del veicolo e verificare se può trasportare un certo peso.

class VeicoloSemplice:
    def __init__(
        self, targa: str, marca: str, modello: str, anno: int,
        capacita_carico: Optional[int] = None, posti_a_sedere: Optional[int] = None
    ):
        self.targa: str = targa
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno
        self.capacita_carico: Optional[int] = capacita_carico
        self.posti_a_sedere: Optional[int] = posti_a_sedere

    def eta(self, anno_corrente: int) -> int:
        return anno_corrente - self.anno

    def puo_trasportare(self, peso: int) -> bool:
        if self.capacita_carico is None:
            return False
        return peso <= self.capacita_carico


# Esempio 2: Separate classi per autovetture e autocarri
# In questo esempio definiamo due classi separate, 'AutovetturaSemplice' e 'AutocarroSemplice',
# per rappresentare autovetture e autocarri rispettivamente.
# Ciascuna classe include attributi e metodi specifici.

class AutovetturaSemplice:
    def __init__(self, targa: str, marca: str, modello: str, anno: int, posti_a_sedere: int):
        self.targa: str = targa
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno
        self.posti_a_sedere: int = posti_a_sedere

    def eta(self, anno_corrente: int) -> int:
        return anno_corrente - self.anno

class AutocarroSemplice:
    def __init__(self, targa: str, marca: str, modello: str, anno: int, capacita_carico: int):
        self.targa: str = targa
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno
        self.capacita_carico: int = capacita_carico

    def eta(self, anno_corrente: int) -> int:
        return anno_corrente - self.anno

    def puo_trasportare(self, peso: int) -> bool:
        if self.capacita_carico is None:
            return False
        return peso <= self.capacita_carico


# Esempio 3: Composizione con classi veicolo di base
# In questo esempio definiamo una classe di base 'Veicolo' e utilizziamo
# la composizione per creare classi 'AutovetturaIncaps' e 'AutocarroIncaps'
# che contengono un'istanza di 'Veicolo'.

class Veicolo:
    def __init__(self, targa: str, marca: str, modello: str, anno: int):
        self.targa: str = targa
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno

    def eta(self, anno_corrente: int) -> int:
        return anno_corrente - self.anno

    def tassa_circolazione(self) -> float:
        return 100.0

class AutovetturaIncaps:
    def __init__(self, targa: str, marca: str, modello: str, anno: int, posti_a_sedere: int):
        self.veicolo: Veicolo = Veicolo(targa, marca, modello, anno)
        self.posti_a_sedere: int = posti_a_sedere

class AutocarroIncaps:
    def __init__(self, targa: str, marca: str, modello: str, anno: int, capacita_carico: int):
        self.veicolo: Veicolo = Veicolo(targa, marca, modello, anno)
        self.capacita_carico: int = capacita_carico

    def puo_trasportare(self, peso: int) -> bool:
        return peso <= self.capacita_carico

auto_incaps: AutovetturaIncaps = AutovetturaIncaps("AB123CD", "Lancia", "Ypsilon", 2005, 4)
print(auto_incaps.veicolo.eta(2025))


# Esempio 4: Ereditarietà e Overriding
# In questo esempio definiamo una classe di base 'Veicolo' e due classi derivate,
# 'Autovettura' e 'Autocarro', che estendono la funzionalità della classe base.
# La classe 'Autocarro' sovrascrive il metodo 'tassa_circolazione' per includere
# una maggiorazione basata sulla capacità di carico.

class Autovettura(Veicolo):
    def __init__(self, targa: str, marca: str, modello: str, anno: int, posti_a_sedere: int):
        super().__init__(targa, marca, modello, anno)
        self.posti_a_sedere: int = posti_a_sedere

class Autocarro(Veicolo):
    def __init__(self, targa: str, marca: str, modello: str, anno: int, capacita_carico: int):
        super().__init__(targa, marca, modello, anno)
        self.capacita_carico: int = capacita_carico

    def puo_trasportare(self, peso: int) -> bool:
        return peso <= self.capacita_carico

    def tassa_circolazione(self) -> float:
        base: float = super().tassa_circolazione()
        maggiorazione: float = self.capacita_carico * 0.1
        return base + maggiorazione

auto: Autovettura = Autovettura("AB123CD", "Lancia", "Ypsilon", 2005, 4)
camion: Autocarro = Autocarro("EF456GH", "Iveco", "Stralis", 2015, 2000)

print(auto.eta(2025))
print(auto.tassa_circolazione())
print(camion.tassa_circolazione())


# Esempio 5: Polimorfismo
# In questo esempio definiamo una classe 'Cliente' che può noleggiare veicoli di tipo 'Veicolo'.
# Nelle funzioni della classe 'Cliente' utilizziamo il polimorfismo per calcolare
# la tassa totale di tutti i veicoli noleggiati, indipendentemente dal loro tipo concreto.

class Cliente:
    def __init__(self, nome: str):
        self.nome: str = nome
        self.veicoli_noleggiati: list[Veicolo] = []

    def noleggia_veicolo(self, veicolo: Veicolo):
        self.veicoli_noleggiati.append(veicolo)

    def tassa_totale(self) -> float:
        totale: float = 0.0
        for veicolo in self.veicoli_noleggiati:
            totale += veicolo.tassa_circolazione()
        return totale

cliente: Cliente = Cliente("Mario Rossi")

cliente.noleggia_veicolo(auto)
cliente.noleggia_veicolo(camion)

print(cliente.tassa_totale())

for veicolo in cliente.veicoli_noleggiati:
    if type(veicolo) is Autocarro:
        print(f"Capacità di carico: {veicolo.capacita_carico} kg")
