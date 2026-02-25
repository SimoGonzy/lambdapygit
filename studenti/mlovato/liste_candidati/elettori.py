def vota_candidato(liste, nome_candidato: str, nome_partito: str):
    for partito in liste:
        if partito["nome"] == nome_partito:
            for candidato in partito["candidati"]:
                if candidato["nome"] == nome_candidato:
                    candidato["voti"] = candidato["voti"] + 1
                    return