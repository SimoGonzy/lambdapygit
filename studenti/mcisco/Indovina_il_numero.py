#Indovina il numero

import random
import os
gioca: int=0
while gioca !=1:
    print("Vuoi giocare\ny per giocare n per finier il gioco)")
    g: str = input()
    if g == 'y':
        os.system("cls")
        #assegnamento delle variabili
        N_segreto_p1: int = 0
        N_tentativi_p1: int = 0
        N_utente_p1: int = 0

        N_segreto_p2: int = 0
        N_tentativi_p2: int = 0
        N_utente_p2: int = 0

        N_segreto_p1 = random.randint(1,100)
        N_segreto_p2 = random.randint(1,100)

        print(f"INDOVINA IL NUMERO (da 1 a 100)\n")

        #while per p2
        while N_utente_p2 != N_segreto_p2:
            #while per p1
            while N_utente_p1 != N_segreto_p1:
                    print("Player 1")
                    N_utente_p1 = int(input("Prova ad Indovinare il numero  :"))

                    if N_utente_p1 == N_segreto_p1:
                        os.system('cls')
                        print(f"Numero Trovato\nNumero Tentativi {N_tentativi_p1}")
                    else:
                        print("Numero NON trovato")
                        if N_utente_p1 < N_segreto_p1:
                            print("Troppo Basso")
                            N_tentativi_p1 += 1
                        else:
                            print("Troppo Alto")
                            N_tentativi_p1 += 1
            #fine while p1

            print("Player 2")
            N_utente_p2 = int(input("Prova ad Indovinare il numero :"))

            if N_utente_p2 == N_segreto_p2:
                os.system('cls')
                print(f"Numero Trovato\nNumero Tentativi {N_tentativi_p2}")
            else:
                print("Numero NON trovato")
                if N_utente_p2 < N_segreto_p2:
                    print("Troppo Basso")
                    N_tentativi_p2 += 1
                else:
                    print("Troppo Alto")
                    N_tentativi_p2 += 1
        #fine while p2            
        os.system('cls')
        if N_tentativi_p1 < N_tentativi_p2:
            print(f"Vince Player 2\n Tentativi Player 1 -> {N_tentativi_p1}\n Tentativi Player 2 ->{N_tentativi_p2}\n ")

        elif N_tentativi_p1 > N_tentativi_p2:
            print(f"Vince Player 1\n Tentativi Player 1 -> {N_tentativi_p1}\n Tentativi Player 2 ->y {N_tentativi_p2}\n ")
        else:
            print(f"PAREGGIO\n Tentativi Player 1 {N_tentativi_p1}\n Tentativi Player 2 {N_tentativi_p2}\n ")
    else:
        print("Fine Gioco")
        gioca = 1




