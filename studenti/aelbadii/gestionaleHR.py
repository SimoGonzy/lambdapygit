
class Dipendente:
    def __init__(self , nome:str , cognome:str , cdf:str,paga_oraria:int):
        self.nome: str =nome
        self.cognome: str=cognome
        self.cdf: str=cdf
        self.paga_oraria:int =paga_oraria 

    def stipendio(self, ore:int)-> int:
        return self.paga_oraria * ore
    
    def __str__(self):
        return f"{self.nome} {self.cognome} (Paga: {self.paga_oraria}€/h)"

    def __lt__(self, altro):
        return self.paga_oraria < altro.paga_oraria

class Manager(Dipendente):
    def __init__(self , nome:str , cognome:str , cdf:str,paga_oraria:int,sottoposti:int):
        super().__init__(nome,cognome,cdf,paga_oraria)
        self.sottoposti:int =sottoposti
    
    def stipendio(self, ore:int)-> int:
        return super().stipendio(ore)+100 * self.sottoposti//10

class Commerciale(Dipendente):
    def __init__(self , nome:str , cognome:str , cdf:str,paga_oraria:int,fatturato:int):
        super().__init__(nome,cognome,cdf,paga_oraria)
        self.fatturato:int = fatturato
    
    def stipendio(self, ore:int)-> int:
        return super().stipendio(ore)+(self.fatturato*0.1)
    

manager:Manager= Manager("Isacco","Pretto","isaccoprestto10",10,20)
commerciale:Commerciale=Commerciale("Isacco","Pretto","isaccoprestto10",10,100000)
print(manager.stipendio(20))
print(commerciale.stipendio(20))
    