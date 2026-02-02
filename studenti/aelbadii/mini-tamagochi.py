import csv
import os

class Tamagotchi:
    def __init__(self, nome, fame=50, felicita=50, stanchezza=0):
        self.nome = nome
        self.fame = int(fame)
        self.felicita = int(felicita)
        self.stanchezza = int(stanchezza)

    def nutre(self):
        self.fame = max(0, self.fame - 20)
        self.stanchezza = min(100, self.stanchezza + 10)

    def gioca(self):
        self.felicita = min(100, self.felicita + 20)
        self.stanchezza = min(100, self.stanchezza + 15)

    def dorme(self):
        self.fame = min(100, self.fame + 10)
        self.felicita = max(0, self.felicita - 5)
        self.stanchezza = 0

def main():
    pets = []
    if os.path.exists('pets.csv'):
        with open('pets.csv', 'r') as f:
            for riga in csv.reader(f):
                if riga: pets.append(Tamagotchi(*riga))

    while True:
        print("\n--- GESTORE TAMAGOTCHI ---")
        if not pets:
            print("Lista vuota. Aggiungi un animaletto!")
        else:
            for i, p in enumerate(pets):
                print(f"{i+1}. {p.nome} (Fame: {p.fame} | Felicità: {p.felicita} | Stanchezza: {p.stanchezza})")
        
        print("\n[ID] Scegli numero | [A] Aggiungi | [R] Rimuovi | [E] Esci")
        scelta = input("Operazione: ").strip().lower()

        if scelta == 'e':
            with open('pets.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                for p in pets: writer.writerow([p.nome, p.fame, p.felicita, p.stanchezza])
            print("Progressi salvati. Ciao!")
            break
        
        elif scelta == 'a':
            nome = input("Nome del nuovo Tamagotchi: ")
            pets.append(Tamagotchi(nome))
            print(f"{nome} creato con successo!")
        
        elif scelta == 'r':
            try:
                idx = int(input("Inserisci l'ID del Tamagotchi da rimuovere: ")) - 1
                if 0 <= idx < len(pets):
                    r = pets.pop(idx)
                    print(f"{r.nome} rimosso.")
            except ValueError:
                print("Inserisci un numero valido!")
        
        elif scelta.isdigit():
            idx = int(scelta) - 1
            if 0 <= idx < len(pets):
                p = pets[idx]
                while True:
                    print(f"\n--- INTERAGISCI CON {p.nome.upper()} ---")
                    print(f"Stato: Fame {p.fame}, Felicità {p.felicita}, Stanchezza {p.stanchezza}")
                    print("1. Nutri | 2. Gioca | 3. Dormi | 4. Indietro")
                    azione = input("Scegli: ")
                    if azione == '1': p.nutre()
                    elif azione == '2': p.gioca()
                    elif azione == '3': p.dorme()
                    elif azione == '4': break

if __name__ == "__main__":
    main()