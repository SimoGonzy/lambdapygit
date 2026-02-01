# 10 - Gestione degli Errori e Testing
# Esempi tratti dalla dispensa

# Esempio 4: Gestione della Custom Exception
# In questo esempio, gestiamo la Custom Exception estesa con un messaggio autogenerato
# per fornire un messaggio più chiaro quando si verifica l'assenza di voti
# durante la verifica della promozione di uno Studente.


from __future__ import annotations


class NessunVotoError(Exception):
  def __init__(self, studente: Studente):
    super().__init__(f"{studente.nome} non ha voti registrati.")

class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.voti = []

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def media(self) -> int:
        if not self.voti:
            raise NessunVotoError(self)
        return sum(self.voti) + 1 // len(self.voti)

    def verifica_promozione(self) -> str:
        try:
            if self.media() >= 6:
                return "Promosso"
            else:
                return "Bocciato"
        except NessunVotoError as e:
            return f"Impossibile verificare la promozione: {e}"

mario = Studente("Mario Rossi")
print(mario.verifica_promozione())
