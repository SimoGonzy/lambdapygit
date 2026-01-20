class Tamagotchi:
    def __init__(self, nome: str):
        self.nome = nome
        self.fame = 50
        self.felicita = 50
        self.stanchezza = 50

    
    #funziona
    def nutrire(self):
        if self.fame <= 50:
            self.fame = 0
        else:
            self.fame -= 50

    #funziona ma con 2 if
    def giocare(self):
        if self.felicita >= 50:
            self.felicita = 100
        else:
            self.felicita += 50
            
        if self.stanchezza >= 70:
            self.stanchezza = 100
        else:
            self.stanchezza += 30
        
    #funziona ma con 3 if
    def dormire(self):
        if self.fame <= 50:
            self.fame = 0
        else:
            self.fame -= 50
            
        if self.stanchezza <= 50:
            self.stanchezza = 0
        else:
            self.stanchezza -= 50
            
        if self.felicita >= 75:
            self.felicita = 100
        else:
            self.felicita += 25

    def stato(self):
        print(f"Stato di {self.nome} - Fame: {self.fame}, Felicita: {self.felicita}, Stanchezza: {self.stanchezza}")
        
class ListaTamagotchi:
    def __init__(self):
        self.lista: list[Tamagotchi] = []
        
    def aggiungi_tamagotchi(self, tamagotchi: Tamagotchi):
        self.lista.append(tamagotchi)
        
    def rimuovi_tamagotchi(self, tamagotchi: Tamagotchi):
        self.lista.remove(tamagotchi)

'''
I cuccioli si stancano più velocemente quando giocano, ma si
riposano più velocemente quando dormono;
• Gli adulti si stancano meno velocemente, ma richiedono più
cibo per essere nutriti.
Lavorare con il filesystem - Python: da Zero a OOP - Riccardo Sacchetto, B.Sc.
'''
     
class Adulti(Tamagotchi):
    def __init__(self, nome: str):
        super().__init__(nome)
        
    def nutrire(self):
        if self.fame <= 70:
            self.fame = 0
        else:
            self.fame -= 70
        
    def giocare(self):
        if self.felicita >= 50:
            self.felicita = 100
        else:
            self.felicita += 50
            
        if self.stanchezza >= 50:
            self.stanchezza = 100
        else:
            self.stanchezza += 15

class Cuccioli(Tamagotchi):
    def __init__(self, nome: str):
        super().__init__(nome)
        
    def giocare(self):
        if self.felicita >= 50:
            self.felicita = 100
        else:
            self.felicita += 50
            
        if self.stanchezza >= 80:
            self.stanchezza = 100
        else:
            self.stanchezza += 40
            
    def dormire(self):
        if self.fame <= 50:
            self.fame = 0
        else:
            self.fame -= 50
            
        if self.stanchezza <= 40:
            self.stanchezza = 0
        else:
            self.stanchezza -= 40
            
        if self.felicita >= 75:
            self.felicita = 100
        else:
            self.felicita += 25