# 10 - Gestione degli Errori e Testing
# Esempi tratti dalla dispensa

# Esempio 1: Uso del None per gestire assenza di dati
# In questo esempio, gestiamo il calcolo della media di uno Studente
# anche quando non sono presenti voti, utilizzando None per indicare
# l'assenza di dati.


class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.voti = []

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def media(self):
        if not self.voti:
            return None  # Nessun voto disponibile
        return sum(self.voti) / len(self.voti)

    def verifica_promozione(self):
        if self.media() >= 6:   # type: ignore
            return "Promosso"
        else:
            return "Bocciato"

mario = Studente("Mario Rossi")
print(mario.verifica_promozione())
