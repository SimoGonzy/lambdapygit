
#Calcolatrice Interattiva


#Creo le variabili per l'input dei numeri e dell'operazione
num1 = (input("Inserisci il primo numero: "))

#Controllo che i numeri siano validi
if isinstance(num1, float):
    pass
else:
    print("Inserisci un valore valido.")


num2 = (float(input("Inserisci il secondo numero: ")))

#Controllo che i numeri siano validi
if isinstance(num2, float):
    pass
else:
    print("Inserisci un valore valido.")
    

op = input("Inserisci l'operazione (+, -, *, /): ")

#Controllo che l'operazione sia valida
if op in ["+", "-", "*", "/"]:
    pass
else:
    print("Inserisci un simbolo valido tra +, -, * o /.")

#Creo la variabile per l'input di continuazione
cont = (str(input("Scrivi Y per continuare o N per uscire: ")))


#Eseguo la verifica dell'operazione scelta e stampo il risultato
#Controllo che l'utente voglia continuare
while cont == "Y" or cont == "y":

    #Controllo se l'utente vuole uscire
    if cont == "N" or cont == "n":
        break
        
    #Somma
    elif op == "+":
        res = num1 + num2
        print("La somma è:", res)
        cont = (str(input("Scrivi Y per codntinuare o N per uscire: "))) 

    #Sottrazione    
    elif op == "-":
        res = num1 - num2
        print("La sottrazione è:", res)
        cont = (str(input("Scrivi Y per codntinuare o N per uscire: ")))

    #Moltiplicazione
    elif op == "*":
        res = num1 * num2
        print("La moltiplicazione è:", res)
        cont = (str(input("Scrivi Y per codntinuare o N per uscire: ")))

    #Divisione
    elif op == "/":
        
        #Controllo del dividendo diverso da zero
        if num2 != 0:
            res = num1 / num2
            print("La divisione è:", res)
            cont = (str(input("Scrivi Y per codntinuare o N per uscire: ")))
        else:
            print("Non è possibile dividere per zero.")
            cont = (str(input("Scrivi Y per codntinuare o N per uscire: ")))






