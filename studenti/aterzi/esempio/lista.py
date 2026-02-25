from comuni import aggiunta_candidato, aggiunta_partito
from elettori import vota_candidato

partito1 = {"nome": "partito di valdagno", "candidati": [{"nome": "tizio", "voti": 0}]}

partito2 = {"nome": "partito di recoaro", "candidati": [{"nome": "caio", "voti": 0}]}


liste = [partito1, partito2]


aggiunta_partito(liste, input("partito di schio"))
aggiunta_candidato(liste, "mario", "partito di schio")
vota_candidato(liste, "partito di schio", "mario")
print(liste)
