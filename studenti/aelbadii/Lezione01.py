 
scelta:bool=True
n=1
while(scelta):
    operazione = input("Inserisci l'operazione che vuoi fare(+,-,x,:)\t")
    numero1= int(input (f"Inserisci il primo numero della {n}° operazione\t"))
    numero2= int(input (f"Inserisci il secondo numero della {n}° operazione\t"))

    if(operazione==":"):
        if(numero2==0):
            numero2=int(input("Inserisci un numero diverso da 0!!!!\t"))
            
        
        
    if(operazione=="+"):
        risultato=numero1+numero2

    elif(operazione=="-"):
        risultato=numero1-numero2

    elif(operazione=="x"):
        risultato=numero1*numero2

    elif(operazione==":"):
        risultato=numero1/numero2
    else:
        risultato="Operazione non valida"
 
    print("Risultato: ",risultato)

    cont=input("vuoi fare un altra operazione?")
    if(cont=="no"or cont=="NO"):
        scelta=False
    n=n+1

    


