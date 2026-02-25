import random

rigioca : bool = True
num_segreto : int = random.randint(1, 50)
print(num_segreto)
giocatori : int = int(input("Quanti giocatori siete?[1/2]"))

while rigioca :
    if giocatori == 1 :

        tentativi : int = 5
    else :
        tentativi : int = 5
        tent : int = 5

    while tentativi > 0 :
        num : int  = int(input("Inserisci un numero compreso tra 1 e 50\n"))
        if num > num_segreto :
            print("il mio numero è più piccolo")
        elif num < num_segreto :
            print("il mio numero è più grande")
        else :
            print("HAI INDOVINATO!!")
            break

        tentativi = tentativi - 1

    if giocatori == 2 :
        print("E il turno del giocatore 2")
        while tent > 0 :
            num : int  = int(input("Inserisci un numero compreso tra 1 e 50\n"))
            if num > num_segreto :
                print("il mio numero è più piccolo")
            elif num < num_segreto :
                print("il mio numero è più grande")
            else :
                print("HAI INDOVINATO!!")
                break

            tent = tent - 1
        if tentativi > tent :
            print("Il giocatore 1 ha vinto")
        elif tentativi < tent :
            print("Il giocatore 2 ha vinto")
        else :
            print("La partita e finita i pareggio")
        replay : str = str(input("Volete rigiocare? inserisci qualsiasi cosa se vuoi rigiocare altrimenti premi solo invio"))
        rigioca = bool(replay)


        


    if giocatori == 1 :
        replay : str = str(input("Volete rigiocare? inserisci qualsiasi cosa se vuoi rigiocare altrimenti premi solo invio"))
        rigioca = bool(replay)
