print ("Mini Calcolatrice")
print ("le operazioni disponibili sono seguenti:")
print ("-Calcolo Mensile")
print ("-Calcolo Mathematico")

richiesta = str(input("inserisci l'operazione da eseguire"))

#richesta al utente delle seguente inforazioni: per calcolo mathematico

num1 = float(input("inserisci il primo numero:"))
num2= float(input("inserisci il secondo numero:"))
operazioneMathematico= input("scegli l'operazione(+,-,*,/,):")
risultato=()
#esegue l'operazione
if operazioneMathematico == "+":
    risultato= num1+num2;
    print ("Risultato", risultato)

    
elif operazioneMathematico == "-":
    risultato= num1-num2;
    print ("Risultato", risultato)

    
elif operazioneMathematico == "*":
    risultato= num1*num2;
    print ("Risultato", risultato)

    
elif operazioneMathematico == "/":
    risultato= num1/num2;
    print ("Risultato", risultato)


else :
    print("l'operazione eseguita non è valida")

    print("FIne Calcolo")

