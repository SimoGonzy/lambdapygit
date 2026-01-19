from pathlib import Path
from time import sleep


class Tamagochi:
    def __init__(self, nome: str):
        self.nome = nome
        self.eta = 0
        self.fame = 0
        self.felicita = 0
        self.stanchezza = 0

    def nutri(self):
        self.fame -= 15
        self.stanchezza += 5

    def gioca(self):
        self.felicita += 20
        self.stanchezza += 15

    def dormi(self):
        self.stanchezza -= 30
        self.fame += 10
        self.felicita -= 10
        self.eta += 1

    def stato(self):
        print(f"Nome: {self.nome}")
        print(f"Fame: {self.fame}")
        print(f"Felicita: {self.felicita}")
        print(f"Stanchezza: {self.stanchezza}")

    def __str__(self):
        return f"Nome: {self.nome}\nFame: {self.fame}\nFelicita: {self.felicita}\nStanchezza: {self.stanchezza}"


class ListaTamagochi:
    def __init__(self):
        self.tamagochi = []

    def aggiungi(self, tamagochi):
        self.tamagochi.append(tamagochi)

    def rimuovi(self, nome):
        for tamagochi in self.tamagochi:
            if tamagochi.nome == nome:
                self.tamagochi.remove(tamagochi)
                break

    def stampa(self):
        for tamagochi in self.tamagochi:
            print(tamagochi)


class Adulto(Tamagochi):
    def __init__(self, nome):
        super().__init__(nome)

    def gioca(self):
        self.felicita += 15
        self.stanchezza += 5

    def nutri(self):
        self.fame -= 7
        self.stanchezza += 5


file = Path(
    "C:\\Users\\Admin\\Desktop\\progetti_python\\lambdapygit\\studenti\\aterzi\\tamagochi\\tamagochi.csv"
)

lista_tamagochi = ListaTamagochi()

with file.open("r") as f:
    next(f)
    for line in f:
        lista = line.strip().split(",")
        tamagochi = Tamagochi(lista[0])
        tamagochi.eta = int(lista[1])
        tamagochi.fame = int(lista[2])
        tamagochi.felicita = int(lista[3])
        tamagochi.stanchezza = int(lista[4])
        lista_tamagochi.aggiungi(tamagochi)

scelta = ""


while scelta != "0":
    scelta = input(
        "1. Creare un Tamagochi\n2. Nutrire\n3. Giocare\n4. Dormire\n5. Stato\n6. Aggiungi\n7. Rimuovi\n0. Esci\n"
    )
    if scelta == "1":
        nome = input("Come ti chiami? ")
        tamagochi = Tamagochi(nome)
        lista_tamagochi.aggiungi(tamagochi)
        print(tamagochi)
    elif scelta == "2":
        print("Con quale Tamagochi vuoi interagire?")
        nome = input("Inserisci il nome del Tamagochi: ")

        for tamagochi in lista_tamagochi.tamagochi:
            if tamagochi.nome == nome:
                tamagochi.nutri()
                break
        else:
            print("Tamagochi non trovato")
    elif scelta == "3":
        print("Con quale Tamagochi vuoi interagire?")
        nome = input("Inserisci il nome del Tamagochi: ")

        for tamagochi in lista_tamagochi.tamagochi:
            if tamagochi.nome == nome:
                tamagochi.gioca()
                break
        else:
            print("Tamagochi non trovato")
    elif scelta == "4":
        print("Con quale Tamagochi vuoi interagire?")
        nome = input("Inserisci il nome del Tamagochi: ")

        for tamagochi in lista_tamagochi.tamagochi:
            if tamagochi.nome == nome:
                tamagochi.dormi()
                break
        else:
            print("Tamagochi non trovato")
    elif scelta == "5":
        lista_tamagochi.stampa()

    elif scelta == "6":
        nome = input("Nome del Tamagochi da aggiungere: ")
        tamagochi = Tamagochi(nome)
        lista_tamagochi.aggiungi(tamagochi)
    elif scelta == "7":
        nome = input("Nome del Tamagochi da rimuovere: ")
        lista_tamagochi.rimuovi(nome)
    elif scelta == "0":
        print("Salvataggio in corso...")
        with file.open("w") as f:
            f.write("Nome,Fame,Felicita,Stanchezza\n")
            for tamagochi in lista_tamagochi.tamagochi:
                f.write(
                    f"{tamagochi.nome},{tamagochi.eta},{tamagochi.fame},{tamagochi.felicita},{tamagochi.stanchezza}\n"
                )
        print("Arrivederci!")
