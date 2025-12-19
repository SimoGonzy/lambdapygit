class Misure:
    def __init__(self, metri: int):
        self.metri = metri
        
    def in_chilometri(self):
        return self.metri / 1000
    
    def in_metri(self):
        return self.metri
    
    
def area_stanza(base: Misure, altezza: Misure) -> int:
    return base.in_metri() * altezza.in_metri()

def calcola_tempo_viaggio(distanza: Misure) -> float:
    distanza_km = distanza.in_chilometri()
    velocita = 130 #km/h
    return distanza_km / velocita

vrsud_valdagno = calcola_tempo_viaggio(Misure(55_000))
print(vrsud_valdagno)