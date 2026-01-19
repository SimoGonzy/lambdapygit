from comune import aggiungi_partito, aggiungi_candidato
from elletori import vota_candidato


partito1 = {
    "nome": "Partito di valdagno",
    "candidati": [{ "nome": "Tizio", "voti": 0 }]
}

partito2 = {
    "nome": "Partito di recoaro",
    "candidati": [{ "nome": "Alice", "voti": 0 }]
}

liste = [partito1, partito2]


def aggiungi_partito(nome_partito: str):
    nuovo_partito = {
        "nome": nome_partito,
        "candidati": []
    }

    liste.append(nuovo_partito)


def aggiungi_candidato(nome_partito: str, nome_candidato: str):
    nuovo_candidato = {
        "nome": nome_candidato,
        "voti": 0
    }

    for pos in range(len(liste)):
        if liste[pos]["nome"] == nome_partito:
            liste[pos]["candidati"].append(nuovo_candidato)
            break


def vota_candidato(nome_partito: str, nome_candidato: str):
    for pos in range(len(liste)):
        if liste[pos]["nome"] == nome_partito:

        
            for pos2 in range(len(liste[pos]["candidati"])):
                if liste[pos]["candidati"][pos2]["nome"] == nome_candidato:
                    liste[pos]["candidati"][pos2]["voti"] += 1
                    return
