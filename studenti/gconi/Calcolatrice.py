decisione = ""
ris = ""
continuare = 0
while decisione != 0:
    if decisione != "":
        for i in range(1, 5):
            print("\n")
    print("inserisci un operazione")
    print("0)exit\n1)+\n2)-\n3)/\n4)*")
    if ris != "":
        print(f"ris:{ris}")
    try:
        decisione = int(input())
        if decisione == 1:
            if continuare == 0:
                print("inserisci il primo numero")
                num1 = int(input())
            else:
                num1 = ris
            print("inserisci il secondo numero")
            num2 = int(input())
            ris = num1 + num2
        elif decisione == 2:
            if continuare == 0:
                print("inserisci il primo numero")
                num1 = int(input())
            else:
                num1 = ris
            print("inserisci il secondo numero")
            num2 = int(input())
            ris = num1 - num2
        elif decisione == 3:
            if continuare == 0:
                print("inserisci il primo numero")
                num1 = int(input())
            else:
                num1 = ris
            print("inserisci il secondo numero")
            num2 = int(input())
            if num2 != 0:
                ris = num1 / num2
            else:
                ris = "impossibile"
                decisione = ""
        elif decisione == 4:
            if continuare == 0:
                print("inserisci il primo numero")
                num1 = int(input())
            else:
                num1 = ris
            print("inserisci il secondo numero")
            num2 = int(input())
            ris = num1 * num2
        elif decisione == 5:
            print("inserisci il primo anno")
            an1 = int(input())
            print("inserisci il primo mese")
            ms1 = int(input())
            print("inserisci il secondo anno")
            an2 = int(input())
            print("inserisci il secondo mese")
            ms2 = int(input())
            # giorni = calcolagiorni(ms1, an1) - calcolagiorni(ms2, an2)
        else:
            print("inserisci un opzione valida")
    except ValueError:
        print("inserisci un numero")
        decisione = ""
    if decisione in range(1, 5):
        print("vuoi continuare?\n1)si\n2)no")
        continuare = int(input())


def calcolagiorni(m, a):
    giorni = 0
    if m == 1:
        giorni = giorni + 31
    if m == 2:
        giorni = giorni + 28
    if m == 3:
        giorni = giorni + 31
    if m == 4:
        giorni = giorni + 30
    if m == 5:
        giorni = giorni + 31
    if m == 6:
        giorni = giorni + 30
    if m == 7:
        giorni = giorni + 31
    if m == 8:
        giorni = giorni + 31
    if m == 9:
        giorni = giorni + 30
    if m == 10:
        giorni = giorni + 31
    if m == 11:
        giorni = giorni + 30
    if m == 12:
        giorni = giorni + 31
    giorni = giorni + (a * 365)
    anno = a
    i = 0
    while anno > 0:
        anno - 4
        i + 1
    giorni = giorni + i
    return giorni
