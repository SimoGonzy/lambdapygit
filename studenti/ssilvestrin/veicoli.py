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


class Autovettura(Veicolo):
    def __init__(self, targa: str, marca: str, modello: str, anno: int, posti_a_sedere: int):
        super().__init__(targa, marca, modello, anno)
        self.posti_a_sedere: int = posti_a_sedere


class Autocarro(Veicolo):
    def __init__(self, targa: str, marca: str, modello: str, anno: int, capacità_di_carico: int):
        super().__init__(targa, marca, modello, anno)
        self.capacità_di_carico: int = capacità_di_carico
    
    def puo_trasportare(self, peso: int) -> bool:
        return peso <= self.capacità_di_carico
    
    def tassa_circolazione(self) -> float:
        return self.capacità_di_carico * 2.0
    

auto = Autovettura("AF356CG", "BMW", "M4", 2002, 4,)
camion = Autocarro("EF258GH", "Volvo", "FH7", 2016, 4000)

flotta: list[Veicolo] = [auto, camion]

for Veicolo in flotta:
    print(Veicolo.targa)
    if type(Veicolo) is Autocarro:
        print(Autocarro.capacità_di_carico)


print(auto.eta(2026))