class NessunVotoError(Exception):
    pass

class Studente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.voti = []

    def aggiungi_voto(self,voto):
        self.voti.append(voto)
    
    def media(self):
        if not self.voti:
            raise NessunVotoError("Lo studente non ha voti")
        return sum(self.voti) / len(self.voti)
    
    def verifica_promozione(self):
        try:
            if self.media() >= 6: #type:ignore
                return "Promosso"
            else:
                return "Bocciato"
        except NessunVotoError as e:
            return f"Impossibile verificare la promozione {e}"
        
mario = Studente("Mario Rossi")
print(mario.verifica_promozione())