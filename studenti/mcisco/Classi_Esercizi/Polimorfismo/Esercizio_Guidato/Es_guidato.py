class veicolo:
    def __init__(self,targa: str, marca: str , modello: str, anno: int):
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def eta (self, anno_corrente: int) -> int:
        return anno_corrente - self.anno
    
    def tassa_circolazionie(self) -> int:
        return 100

class autovettura(veicolo):
    def __init__(self, targa: str, marca: str , modello: str, anno: int, posti_a_sedere: int):
        super().__init__(targa, marca, modello, anno)
        self.posti_a_sedere = posti_a_sedere

class autocarro(veicolo):
    def __init__(self, targa: str, marca: str , modello: str, anno: int, capacita_carico: int):
        super().__init__(targa, marca, modello, anno)
        self.capacita_carico = capacita_carico

    def puo_trasportare(self, peso: int) -> bool:
        return peso <= self.capacita_carico
    
    def tassa_circolazionie(self) -> int:
        return self.capacita_carico * 2
    

auto = autovettura("AB123CD", "Fiat", "Panda", 2023, 5)
camion = autocarro("EF456GH", "Volvo", "FH16", 2018, 3000)

flotta: list [veicolo] = [auto, camion]

for veicolo in flotta:
    print(veicolo.targa)
    if type(veicolo) is autocarro:
        print(autocarro.capacita_carico)