# 10 - Gestione degli Errori e Testing
# Esempi tratti dalla dispensa

# Esempio 3: Definizione di una Custom Exception
# In questo esempio, definiamo una Custom Exception specifica per gestire
# l'assenza di voti quando si calcola la media di uno Studente.


class NessunVotoError(Exception):
  pass

class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.voti = []

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def media(self) -> int:
        if not self.voti:
            raise NessunVotoError(f"{self.nome} non ha voti registrati.")
        return sum(self.voti) // len(self.voti)

mario = Studente("Mario Rossi")
print(mario.media())
