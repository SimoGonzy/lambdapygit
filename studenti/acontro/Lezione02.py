import random

print("Quanti giocatori siete?")
nplayer: int = int(input())
counter: int = 1
i: int = 1
while counter != 0:
    print("Quanti tentativi vuoi per indovinare?")
    max: int = int(input())
    print(max)
    while i <= nplayer:
        result: int = random.randint(0, 100)
        print(result)
        print(max)
        numt: int = 1
        while max != 0:
            print("Prova ad indovinare un numero da 0 a 100")
            tentativo: int = int(input())
            if tentativo == result:
                print(f"Complimenti! Player {i} ha indovinato in {numt} tentativi")
                break
            elif tentativo > result:
                print("Troppo alto")
            elif tentativo < result:
                print("Troppo basso")
            numt = numt + 1
            max = max - 1
            if max == 0:
                print(f"Non sei riuscito ad indovinare, la risposta era {result}")
            print(max)
        i += 1

    print("Vuoi giocare ancora? [Sì/No]")
    risposta: str = input()
    if risposta == "Sì":
        counter += 1
    elif risposta == "No":
        print("Grazie per aver giocato")
    counter -= 1
