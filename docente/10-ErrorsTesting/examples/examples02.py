# 10 - Gestione degli Errori e Testing
# Esempi tratti dalla dispensa

# Esempio 2: Uso di `raise Exception` per gestire assenza di dati
# In questo esempio, sostituiamo l'utilizzo del None con il lancio di un'eccezione
# generica quando non sono presenti voti per calcolare la media di uno Studente.


class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.voti = []

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def media(self):
        if not self.voti:
            raise Exception("Lo studente non ha voti")
        return sum(self.voti) / len(self.voti)

mario = Studente("Mario Rossi")
print(mario.media())
