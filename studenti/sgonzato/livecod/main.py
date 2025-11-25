from comuni import aggiungi_partito, aggiungi_candidato
from elettori import vota_candidato

partito1 = {
    "nome": "Partito di Valdagno",
    "candidati": [ { "nome" : "Tizio", "voti": 0} ]
}

partito2 = {
    "nome": "Partito di Recoaro",
    "candidati": [ { "nome" : "Caio", "voti": 0} ]
}

liste = [  ]
                   
aggiungi_partito(liste, input("\nCome si chiama il partito? "))
aggiungi_candidato(liste, "Mario", "Partito di Schio")
vota_candidato(liste, "Partito di Schio", "Mario")
print(liste)