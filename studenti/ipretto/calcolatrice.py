
continuare:bool = True

while continuare:

    operazione = input("Inserisci operazione (+, -, *, /, gg): ")   
    
    risposta:str    
    risultato: int

    if operazione == "+":
        n1 = int(input("Inserisci il primo numero: "))
        n2 = int(input("Inserisci il secondo numero: "))
        risultato = n1+n2
        print(risultato)

    elif operazione == "-":
        n1 = int(input("Inserisci il primo numero: "))
        n2 = int(input("Inserisci il secondo numero: "))
        risultato = n1-n2
        print(risultato)

    elif operazione == "*":
        n1 = int(input("Inserisci il primo numero: "))
        n2 = int(input("Inserisci il secondo numero: "))
        risultato = n1*n2
        print(risultato)

    elif operazione == "/":
        controllo_div:bool = True
        n1 = int(input("Inserisci il primo numero: "))

        while controllo_div:
            n2 = int(input("Inserisci il secondo numero: "))
            if n2 == 0:
                print("INSERISCI UN NUMERO DIVERSO DA 0")
            else:
                controllo_div = False

        risultato = n1/n2
        print(risultato)
    
    #da finire!!
    elif operazione == "gg":

        g1 = int(input("Inserisci il giorno 1: "))
        m1 = str(input("Inserisci il mese 1: "))
        a1 = int(input("Inserisci l'anno 1: "))

        g2 = int(input("Inserisci il giorno 2: "))
        m2 = str(input("Inserisci il mese 2: "))
        a2 = int(input("Inserisci l'anno 2: "))

        #variabili per salvare il numero del mese partendo dalla parola
        m1n:int
        m2n:int
        
        if(m1 == "gennaio" or m1 == "Gennaio"): m1=1
        if(m2 == "gennaio" or m2 == "Gennaio"): m2=1        
        if(m1 == "febbraio" or m1 == "Febbraio"): m1=2
        if(m2 == "febbraio" or m2 == "Febbraio"): m2=2
        if(m1 == "marzo" or m1 == "Marzo"): m1=3
        if(m2 == "marzo" or m2 == "Marzo"): m2=3
        if(m1 == "aprile" or m1 == "Aprile"): m1=4
        if(m2 == "aprile" or m1 == "Aprile"): m2=4
        if(m1 == "maggio" or m1 == "Maggio"): m1=5
        if(m2 == "maggio" or m2 == "Maggio"): m2=5
        
     


        if(a1 <= a2):
            diff_anno = a2-a1





        
    
    else:
        print("Scegli un operazione valida!")

#Ciclo di controllo per capire se l'utente vuole continuare, se risponde qualcosa di diverso da si, Si, no, No gli viene
#rifatta la domanda
    controllo:bool = True
    while controllo:
        risposta = input("Vuoi continuare? ")
        if risposta == "Si" or risposta == "si":
            continuare = True
            controllo = False
        elif risposta == "No" or risposta == "no":
            continuare = False
            controllo = False


