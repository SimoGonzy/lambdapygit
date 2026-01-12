from comuni import aggiungiCandidato, nuovoPartito, vota_candidato

partito1 = {"nome": "Partito di Valdagno", "candidati": [{"nome": "Tizio", "voti": 0}]}
partito2 = {"nome": "Partito di Recoaro", "candidati": [{"nome": "Caio", "voti": 0}]}
liste = [partito1, partito2]

nuovoPartito(liste, input("inserisci pertito"))
aggiungiCandidato(liste, "Mario", "Partito di Schio")
vota_candidato(liste, "Partito di Schio", "Mario")
print(liste)
