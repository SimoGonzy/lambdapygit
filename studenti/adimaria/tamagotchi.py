import csv
import os

class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.fame = 50      # 0 = Affamato, 100 = Sazio
        self.felicita = 50  # 0 = Triste, 100 = Felice
        self.stanchezza = 0 # 0 = Riposato, 100 = Esausto

    def is_vivo(self):
        return self.fame > 0

    def nutrisci(self):
        """Aumenta la fame (sazietà) e la stanchezza."""
        if not self.is_vivo():
            print(f"\n{self.nome} è morto di fame. Non può mangiare.")
            return

        if self.stanchezza >= 100:
            print(f"\n{self.nome} è troppo stanco per mangiare! Fallo dormire.")
            return

        print(f"\n{self.nome} sta mangiando...")
        self.fame = min(100, self.fame + 20)
        self.stanchezza = min(100, self.stanchezza + 10)

    def gioca(self):
        """Aumenta la felicità e la stanchezza."""
        if not self.is_vivo():
            print(f"\n{self.nome} è morto. Non può giocare.")
            return

        if self.stanchezza >= 100:
            print(f"\n{self.nome} è esausto! Deve dormire.")
            return

        print(f"\n{self.nome} sta giocando!")
        self.felicita = min(100, self.felicita + 20)
        self.stanchezza = min(100, self.stanchezza + 20)

    def dormi(self):
        """Diminuisce tutti i parametri (recupera stanchezza, ma scende sazietà e felicità)."""
        if not self.is_vivo():
            print(f"\n{self.nome} è morto. Non serve dormire.")
            return

        print(f"\n{self.nome} sta dormendo...")
        self.fame = max(0, self.fame - 20)
        self.felicita = max(0, self.felicita - 10)
        self.stanchezza = max(0, self.stanchezza - 50)

        if self.fame == 0:
            print(f"\n!!! {self.nome} è morto di fame nel sonno !!!")

    def mostra_stato(self):
        status = "VIVO" if self.is_vivo() else "MORTO 💀"
        print(f"\n--- Stato di {self.nome} ({status}) ---")
        print(f"Fame (Sazietà): {self.fame}/100")
        print(f"Felicità:       {self.felicita}/100")
        print(f"Stanchezza:     {self.stanchezza}/100")
        print("--------------------------")

def salva_dati(tamagotchis, filename="tamagotchis.csv"):
    try:
        with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Nome", "Fame", "Felicita", "Stanchezza"])
            for t in tamagotchis.values():
                writer.writerow([t.nome, t.fame, t.felicita, t.stanchezza])
        print(f"Dati salvati correttamente in {filename}!")
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")

def carica_dati(filename="tamagotchis.csv"):
    if not os.path.exists(filename):
        return {}
    tamagotchis = {}
    try:
        with open(filename, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                t = Tamagotchi(row["Nome"])
                t.fame = int(row["Fame"])
                t.felicita = int(row["Felicita"])
                t.stanchezza = int(row["Stanchezza"])
                tamagotchis[t.nome] = t
        print(f"Dati caricati da {filename}.")
        return tamagotchis
    except Exception as e:
        print(f"Errore durante il caricamento ({e}), si parte da zero.")
        return {}

def interagisci(tamagotchi):
    """Loop di interazione con un singolo Tamagotchi."""
    while True:
        tamagotchi.mostra_stato()
        print(f"\nAzioni per {tamagotchi.nome}:")
        print("1. Nutri")
        print("2. Gioca")
        print("3. Dormi")
        print("0. Torna al menu principale")

        scelta = input("Cosa vuoi fare? ")

        if scelta == "1":
            tamagotchi.nutrisci()
        elif scelta == "2":
            tamagotchi.gioca()
        elif scelta == "3":
            tamagotchi.dormi()
        elif scelta == "0":
            break
        else:
            print("Scelta non valida.")

def main():
    print("Benvenuto nel Tamagotchi Maker (Multi-Edition)!")
    tamagotchis = carica_dati() # Carica i salvataggi all'avvio

    while True:
        print("\n=== Menu Principale ===")
        vivi = [t.nome for t in tamagotchis.values() if t.is_vivo()]
        morti = [t.nome for t in tamagotchis.values() if not t.is_vivo()]

        print(f"\nTamagotchi Totali: {len(tamagotchis)}")
        if vivi:
            print(f"Attivi ({len(vivi)}): {', '.join(vivi)}")
        if morti:
            print(f"Morti ({len(morti)}): {', '.join(morti)} 💀")
        
        print("\n1. Crea nuovo Tamagotchi")
        print("2. Seleziona un Tamagotchi")
        print("3. Rimuovi un Tamagotchi")
        print("0. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            nome = input("Inserisci il nome del nuovo Tamagotchi: ").strip()
            if nome:
                if nome in tamagotchis:
                    print("Hai già un Tamagotchi con questo nome!")
                else:
                    tamagotchis[nome] = Tamagotchi(nome)
                    print(f"{nome} è nato!")
            else:
                print("Il nome non può essere vuoto.")

        elif scelta == "2":
            if not tamagotchis:
                print("Non hai ancora nessun Tamagotchi!")
                continue
            
            nome = input("Inserisci il nome del Tamagotchi con cui giocare: ").strip()
            if nome in tamagotchis:
                interagisci(tamagotchis[nome])
            else:
                print("Tamagotchi non trovato.")

        elif scelta == "3":
            if not tamagotchis:
                print("Non c'è nessuno da rimuovere.")
                continue

            nome = input("Chi vuoi rimuovere (nome)? ").strip()
            if nome in tamagotchis:
                del tamagotchis[nome]
                print(f"{nome} ci ha lasciato...")
            else:
                print("Tamagotchi non trovato.")

        elif scelta == "0":
            salva_dati(tamagotchis) # Salva prima di uscire
            print("Arrivederci!")
            break
        else:
            print("Comando non riconosciuto.")

if __name__ == "__main__":
    main()
