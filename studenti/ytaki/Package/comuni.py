def aggiungi_partito(liste: str, nome_partito: str):
    nuovo_partito = {
        "nome": nome_partito,
        "candidati": []
    }
    
    liste.append(nuovo_partito)

def aggiungi_candidato(liste: str, nome_candidato: str, nome_partito: str):
    nuovo_candidato = {
        "nome": nome_candidato,
        "voti": 0
    }

    for i in range(len(liste)):
        if (liste[i]["nome"] == nome_partito):
            liste[i]["candidati"].append(nuovo_candidato)
            break