# Dizionario che rappresenta un partito politico

from Elezioni.Comuni import aggiungi_partito, aggiungi_candidato
from Elezioni.Elettori import vota_candidato

partito_1 = {
    "nome": "Partito di Valdagno",
    "abbreviazione": "PDV",
    # Lista dei candidati del partito (Dizionario)
    "candidati": [
        {
            "nome": "Mario Rossi",
            "n_voti": 0,
        },]
}

partito_2 = {
    "nome": "Partito di Recoaro",
    "abbreviazione": "PDR",
    "candidati": [
        {
            "nome": "Luigi Bianchi",
            "n_voti": 0,
        },]
}

# Lista dei partiti
lista_partiti = [partito_1, partito_2]
"""
#Funzione per aggiungere un nuovo partito
def aggiungi_partito(nome_partito: str):
    nuovo_partito = {
        "nome": nome_partito,
        "candidati": []
    }

    lista_partiti.append(nuovo_partito)

#Funzione per aggiungere un nuovo candidato a un partito esistente
def aggiungi_candidato(nome_partito: str, nome_candidato: str):
    nuovo_candidato = {
        "nome": nome_candidato,
        "n_voti": 0
    }

    for pos in range(len(lista_partiti)):
        if lista_partiti[pos]["nome"] == nome_partito:
            lista_partiti[pos]["candidati"].append(nuovo_candidato)
            break

#Funzione per votare un candidato di un partito
def vota_candidato(nome_partito: str, nome_candidato: str):
    # Cerco il partito e il candidato
    for pos_par in range(len(lista_partiti)):
        if lista_partiti[pos_par]["nome"] == nome_partito:
            for pos_cand in range(len(lista_partiti[pos_par]["candidati"])):
                if lista_partiti[pos_par]["candidati"][pos_cand]["nome"] == nome_candidato:
                    lista_partiti[pos_par]["candidati"][pos_cand]["n_voti"] +=1
                    return
"""


#chiama le funzioni per testarle
aggiungi_partito(lista_partiti, "Partito di Schio")
aggiungi_candidato(lista_partiti, "Partito di Schio", "Giovanni Verdi")
vota_candidato(lista_partiti, "Partito di Schio", "Giovanni Verdi")

# Stampa la lista dei partiti per verificare le modifiche
print(lista_partiti)


