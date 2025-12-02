def vota_candidato(liste, nome_partito: str, nome_candidato: str):
    for pos in range(len(liste)):
        if liste[pos]["nome"] == nome_partito:
            for i in range(len(liste[pos]["candidati"])):
                if liste[pos]["candidati"][i]["nome"] == nome_candidato:
                    liste[pos]["candidati"][i]["voti"] += 1
                    return