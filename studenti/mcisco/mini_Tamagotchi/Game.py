"""
Game of Tamagotchi

"""
import os
from pathlib import Path
from typing import Optional
class Tamagotchi:
    def __init__(self, name: str, age: int, health: int, happiness: int, hunger: int, stanchezza: int):
        file_tamagotchi = Path(f"/home/matteo/Documenti/ITS_WorkSpace/Python/lambdapygit/studenti/mcisco/mini_Tamagotchi/{name}.txt")
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
        self.hunger = hunger
        self.stanchezza = stanchezza
        with file_tamagotchi.open("w", encoding="utf-8") as f:
            f.write(f"{name};{age};{health};{happiness};{hunger};{stanchezza}")
    """ 
    def apri(self, name: str):
        file_tamagotchi = Path(f"/home/matteo/Documenti/ITS_WorkSpace/Python/lambdapygit/studenti/mcisco/mini_Tamagotchi/{name}.txt")
        with file_tamagotchi.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.split(";")
                self.name = line[0]
                self.age = line[1]
                self.health = line[2]
                self.happiness = line[3]
                self.hunger = line[4]
                self.stanchezza = line[5]
        print(line)
        input()
    """

    def set_name(self, name: str):
        self.name = name
    
    def set_age(self, age: int):
        self.age = age

    def set_health(self, health: int):
        self.health = health
    
    def set_happiness(self, happiness: int):
        self.happiness = happiness

    def set_hunger(self, hunger: int):
        self.hunger = hunger
    
    def set_stanchezza(self, stanchezza: int):
        self.stanchezza = stanchezza

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_health(self):
        return self.health
    
    def get_happiness(self):
        return self.happiness
    
    def get_hunger(self):
        return self.hunger
    
    def get_stanchezza(self):
        return self.stanchezza
    
    def __str__(self):
        return f"{self.name} - {self.age} anni - {self.health} salute - {self.happiness} felicita - {self.hunger} hunger - {self.stanchezza} stanchezza"
    
    def status(self):
        str_vita = ""
        str_felicita = ""
        str_fame = ""
        str_stanchezza = ""


        for i in range(1, self.health + 1):
            str_vita += "❤"

        for i in range(1, self.happiness + 1):
            str_felicita += "😊"

        for i in range(1, self.hunger + 1):
            str_fame += "🍔"

        for i in range(1, self.stanchezza + 1):
            str_stanchezza += "💪"

        print(f"{self.name} - {self.age} anni\nSalute: {str_vita}\nFelicita:{str_felicita}\nSazieta': {str_fame}\nStanchezza: {str_stanchezza}\n")
        
    def mangia(self):
        self.hunger += 1
        self.stanchezza += 1
    
    def giocare(self):
        self.happiness += 1
        self.stanchezza += 1

    def dormire(self):
        self.happiness -= 1
        self.stanchezza -= 1
        self.hunger -= 1

    #def aggiorna(self):

    
    
#--------------------------------------------------------------------------------------------#

#Inizia il gioco da qui

gioco = True

while gioco:
    os.system('clear')
    print("Tamagotchi Game\n")

    #-------#
    #mostro
    #-------#

    print("0 - Esci\n1 - Crea il tuo Tamagotchi\n2 - Lista dei Tamagotchi\n3 - Apri un Tamagotchi\n4 - Rimuovi un Tamagotchi")
    scelta = int(input())

    if(scelta == 0):
        os.system('clear')
        print("\nGrazie per aver giocato\nArrivederci")
        gioco = False
    elif(scelta == 1):
        os.system('clear')
        name = input("Inserisci il nome del tuo Tamagotchi: ")
        age = int(input("Inserisci l'eta del tuo Tamagotchi: "))
        health = int(input("Inserisci la salute del tuo Tamagotchi: "))
        happiness = int(input("Inserisci la felicita del tuo Tamagotchi: "))
        hunger = int(input("Inserisci la sazieta' del tuo Tamagotchi: "))
        stanchezza = int(input("Inserisci la stanchezza del tuo Tamagotchi: "))
        tamagotchi = Tamagotchi(name, age, health, happiness, hunger, stanchezza)

        os.system('clear')
        #print(tamagotchi)
        tamagotchi.status()
        input()
    elif(scelta == 2):
        os.system('clear')
        print("Tamagotchi: ")

        for file in os.listdir("/home/matteo/Documenti/ITS_WorkSpace/Python/lambdapygit/studenti/mcisco/mini_Tamagotchi"):
            if(file.endswith(".txt")):
                print(file[:-4])

        input()
    elif(scelta == 3):
        os.system('clear')
        try:
            n = input("Inserisci il nome del Tamagotchi da caricare: ")
            with open(f"/home/matteo/Documenti/ITS_WorkSpace/Python/lambdapygit/studenti/mcisco/mini_Tamagotchi/{n}.txt", "r") as f:
                dati = f.read().split(";")
                tamagotchi = Tamagotchi(dati[0], int(dati[1]), int(dati[2]), int(dati[3]), int(dati[4]), int(dati[5]))
                tamagotchi.status()
                input()

                try:
                    azioni = "y"
                    while azioni != "n":
                        print("Tamagotchi Game\n")
                        azioni = input("Vuoi giocare con il tuo Tamagotchi? (y/n): ")
                        
                        if(azioni == "y"):
                            print("0 - Esci\n1 - Mangia\n2 - Gioca\n3 - Dormi\n")
                            azione = int(input())
                            if(azione == 1):
                                tamagotchi.mangia()
                            elif(azione == 2):
                                tamagotchi.giocare()
                            elif(azione == 3):
                                tamagotchi.dormire()
                            tamagotchi.status()
                            input()
                            with open(f"/home/matteo/Documenti/ITS_WorkSpace/Python/lambdapygit/studenti/mcisco/mini_Tamagotchi/{n}.txt", "w") as f:
                                f.write(f"{tamagotchi.name};{tamagotchi.age};{tamagotchi.health};{tamagotchi.happiness};{tamagotchi.hunger};{tamagotchi.stanchezza}")
                except:
                    print("Tamagotchi non trovatooooo")
        except:
            print("Tamagotchi non trovato")
    elif(scelta == 4):
        os.system('clear')
        r = input("Inserisci il nome da riumuovere: ")
        os.remove(f"/home/matteo/Documenti/ITS_WorkSpace/Python/lambdapygit/studenti/mcisco/mini_Tamagotchi/{r}.txt")

        for file in os.listdir("/home/matteo/Documenti/ITS_WorkSpace/Python/lambdapygit/studenti/mcisco/mini_Tamagotchi"):
            if(file.endswith(".txt")):
                print(file[:-4])

        input()

    else:
        os.system('clear')
        print("Scelta non valida")
        input()
