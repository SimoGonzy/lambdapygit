import os
ricalcola : bool = True 
while ricalcola :
    num1_stringato : str = str(input("Inserisci il primo numero\t"))
    num2_stringato : str = str(input("Inserisci il secondo numero\t"))
    operatore : str = str(input("Inserisci l'operatore\t"))
    if num1_stringato.isnumeric() and num2_stringato.isnumeric() :
        num1 : float = float(num1_stringato)
        num2 : float =float(num2_stringato)

        match operatore :
            case "+" :
                print(num1 + num2)
                
            case "-" :
                print(num1 - num2)

            case "*" :
                print(num1 * num2)

            case "/" :
                if num2 == 0.0 :
                    print("Operazione impossibile: il divisore inserito è 0")
                else :
                    print(num1/num2)
            case _ :
                print("Il carattere inserito non e valido")
    ricalcola_string : str = str(input("Vuoi fare qualche altra operazione?[s/n]"))
    if ricalcola_string.lower() == "n" :
        ricalcola = False

    os.system("clear")

def calcolaGiorniDeiMesi(mese1) :
    match mese1 : 
        case 1 :
            giorni : int = 31
            return giorni
        case 2 : 
            giorni : int = 28
            return giorni
        case 3 : 
            giorni : int = 31
            return giorni
        case 4 :
            giorni : int = 30
            return giorni
        case 5 :
            giorni : int = 31
            return giorni
        case 6 :
            giorni : int = 30
            return giorni
        case 7 :
            giorni : int = 31
            return giorni
        case 8 :
            giorni : int = 31
            return giorni
        case 9 :
            giorni : int = 30
            return giorni
        case 10 :
            giorni : int = 31
            return giorni
        case 11 :
            giorni : int = 30
            return giorni
        case 12 :
            giorni : int = 31
            return giorni
        case _:
            print("errore nell'inserimento del mese")
            return giorni
        



anno : int = int(input("Inserisci l'anno di partenza"))
mase : int = int(input("inserisci il primo mese"))
giorno : int = str(input("inserisci il primo giorno"))

anno2 : int = int(input("Inserisci l'anno di arrivo"))
mase2 : int = int(input("inserisci il  mese di arrivo"))
giorno2 : int = str(input("inserisci il  giorno arrivo"))

if anno == anno2 :
    if mase == mase2 :
        if giorno == giorno2 :
            print("Hai inserito lo stesso giorno")
        elif giorno > giorno2 :
            print(f"Fra le due date ci sono{giorno - giorno2} giorni di differenza")
        else :
            print(f"Fra le due date ci sono{giorno2 - giorno} giorni di differenza")
    elif mase > mase2 :
        diff : int = mase2
        giorni_diff : int 
        giorni_diff = calcolaGiorniDeiMesi(mase2) - giorno2 # type: ignore
        while mase2 < mase :
            giorni_diff = giorni_diff + calcolaGiorniDeiMesi(diff) # pyright: ignore[reportUndefinedVariable]
            diff = diff + 1
        if diff == mase :
            giorni_diff = giorni_diff + giorno
    else :
        diff : int = mase
        giorni_diff : int 
        giorni_diff = calcolaGiorniDeiMesi(mase) - giorno
        while mase < mase2 :
            giorni_diff = giorni_diff + calcolaGiorniDeiMesi(diff)
            diff = diff + 1
        if diff == mase2 :
            giorni_diff = giorni_diff + giorno2
elif anno > anno2 :
    if mase == mase2 :
        if giorno == giorno2 :
            print("Ci sono 365 giorni di differenza")
        elif giorno > giorno2 :

            print(f"Fra le due date ci sono{365 + (giorno - giorno2)} giorni di differenza")
        else :
            print(f"Fra le due date ci sono{365 - (giorno2 - giorno)} giorni di differenza")
    elif mase > mase2 :
        diff : int = mase2
        giorni_diff : int 
        giorni_diff = calcolaGiorniDeiMesi(mase2) - giorno2
        while mase2 < mase :
            giorni_diff = giorni_diff + calcolaGiorniDeiMesi(diff)
            diff = diff + 1
        if diff == mase :
            giorni_diff = giorni_diff + giorno
        print(f"Fra le due date ci sono {(anno - anno2)* 365 + giorni_diff} giorni di differenza")
    else :
        diff : int = mase
        giorni_diff : int 
        giorni_diff = calcolaGiorniDeiMesi(mase) - giorno
        while mase < mase2 :
            giorni_diff = giorni_diff + calcolaGiorniDeiMesi(diff)
            diff = diff + 1
        if diff == mase2 :
            giorni_diff = giorni_diff + giorno2
        print(f"Fra le due date ci sono {(anno - anno2)* 365 - giorni_diff} giorni di differenza")
else :
    if mase == mase2 :
        if giorno == giorno2 :
            print(f"Ci sono {(anno2 - anno)*365 }g iorni di differenza")
        elif giorno > giorno2 :

            print(f"Fra le due date ci sono{365 - (giorno - giorno2)} giorni di differenza")
        else :
            print(f"Fra le due date ci sono{365 + (giorno2 - giorno)} giorni di differenza")
    elif mase > mase2 :
        diff : int = mase2
        giorni_diff : int 
        giorni_diff = calcolaGiorniDeiMesi(mase2) - giorno2
        while mase2 < mase :
            giorni_diff = giorni_diff + calcolaGiorniDeiMesi(diff)
            diff = diff + 1
        if diff == mase :
            giorni_diff = giorni_diff + giorno
        print(f"Fra le due date ci sono {(anno2 - anno)* 365 - giorni_diff} giorni di differenza")
    else :
        diff : int = mase
        giorni_diff : int 
        giorni_diff = calcolaGiorniDeiMesi(mase) - giorno
        while mase < mase2 :
            giorni_diff = giorni_diff + calcolaGiorniDeiMesi(diff)
            diff = diff + 1
        if diff == mase2 :
            giorni_diff = giorni_diff + giorno2
        print(f"Fra le due date ci sono {(anno2 - anno)* 365 + giorni_diff} giorni di differenza")





        





