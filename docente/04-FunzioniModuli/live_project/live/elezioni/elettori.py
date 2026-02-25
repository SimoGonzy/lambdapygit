def vota_candidato(liste, nome_partito: str, nome_candidato: str):
    for partito in liste:
        if partito["nome"] == nome_partito:
            for candidato in partito["candidati"]:
                if candidato["nome"] == nome_candidato:
                    candidato["voti"] += 1
                    return
