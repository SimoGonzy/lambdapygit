class Veicolo:
    def __init__(self, targa: str, marca: str, modello: str, anno: int):
        self.targa: str = targa
        self.marca: str = marca
        self.modello: str = modello
        self.anno: int = anno


def età(self, anno_corrente: int) -> int:
    return anno_corrente - self.anno


def tassa_circolazione(self) -> float:
    return 100.0


class Autovettura(Veicolo):
    def __init__(
        self, targa: str, marca: str, modello: str, anno: int, posti_a_sedere: int
    ):
        super().__init__(targa, marca, modello, anno)
        self.posti_a_sedere: int = posti_a_sedere


class Autocarro(Veicolo):
    def __init__(
        self, targa: str, marca: str, modello: str, anno: int, capacità_carico: int
    ):
        super().__init__(targa, marca, modello, anno)
        self.capacità_carico: int = capacità_carico

    def può_trasportare(self, peso: int) -> bool:
        return peso <= self.capacità_carico

    def tassa_circolazione(self) -> float:
        return self.capacità_carico * 2.0


auto = Autovettura("BA123CD", "Fiat", "Panda", 2015, 5)
camion = Autocarro("CA345BE", "Volvo", "BH15", 2018, 2000)

flotta: list[Veicolo] = [auto, camion]
for veicolo in flotta:
    print(veicolo.targa)
    if type(veicolo) is Autovettura:
        print(veicolo.marca)
