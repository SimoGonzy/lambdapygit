# %% [markdown]
# Veicoli (H1)

# %%
class Veicolo:
    def __init__(self, targa: str, marca: str, modello: str, anno: int) -> None:
        self.targa: str = targa
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno
    
    def eta(self, anno_corrente: int) -> int:
        return anno_corrente - self.anno

    def tassa_circolazione(self) -> float:
        return 100.0

class Autovettura(Veicolo):
    def __init__(self, targa: str, marca: str, modello: str, anno: int, posti_a_sedere: int) -> None:
        super().__init__(targa, marca, modello, anno)
        self.posti_a_sedere: int = posti_a_sedere

class Autocarro(Veicolo):
    def __init__(self, targa: str, marca: str, modello: str, anno: int, capacita_carico: int) -> None:
        super().__init__(targa, marca, modello, anno)
        self.capacita_carico = capacita_carico

    def puo_trasportare(self, peso: int) -> bool:
        return peso <= self.capacita_carico
    
    def tassa_circolazione(self) -> float:
        return self.capacita_carico * 2.0
# %%
auto = Autovettura("AB123CD", "Fiat", "Panda", 2015, 5)
print(auto.eta(2026))
print(auto.tassa_circolazione())
# %%
camion = Autocarro("EF456GH", "Volvo", "FH16", 2018, 3000)
flotta: list[Veicolo] = [auto, camion]
for veicolo in flotta:
    print(veicolo.targa)
    if type(veicolo) is Autocarro:
        print(veicolo.capacita_carico)
    print(f"€ {veicolo.tassa_circolazione()}")