def aggiungi_partito(liste, nome_partito: str):
    nuovo_partito = {
        "nome": nome_partito,
        "candidati": []
    }
    liste.append(nuovo_partito)

def aggiungi_candidato(liste, nome_candidato: str, nome_partito: str):
    nuovo_candidato = {
        "nome": nome_candidato,
        "voti": 0
    }
    for pos in range(len(liste)):
        if liste[pos]["nome"] == nome_partito:
            liste[pos]["candidati"].append(nuovo_candidato)
            break