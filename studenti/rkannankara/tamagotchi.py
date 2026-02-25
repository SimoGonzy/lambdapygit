from pathlib import Path

file = Path("Python/lambdapygit/studenti/rkannankara/Tamagotchi.csv")


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
        self.felicita = max(self.felicita - 50, 0)
        self.stanchezza -= 50

    def __str__(self) -> str:
        return f"{self.nome} \n- fame: {self.fame} \n- felicita: {self.felicita} \n- stanchezza: {self.stanchezza}"


lista_tamagotchi = []

with file.open("r", encoding="utf-8") as f:
    next(f)
    for riga in f:
        campi = riga.strip().split(",")
        nome = campi[0]
        fame = int(campi[1])
        felicita = int(campi[2])
        stanchezza = int(campi[3])
        nuovo_tamagotchi = Tamagotchi(nome, fame, felicita, stanchezza)
        lista_tamagotchi.append(nuovo_tamagotchi)

while True:
    print("1 - Stato")
    print("2 - Azioni")
    print("3 - Aggiungere Tamagotchi")
    print("4 - Rimuovere Tamagotchi")
    print("0 - Esci")
    scelta = input("Cosa vuoi fare?  ")
    if scelta == "0":
        break
    elif scelta == "1":
        for tamagotchi in lista_tamagotchi:
            print(tamagotchi)
            print("-" * 10)
    elif scelta == "2":
        nome_tamagotchi = input("Nome del tamagotchi che vuoi:  ")
        trovato = False
        for tamagotchi in lista_tamagotchi:
            if tamagotchi.nome == nome_tamagotchi:
                trovato = True
                print("1 - Nutri")
                print("2 - Gioca")
                print("3 - Dormi")
                print("0 - Torna al Menu")
                scelta = input("Scegli l'azione:  ")
                if scelta == "0":
                    continue
                elif scelta == "1":
                    quantita_cibo = int(input("Quanto cibo gli diamo?  "))
                    tamagotchi.nutri(quantita_cibo)
                elif scelta == "2":
                    gioca = int(input("Quanto tempo puo giocare?  "))
                    tamagotchi.gioca(gioca)
                elif scelta == "3":
                    tamagotchi.dormi()
                break
        if not trovato:
            print(f"{nome_tamagotchi}: non trovato")
    elif scelta == "3":
        nome = input("Nome del nuovo Tamagotchi:  ")
        nuovo_tamagotchi = Tamagotchi(nome)
        lista_tamagotchi.append(nuovo_tamagotchi)
    elif scelta == "4":
        nome = input("Nome del tamagotchi da rimuovere:  ")
        for tamagotchi in lista_tamagotchi:
            if tamagotchi.nome == nome:
                lista_tamagotchi.remove(tamagotchi)


with file.open("w", encoding="utf-8") as f:
    f.write("nome,fame,felicita,stanchezza\n")
    for tamagotchi in lista_tamagotchi:
        f.write(
            f"{tamagotchi.nome},{tamagotchi.fame},{tamagotchi.felicita},{tamagotchi.stanchezza}\n"
        )
