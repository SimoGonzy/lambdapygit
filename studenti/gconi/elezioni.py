prova = 5
print(prova)
partito1 = {"nome": "Partito di Valdagno", "candidati": [{"nome": "Tizio", "voti": 0}]}
partito2 = {"nome": "Partito di Recoaro", "candidati": [{"nome": "Caio", "voti": 0}]}
liste = [partito1, partito2]


def nuovoPartito(nome_partito: str):
    nuovo_partito = {"nome": nome_partito, "candidati": []}
    liste.append(nuovo_partito)


def aggiungiCandidato(nome_candidato: str, nome_partito: str):
    nuovo_Candidato = {"nome": nome_candidato, "voti": 0}
    for pos in range(len(liste)):
        if liste[pos]["nome"] == nome_partito:
            liste[pos]["candidati"].append(nuovo_Candidato)
            break


def vota_candidato(nome_partito: str, nome_candidato: str):
    for pos in range(len(liste)):
        if liste[pos]["nome"] == nome_partito:
            for i in range(len(liste[pos]["candidati"])):
                if liste[pos]["candidati"][i]["nome"] == nome_candidato:
                    liste[pos]["candidati"][i]["voti"] += 1
                    return


nuovoPartito("Partito di Schio")
aggiungiCandidato("Mario", "Partito di Schio")
vota_candidato("Partito di Schio", "Mario")
print(liste)
