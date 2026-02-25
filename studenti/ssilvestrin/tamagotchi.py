class Bestia:
    def __init__(self, nome_bestia: str, fame: int, felicità: int, stanchezza: int):
        self.nome_bestia: str = nome_bestia
        self.fame: int = fame
        self.felicità: int = felicità
        self.stanchezza: int = stanchezza

    def stato_bestia(self):
        return f"Nome: {self.nome_bestia} - Fame: {self.fame} - Felicità: {self.felicità} - Stanchezza: {self.stanchezza}"
    
    def mangia(self, quantità_cibo: int):
        self.fame = max(0, self.fame - quantità_cibo)
        print(f"{self.nome_bestia} ha mangiato {quantità_cibo} unità di cibo.")
    
    def gioca(self, tempo_gioco: int):
        self.felicità += tempo_gioco
        self.stanchezza += tempo_gioco // 2
        print(f"{self.nome_bestia} ha giocato per {tempo_gioco} minuti.")

    def dormi(self, ore_dormite: int):
        self.stanchezza = max(0, self.stanchezza - ore_dormite * 2)
        self.felicità -= ore_dormite // 2
        self.fame -= ore_dormite // 2
        print(f"{self.nome_bestia} ha dormito per {ore_dormite} ore.")

    def salva_stato(self, summary_dict, filename):
        try:
            with open(filename, "w") as f:
                f.write(summary_dict.nome_bestia)
                f.write(f"\nFame: {summary_dict.fame}")
                f.write(f"\nFelicità: {summary_dict.felicità}")
                f.write(f"\nStanchezza: {summary_dict.stanchezza}")

        except:
            print(f"Errore nella creazione del file {Exception}")

    def carica_stato(self, filename):
        try:
            with open(filename, "r") as f:
                dati = f.read().split("\n")
                self.nome_bestia = dati[0]
                self.fame = int(dati[1].split(": ")[1])
                self.felicità = int(dati[2].split(": ")[1])
                self.stanchezza = int(dati[3].split(": ")[1])
        
        except:
            print(f"Errore nel caricamento del file {Exception}")


#Seleziona operazione

lista_bestie = []

while True:
    print("\nSeleziona cosa vuoi fare:")
    print("1 - Crea una nuova bestia")
    print("2 - Scegli con quale bestia giocare")
    print("3 - Carica stato bestia da file")
    print("4 - Salva stato bestia su file")
    print("5 - Esci")

    scelta = input("Seleziona un numero da 1 a 5: ")
    if scelta == "1":
        nome = input("Inserisci il nome della bestia: ").capitalize()
        bestia = Bestia(nome, fame=5, felicità=5, stanchezza=5)
        lista_bestie.append(bestia)
        print(f"Bestia {nome} creata!")

    elif scelta == "2":
        try:
            for i in range(len(lista_bestie)):
                print(f"{i + 1} - {lista_bestie[i].nome_bestia}")
            indice = int(input("Seleziona il numero della bestia con cui vuoi giocare: ")) - 1
            if 0 <= indice < len(lista_bestie):
                bestia = lista_bestie[indice]
                print(f"Hai scelto di giocare con {bestia.nome_bestia}.")
                print("1 - Mostra stato della bestia")
                print("2 - Dai da mangiare alla bestia")
                print("3 - Fai giocare la bestia")
                print("4 - Fai dormire la bestia")
                print("5 - Esci")
                scelta = input("Cosa vuoi fare con questa bestia?")
            if scelta == "1":
                try:
                    for i in range(len(lista_bestie)):
                        print(f"{i + 1} - {lista_bestie[i].nome_bestia}")
                        print(lista_bestie[i].stato_bestia())
                        if lista_bestie[i].fame >= 10 or lista_bestie[i].felicità <= 0 or lista_bestie[i].stanchezza >= 10:
                            print(f"La bestia {lista_bestie[i].nome_bestia} è morta.")
                            lista_bestie.pop(i)
                except:
                    print("Nessuna bestia creata. Crea una bestia prima.")

            elif scelta == "2":
                try:
                    quantità = int(input("Inserisci la quantità di cibo da dare: "))
                    bestia.mangia(quantità)
                    if bestia.fame >= 10 or bestia.felicità <= 0 or bestia.stanchezza >= 10:
                        print(f"La bestia {bestia.nome_bestia} è morta.")
                        lista_bestie.pop(i)
                except:
                    print("Nessuna bestia creata. Crea una bestia prima.")

            elif scelta == "3":
                try:
                    tempo = int(input("Inserisci il tempo di gioco in minuti: "))
                    bestia.gioca(tempo)
                    if bestia.fame >= 10 or bestia.felicità <= 0 or bestia.stanchezza >= 10:
                        print(f"La bestia {bestia.nome_bestia} è morta.")
                        lista_bestie.pop(i)
                except:
                    print("Nessuna bestia creata. Crea una bestia prima.")

            elif scelta == "4":
                try:
                    ore = int(input("Inserisci il numero di ore di sonno: "))
                    bestia.dormi(ore)
                    if bestia.fame >= 10 or bestia.felicità <= 0 or bestia.stanchezza >= 10:
                        print(f"La bestia {bestia.nome_bestia} è morta.")
                        lista_bestie.pop(i)
                except:
                    print("Nessuna bestia creata. Crea una bestia prima.")

            elif scelta == "5":
                print(f"La bestia {bestia.nome_bestia} è morta.")
                lista_bestie.pop(i)
        except:
            print("Seleziona un'opzione valida.")

    elif scelta == "3":
        filename = input("Inserisci il nome del file da cui caricare lo stato della bestia: ")
        try:
            bestia = Bestia("", 0, 0, 0)
            bestia.carica_stato(filename)
            lista_bestie.append(bestia)
            print(f"Bestia {bestia.nome_bestia} caricata dal file {filename}.")

        except:
            print("Errore nel caricamento del file. Assicurati che il file esista.")

    elif scelta == "4":
        filename = input("Inserisci il nome del file su cui salvare lo stato della bestia: ")
        try:
            print(f"Seleziona la bestia da salvare su {filename}:")
            for i in range(len(lista_bestie)):
                print(f"{i + 1} - {lista_bestie[i].nome_bestia}")
            indice = int(input("Seleziona il numero della bestia da salvare: ")) - 1
            if 0 <= indice < len(lista_bestie):
                bestia = lista_bestie[indice]
                bestia.salva_stato(bestia, filename)
                print(f"Stato della bestia {bestia.nome_bestia} salvato su {filename}.")
        except:
            print("Nessuna bestia creata. Crea una bestia prima.")

    elif scelta == "5":
        for i in range(len(lista_bestie)):
            print(f"la bestia {lista_bestie[i].nome_bestia} è morta.")
        break

    else:
        print("Scelta non valida, inserisci un numero da 1 a 3")

