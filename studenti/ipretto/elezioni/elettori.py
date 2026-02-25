def voto_candidato(liste, nome_partito:str, nome_candidato:str):
    for pos in range(len(liste)):
        if liste[pos]["nome"] == nome_partito:
            for pos2 in range(len(liste[pos]["candidati"])):
                if liste[pos]["candidati"][pos2]["nome"] == nome_candidato:
                   liste[pos]["candidati"][pos2]["voti"] += 1
                   return