from Comuni05 import aggiungi_candidato, aggiungi_partito
from Elettori05 import vota_candidato

partito1 = {"nome": "Partito di Valdagno", "candidati": [{"nome": "Tizio", "voti": 0}]}

partito2 = {"nome": "Partito di Valdagno", "candidati": [{"nome": "Caio", "voti": 0}]}

liste = [partito1, partito2]

aggiungi_partito("Partito di Schio")
aggiungi_candidato("Partito di Schio", "Mario")
vota_candidato("Partito di Schio", "Mario")
print(liste)
