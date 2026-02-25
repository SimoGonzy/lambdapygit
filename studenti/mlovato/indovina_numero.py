import random
import os

# il gioco inizia con una fase di configurazione, posso cambiare
# il numero di tentativi (default = 5), di giocare in 1 o 2 (default 1)
# solo ora inizia il gioco, viene generato randomicamente un numero (nascosto all'utente)
# inizia il giocatore 1, cerca di indovinare, se non si indovina la console
# restituisce un indizio per il prossimo tentativo, la console viene pulita per 
# non dare indizi al giocatore 2, ora tocca al giocatore 2, deve indovinare, se non indovina
# la console restituisce un indizio
# infine viene chiesto se giocare nuovamente, il gioco ricorda la configurazione iniziale
# numero di tentativi e numero giocatori, usare c per tornare alla configurazione

num_max_range: int = 10
max_tentativi = 5
p2: bool = False # flag per giocare in 2
gioca_ancora: str = "c" # c per configurare il gioco
tentativiP1 = tentativiP2 = 0
punteggioP1 = punteggioP2 = 0


while(gioca_ancora != "n"):
    if gioca_ancora == "c":
        punteggioP1 = 0
        config_tentativi = input(f"Hai a disposizione {max_tentativi} tentativi, vuoi modificare? (y/n)").lower() # chiedo se cambiare il numero di tentativi
        if(config_tentativi == "y"):
            max_tentativi_str = input("Quanti tentativi vuoi fare? ")
            while(not(max_tentativi_str.isnumeric())):
                max_tentativi_str = input("Inserisci un numero. Quanti tentativi vuoi fare? ")
            max_tentativi = int(max_tentativi_str)
        tentativiP1 = max_tentativi
        giocatore2 = input("Vuoi giocare in 2? (y/n)").lower() # chiedo se giocare in 2
        if(giocatore2 == "y"):
            p2 = True
            punteggioP2 = 0   
    numero_misterioso = random.randint(0, num_max_range) # genero numero da indovinare
    tentativiP1 = max_tentativi
    if(p2):
            tentativiP2 = max_tentativi
    while(tentativiP1 > 0 or (p2 and tentativiP2 > 0)):
        os.system("clear") # pulisco console per avere una vista pulita
        print(f"P1 hai {"ancora " if tentativiP1 != max_tentativi else ""}{tentativiP1} tentativi") # gioca P1
        tentativiP1 = tentativiP1 - 1
        
        sceltaP1_str = input("Indovina il numero! ")
        while(not(sceltaP1_str.isnumeric())):
            sceltaP1_str = input("Inserisci un numero. Indovina il numero! ")
        sceltaP1 = int(sceltaP1_str)     
        print("--------------")
        if(sceltaP1 == numero_misterioso):
            print("P1 Hai vinto!")
            input("Premi un bottone per continuare.")
            punteggioP1 = punteggioP1 + 1
            os.system("clear")
            if(p2): # se P1 vince, P2 ha la possibilità di giocare per fare un pareggio
                print(f"P2 tocca a te, hai {"ancora " if tentativiP2 != max_tentativi else ""}{tentativiP2} tentativi")
                tentativiP2 = tentativiP2 - 1
                sceltaP2_str = input("Indovina il numero! ")
                while(not(sceltaP2_str.isnumeric())):
                    sceltaP2_str = input("Inserisci un numero. Indovina il numero! ")
                sceltaP2 = int(sceltaP2_str)  
                if(sceltaP2 == numero_misterioso):
                    print("P2 Hai vinto!")
                    punteggioP2 = punteggioP2 + 1
                input("Premi un bottone per continuare.")
                os.system("clear")
                break
            break
        elif sceltaP1 < numero_misterioso:
            if(tentativiP1 == 0):
                print(f"P1 hai perso! Il numero era: {numero_misterioso} sarai più fortunato la prossima volta")
            else:
                print("P1 Sei troppo basso, punta più in alto")
        else:
            if(tentativiP1 == 0):
                print(f"P1 hai perso! Il numero era: {numero_misterioso} sarai più fortunato la prossima volta")
            else:
                print("P1 Sei troppo alto, abbassa il tiro")
        input("Premi un bottone per continuare.")
        os.system("clear") # pulisco così può giocare P2 senza vedere cos'ha fatto P1
        if p2: # se ho deciso di giocare in 2
            print(f"P2 tocca a te, hai {"ancora " if tentativiP2 != max_tentativi else ""}{tentativiP2} tentativi")
            tentativiP2 = tentativiP2 - 1
            sceltaP2_str = input("Indovina il numero! ")
            while(not(sceltaP2_str.isnumeric())):
                sceltaP2_str = input("Inserisci un numero. Indovina il numero! ")
            sceltaP2 = int(sceltaP2_str)  
            if(sceltaP2 == numero_misterioso):
                print("P2 Hai vinto!")
                input("Premi un bottone per continuare.")
                punteggioP2 = punteggioP2 + 1
                os.system("clear")
                break
            elif sceltaP2 < numero_misterioso:
                if(tentativiP2 == 0):
                    print(f"P2 hai perso! Il numero era: {numero_misterioso} sarai più fortunato la prossima volta")
                else:
                    print("P2 Sei troppo basso, punta più in alto")
            else:
                if(tentativiP2 == 0):
                    print(f"P2 hai perso! Il numero era: {numero_misterioso} sarai più fortunato la prossima volta")
                else:
                    print("P2 Sei troppo alto, abbassa il tiro")
            input("Premi un bottone per continuare.")
            os.system("clear")
    if(not(p2)):
        print(f"Hai vinto {punteggioP1} volte")
    else:
        print("Il punteggio è:")
        print(f"P1: {punteggioP1}")
        print(f"P2: {punteggioP2}")
    gioca_ancora = input("Vuoi giocare ancora? (y/n) oppure (c) per tornare alla configurazione: ").lower()
    