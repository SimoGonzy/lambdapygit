# 2. Indovina il Numero
# Scrivere un programma che genera un numero segreto e lo fa indovinare all’utente.
# Dopo ogni tentativo, il programma dovrebbe rispondere «troppo alto», «troppo basso» o «corretto!», contando il numero di tentativi e mostrandolo alla fine.
# Provare anche a:
# • Dare un numero massimo di tentativi (configurabile);
# • Permettere all’utente di giocare di nuovo;
# • Implementare un qualche tipo di multiplayer (locale!).

# utilizziamo il metodo random che serve per generare il numero casuale da indovinare
import random
from time import sleep

# variabili globali
num1 = 1
num2 = 15
tentativi = 5
riprova: bool = True

# menu di inizio
print("--- Benvenuto a 'Indovina il numero'! ---")
sleep(2)  # fa aspettare l'utente 2 secondi
print(f"Il tuo obbiettivo è quello di indovinare un numero tra {num1} e {num2}")
sleep(2)
print(f"Avrai a disposizione {tentativi} tentativi")
sleep(2)
print("Premi 'Invio' per continuare")
input()

# ciclo while utile per fare giocare l'utente più volte
while riprova:
    # t serve per rigenerare i tentativi nel momento in cui l'utente decide di giocare di nuovo
    t = tentativi
    # generiamo il numero casuale da indovinare
    num_generato = random.randint(num1, num2)

    # ciclo for che utilizziamo per tener conto dei tentativi
    for i in range(1, t + 1):
        print(f"\nTentativo {i}, inserisci un numero:")

        # Questi print servono per testare la correttezza del codice
        # print(f"NUMERO: {num_generato}")
        # print(f"TENTATIVI: {t}")

        # l'utente inserisce il numero
        scelta = int(input())

        # ora controlliamo se l'input dell'utente è uguale al numero generato
        if scelta == num_generato:
            # allora l'utente vince il gioco
            sleep(0.5)
            print(f" --- Complimenti hai indovinato il numero {scelta}! ---")

            # viene chiesto all'utente se vuole giocare di nuovo
            print("\nVuoi giocare di nuovo? (S/N)")
            val = str(input())

            # in caso in cui voglia giocare di nuovo viene aggiornata la variabile riprova e il gioco ricomincia
            if val == "S":
                riprova: bool = True
                sleep(0.5)
                # il "break" serve per uscire dal ciclo for e ritornare al ciclo while
                break
            else:
                # sennò aggiornando la variabile a "False" il gioco finisce
                riprova: bool = False
                sleep(1)
                print("--- Grazie per aver giocato! ---")

                # usciamo dal codice e il gioco finisce
                exit()
        else:
            # se il numero scelto è minore di quello generato allora scriviamo
            if scelta < num_generato:
                sleep(0.5)
                print(f"--- Numero troppo basso! Hai ancora {t - i} tentativi ---")
            # se il numero scelto è maggiore di quello generato allora scriviamo
            if scelta > num_generato:
                sleep(0.5)
                print(f"--- Numero troppo alto! Hai ancora {t - i} tentativi ---")

            # se i tentativi finiscono allora chiediamo all'utente se vuole rigiocare
            if i >= t:
                sleep(0.5)
                print("\nMi dispiace non hai vinto! Ritenta più tardi")

                # viene chiesto all'utente se vuole giocare di nuovo
                print("\nVuoi giocare di nuovo? (S/N)")
                val = str(input())
                sleep(0.5)

                # in caso in cui voglia giocare di nuovo viene aggiornata la variabile riprova e il gioco ricomincia
                if val == "S":
                    riprova: bool = True
                else:
                    # sennò aggiornando la variabile a "False" il gioco finisce
                    riprova: bool = False
                    sleep(1)
                    print("\n--- Grazie per aver giocato! ---")

                    # usciamo dal codice e il gioco finisce
                    exit()
