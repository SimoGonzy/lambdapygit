def aggiungi_partito(nome_partito: str):
    nuovo_partito = {
    "nome":nome_partito,
    "candidati":[]
    }
    liste.append(nuovo_partito)

def aggiungi_candidato(nome_candidato: str, nome_partito: str):
    nuovo_candidato={
        "nome": nome_candidato,
        "voti":0
    }
    for pos in range(len(liste)):
        if(liste[pos]["nome"]==nome_partito):
            liste[pos]["candidati"].append(nuovo_candidato)
            break

def voto_candidato(nome_partito: str, nome_candidato:str):
    for pos in range(len(liste)):
        if liste[pos]["nome"]==nome_partito:
            for pos1 in range(len(liste[pos]["candidati"])):
                if liste[pos]["candidati"][pos1]["nome"]==nome_candidato:
                    liste[pos]["candidati"][pos1]["voti"] += 1
                    return
                   
    
 
 
partito1 = {
    "nome":"Partito di Valdagno",
    "candidati":[ { "nome": "Tizio", "voti":0 } ]
}

partito2 = {
    "nome":"Partito di Recoaro",
    "candidati":[ { "nome": "Caio", "voti":0 } ]
}

liste=[partito1 , partito2]

aggiungi_partito(input("Come si chiama il partito"))
aggiungi_candidato("Mario", "Partito di Schio")
voto_candidato("Partito di Schio","Mario")
print(liste)