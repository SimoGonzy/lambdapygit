class Veicolo:
    def __init__(self, targa: str, marca: str, modello: str, anno: int):
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    def eta(self, anno_corrente: int) -> int:
        return anno_corrente - self.anno
    
    def tassa_circolazione(self) -> float:
        return 100.0
        
class Autovettura(Veicolo):
    def __init__(self, targa: str, marca: str, modello: str, anno: int, massa: int, numero_posti: int):
        super().__init__(targa, marca, modello, anno, massa)
        self.numero_posti = numero_posti
        
class Autocarro(Veicolo):
    def __init__(self, targa: str, marca: str, modello: str, anno: int, massa: int, massa_trasportabile: int):
        super().__init__(targa, marca, modello, anno, massa)
        self.massa_trasportabile = massa_trasportabile
        
    def puoi_trasportare(self, peso: int) -> bool:
        return peso <= self.massa_trasportabile
    
    def tassa_circolazione(self) -> float:
        return self.massa_trasportabile * 2.0
    
    
auto = Autovettura("AB123CD", "Fiat", "Panda", 2015, 1000)
camion = Autocarro("EF456GH", "Iveco", "Stralis", 2018, 8000, 20000)

flotta: list[Veicolo] = [auto, camion]
for veicolo in flotta:
    print(veicolo.targa)
    if type(veicolo) is Autocarro:
        print(veicolo.massa_trasportabile)