from pathlib import Path

file = Path("tamagotchi.csv")

class Tamagotchi:
    def __init__(self, nome, fame=0, felicita=100, stanchezza=0) -> None:
        self.nome = nome
        self.fame = fame
        self.felicita = felicita
        self.stanchezza = stanchezza

    def nutri(self, quantita_cibo):
        if quantita_cibo <= self.fame:
            self.fame -= quantita_cibo
        else:
            self.fame = 0
        self.stanchezza += quantita_cibo
        if self.stanchezza > 100:
            self.stanchezza = 100
    def gioca(self, tempo=10):
        self.felicita += tempo
        if self.felicita > 100:
            self.felicita = 100
        self.stanchezza += tempo
        if self.stanchezza > 100:
            self.stanchezza = 100
    def dormi(self):
        self.fame = min(self.fame + 50, 100)
        self.felicita = max(0, self.felicita - 50)
        self.stanchezza = max(0, self.stanchezza - 50)
    def __str__(self) -> str:
        return f"{self.nome}:\n- fame: {self.fame}\n- felicita: {self.felicita}\n- stanchezza: {self.stanchezza}"

lista_tamagotchis: list[Tamagotchi] = []

with file.open("r", encoding="utf-8") as f:
    next(f)
    for riga in f:
        campi = riga.strip().split(',')
        nome = campi[0]
        fame = int(campi[1])
        felicita = int(campi[2])
        stanchezza = int(campi[3])
        new_tamagotchi = Tamagotchi(nome, fame, felicita, stanchezza)
        lista_tamagotchis.append(new_tamagotchi)


while True:
    print("1 - Stato")
    print("2 - Azioni")
    print("3 - Aggiungi tamagotchi")
    print("4 - Rimuovi tamagotchi")
    print("0 - Esci")
    scelta = input("Cosa vuoi fare? ")
    if scelta == "0":
        break
    elif scelta == "1":
        # stampo lo stato
        for tamagotchi in lista_tamagotchis:
            print(tamagotchi)
            print("-"*10)
    elif scelta == "2":
        # entro nel ramo azioni
        nome_tamagotchi = input("Nome del tamagotchi che vuoi? ")
        trovato = False
        for tamagotchi in lista_tamagotchis:
            if tamagotchi.nome == nome_tamagotchi:
                trovato = True
                print("1 - nutri")
                print("2 - gioca")
                print("3 - dormi")
                print("0 - esci")
                scelta = input("Scegli l'azione: ")
                if scelta == "0":
                    break
                elif scelta == "1":
                    quantita_cibo = int(input("Quanto cibo gli diamo? "))
                    tamagotchi.nutri(quantita_cibo)
                elif scelta == "2":
                    quanto_tempo = int(input("Quanto tempo vuoi giocare? "))
                    tamagotchi.gioca(quanto_tempo)
                elif scelta == "3":
                    tamagotchi.dormi()
        if not trovato:
            print(f"{nome_tamagotchi}: non trovato")
    elif scelta == "3":
        nome = input("Nome del nuovo Tamagotchi? ")
        new_tamagotchi = Tamagotchi(nome)
        lista_tamagotchis.append(new_tamagotchi)
    elif scelta == "4":
        nome = input("Nome del tamagotchi da rimuovere: ")
        for tamagotchi in lista_tamagotchis:
            if tamagotchi.nome == nome:
                lista_tamagotchis.remove(tamagotchi)

with file.open("w", encoding="utf-8") as f:
    f.write("nome,fame,felicita,stanchezza\n")
    for tamagotchi in lista_tamagotchis:
        f.write(f"{tamagotchi.nome},{tamagotchi.fame},{tamagotchi.felicita},{tamagotchi.stanchezza}\n")