#Comuni

def aggiungi_partito(lista_partiti,nome_partito: str):
    nuovo_partito = {
        "nome": nome_partito,
        "candidati": []
    }

    lista_partiti.append(nuovo_partito)

#Funzione per aggiungere un nuovo candidato a un partito esistente
def aggiungi_candidato(lista_partiti, nome_partito: str, nome_candidato: str):
    nuovo_candidato = {
        "nome": nome_candidato,
        "n_voti": 0
    }

    for pos in range(len(lista_partiti)):
        if lista_partiti[pos]["nome"] == nome_partito:
            lista_partiti[pos]["candidati"].append(nuovo_candidato)
            break