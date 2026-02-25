rubrica = {}
# per registrere un contatto
nome = input("inserici il nome del contatto : ")
numeroditelefono = input("inserici il numero :  ")
rubrica[nome] = numeroditelefono
print(rubrica)
# registrare piu contatti scelti dall'utente con un ciclo

rubrica = {}

while True:
    nome = input("Inserisci il nome (o 'stop' per uscire): ")
    if nome == "stop":
        break

    numero = input("Inserisci il numero: ")
    rubrica[nome] = numero
    # aggiungere un nuovo conatatto

    nome = input("Inserisci il nome: ")
    numero = input("Inserisci il numero: ")

if nome not in rubrica:
    rubrica[nome] = [numero]
    print("contto aggiunto")
else:
    print("contatto gia presente")
# cercare un conatto per nome

nomdacerc = input("inserici il nome del conattto da cercare")

if nomdacerc in rubrica:
    print(f"nome torvato", rubrica[nome])
else:
    print("conatto non trovato")
# Aggiungere / rimuovere un numero a un contatto
nome = input("Nome del contatto: ")
numero = input("Numero da aggiungere: ")

if nome in rubrica:
    rubrica[nome] = numero
    print("contatto aggiunto")
else:
    print("contatto gia essitente")
# rimuovere conattto
nome = input("Nome del contatto: ")

if nome in rubrica:
    del rubrica[nome]
    print("Contatto rimosso")
else:
    print("contatto non torvato")
