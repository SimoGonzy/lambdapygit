def aggiungi_candidato(nome_partito: str, nome_candidato: str):
    nuovo_candidato = {
        "nome": nome_candidato,
        "voti": 0
    }

    for pos in range(len(liste)):
        if liste[pos]["nome"] == nome_partito:
            liste[pos]["candidati"].append(nuovo_candidato)
            break