from asyncio.windows_events import NULL
from os import system
from pathlib import Path


class tamagotchi:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 100
        self.happyness = 100
        self.tireness = 0
        self.age = 1

    @classmethod
    def load(cls, name: str, hunger: int, happyness: int, tireness: int, age: int):
        tama = tamagotchi(name)
        tama.happyness = happyness
        tama.hunger = hunger
        tama.tireness = tireness
        tama.age = age
        return tama

    def feed(self):
        if self.age > 10:
            self.hunger += 20
            self.tireness += 5
        else:
            self.hunger += 20
            self.tireness += 10

    def play(self):
        if self.age > 10:
            self.happyness += 20
            self.tireness += 5
        else:
            self.happyness += 20
            self.tireness += 10

    def sleep(self):
        if self.age > 10:
            self.happyness -= 10
            self.hunger -= 20
            self.tireness -= 10
        else:
            self.happyness -= 10
            self.hunger -= 10
            self.tireness -= 20
        self.age += 1

    def __str__(self) -> str:
        if self.age > 10:
            return f"{self.name}\nfame: {self.hunger}\nsonno: {self.tireness}\nfelicità: {self.happyness}\nage: adulto"
        else:
            return f"{self.name}\nfame: {self.hunger}\nsonno: {self.tireness}\nfelicità: {self.happyness}\nage: cucciolo"


file: Path = Path(
    "C:\\Users\\fizzo\\Documents\\python\\lambdapygit\\studenti\\gconi\\01-19\\salvataggio.csv"
)
select = ""
animali: list[tamagotchi] = []
with file.open("r", encoding="utf-8") as carica:
    if file.stat().st_size != 0:
        next(carica)
        for x in carica:
            lista = x.strip().split(",")
            tame = tamagotchi.load(
                lista[0], int(lista[1]), int(lista[2]), int(lista[3]), int(lista[4])
            )
            animali.append(tame)
while select != "0":
    select = input(
        "Scegli un opzione: \n0)esci \n1)crea nuovo tamagotchi \n2)selezione un tamagotchi \n3)lascia un tamagotchi \n4)salva \n5)mostra i tamagochi\n:"
    )
    system("cls")
    if select == "1":
        nome = input("inserisci il nome:\n")
        if list(filter(lambda x: x.name == nome, animali)) != []:
            print("il nome esiste già\n")
        else:
            tama = tamagotchi(nome)
            animali.append(tama)
    elif select == "2":
        nome = input("inserisci il nome:\n")
        animale = -1
        for x, y in enumerate(animali):
            if y.name == nome:
                animale = x
                break
        if animale != -1:
            select2 = ""
            while select2 != "0":
                select2 = input(
                    "Scegli un opzione: \n0)esci \n1)Sfama \n2)Gioca \n3)Dormi \n4)come sta\n:"
                )
                system("cls")
                if select2 == "1":
                    animali[animale].feed()
                elif select2 == "2":
                    animali[animale].play()
                elif select2 == "3":
                    animali[animale].sleep()
                elif select2 == "4":
                    print(animali[animale])
        else:
            print("il nome non esiste\n")
    elif select == "3":
        nome = input("inserisci il nome:\n")
        tama = list(filter(lambda x: x.name == nome, animali))
        if tama != []:
            animali.remove(tama[0])
        else:
            print("il nome non esiste\n")
    elif select == "4":
        with file.open("w", encoding="utf-8") as salvataggio:
            salvataggio.write("nome,fame,felicità,sonno,età\n")
            for tame in animali:
                salvataggio.write(
                    f"{tame.name},{tame.hunger},{tame.happyness},{tame.tireness},{tame.age}\n"
                )
    elif select == "5":
        for x in animali:
            print(x.name + "\n")
