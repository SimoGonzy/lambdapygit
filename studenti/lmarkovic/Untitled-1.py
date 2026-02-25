birra : int = 5
caffè : float = 1.5
campari : float = 3.50
thè : int = 3  

scelta : int = 0
somma : int = 0
while True :
    print("Menù di scelta, inserire Stop per uscire dal menù")
    print(f"1) birra {birra} ")
    print(f"2) caffè {caffè} ") 
    print(f"3) campari {campari} ") 
    print(f"4) thè {thè} ") 
    print("5) Stop \n")

    scelta = int(input("inserisci la tua scelta: "))
    if scelta != range(1,6) :
        print("scelta non valida riprova")

    if scelta == 1 :
        print("Hai scelto una birra \n")
        somma = somma + birra 
        print(f"La somma del tuo ordine attuale è {somma}\n")
        

    elif scelta == 2 :
        print(f"Hai scelto un caffè {caffè}\n")
        somma = somma + caffè
        print(f"La somma del tuo ordine attuale è {somma}\n")
        

    elif scelta == 3 :
        print(f"Hai scelto un campari {campari}")
        somma = somma + campari
        print(f"La somma del tuo ordine attuale è {somma}\n")
        

    elif scelta == 4 :
        print(f"Hai scelto un {thè}")
        somma = somma + thè
        print(f"La somma del tuo ordine attuale è {somma}\n")

    elif scelta == 5 : 
        print(f"la somma totale dell'ordine è {somma}\n")
        break

        






