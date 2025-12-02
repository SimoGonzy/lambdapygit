from comuni import aggiungi_candidato, aggiungi_partito
from elettori import vota_candidato
import os

partito1 = {"nome": "Partito di Valdagno", "candidati": [{"nome": "Tizio", "voti": 0}]}

partito2 = {"nome": "Partito di Recoaro", "candidati": [{"nome": "Caio", "voti": 0}]}

liste = [partito1, partito2]

elezioni = True


def mostra_risultati():
    for partito in liste:
        print(f"Partito: {partito['nome']}")
        for candidato in partito["candidati"]:
            print(f"- {candidato['voti']} : {candidato['nome']}")


while elezioni:
    print("Benvenuto al seggio!")
    print("Menù:")
    print("1 - vota")
    print("2 - candidati per un partito")
    print("3 - aggiungi un nuovo partito")
    print("Premi q per uscire")
    scelta = input("Fai la tua scelta: ")
    if scelta == "1":
        print("Vota il candidato:")
        nome_candidato = input("Nome del candidato a cui vuoi assegnare il" "voto")
        nome_partito = input("Partito di appartenenza del candidato")
        input("premi un bottone per continuare")
        os.system("clear")
    if scelta == "2":
        pass
        
        


aggiungi_partito(liste, "Partito di Schio")
aggiungi_candidato(liste, "prova", "Partito di Recoaro")
vota_candidato(liste, "prova", "Partito di Recoaro")
mostra_risultati()
