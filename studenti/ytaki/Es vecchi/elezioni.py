from Package.comuni import aggiungi_candidato, aggiungi_partito
from Package.elettori import vota_candidato

partito1 = {
    "nome": "Partito di Valdagno",
    "candidati": [ { "nome": "Tizio", "voti": 0 } ]
}

partito2 = {
    "nome": "Partito di Recoaro",
    "candidati": [ { "nome": "Tizio", "voti": 0 } ]
}

liste = [ partito1, partito2 ]

aggiungi_partito(liste, "Partito di Schio")
aggiungi_candidato(liste, "Mario", "Partito di Schio")
vota_candidato(liste, "Partito di Schio", "Mario")
print(liste)