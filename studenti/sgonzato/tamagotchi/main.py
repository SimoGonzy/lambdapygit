from pathlib import Path
from time import sleep
from lib import *
        
#Codice principale

file: Path = Path(
    "C:\\Users\\gonza\\Documents\\Python\\lambdapygit\\studenti\\sgonzato\\tamagotchi\\tamagotchi_data.csv"
    )

lista_tamagotchi = ListaTamagotchi()

print("Caricamento in corso...")
sleep(2)

with file.open('r', encoding="utf-8") as f: 
            next(f)
            for x in f:
                lista = x.strip().split(",")
                
                pet = Tamagotchi(lista[0])
                pet.fame = int(lista[1])
                pet.felicita = int(lista[2])
                pet.stanchezza = int(lista[3])
                lista_tamagotchi.aggiungi_tamagotchi(pet)
                
scelta = ""

print("\n--- MENU --- \n1. Crea un nuovo Tamagotchi\n2. Nutri il Tamagotchi\n3. Fai giocare il Tamagotchi\n4. Fai dormire il Tamagotchi\n5. Mostra lo stato dei Tamagotchi\n6. Rimuovi un Tamagotchi\n0. Esci\n ------------")
while scelta != 0:
    
    scelta = int(input("\nScegli un'opzione: "))
    
    if scelta == 1:
        nome = input("\nInserisci il nome del tuo Tamagotchi: ")
        
        if(any(x.nome == nome for x in lista_tamagotchi.lista)):
            print("\nEsiste già un Tamagotchi con questo nome. Scegli un altro nome.")
            continue
        
        pet = Tamagotchi(nome)
        lista_tamagotchi.aggiungi_tamagotchi(pet)
        print(f"\nHai aggiunto {pet.nome} alla lista dei Tamagotchi.")

    elif scelta == 2:
        print("\nQuale Tamagotchi vuoi nutrire?")
        nome = input("Inserisci il nome del Tamagotchi: ")
        for x in lista_tamagotchi.lista: 
            if x.nome == nome:
                pet = x
                pet.nutrire()
                print(f"\nHai nutrito {pet.nome}.")
                break
        
    elif scelta == 3:
        print("\nQuale Tamagotchi vuoi fare giocare?")
        nome = input("Inserisci il nome del Tamagotchi: ")
        for x in lista_tamagotchi.lista: 
            if x.nome == nome:
                pet = x
                pet.giocare()
                print(f"\nHai fatto giocare {pet.nome}.")
                break
        
        
    elif scelta == 4:
        print("\nQuale Tamagotchi vuoi fare giocare?")
        nome = input("Inserisci il nome del Tamagotchi: ")
        for x in lista_tamagotchi.lista: 
            if x.nome == nome:
                pet = x
                pet.dormire()
                print(f"\n{pet.nome} ha dormito.")
                break
        
    elif scelta == 5:
        for x in lista_tamagotchi.lista: 
            pet = x
            pet.stato()
        
    elif scelta == 6:
        print("\nQuale Tamagotchi vuoi rimuovere?")
        nome = input("Inserisci il nome del Tamagotchi: ")
        for x in lista_tamagotchi.lista: 
            if x.nome == nome:
                pet = x
                lista_tamagotchi.rimuovi_tamagotchi(pet)
                print(f"\nHai rimosso {pet.nome} dalla lista dei Tamagotchi.")
                break
    
    elif scelta == 0:
        print("\nSalvataggio in corso...")
        sleep(2)
        
        #scrivo i dati nel file
        with file.open('w', encoding="utf-8") as f: 
            f.write("nome,fame,felicita,stanchezza\n")   
            for x in lista_tamagotchi.lista:
                f.write(f"{x.nome},{x.fame},{x.felicita},{x.stanchezza}\n")
        print("\nUscita dal programma.")