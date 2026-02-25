while True:
   try:
      num1 = float(input("Inserisci numero 1: "))
      num2 = float(input("Inserisci numero 2: "))
   except ValueError:
      print("Input non valido. Per favore inserisci dei numeri.")
      continue

   operazione = input("Inserisci operazione (+,-,*,/): ")

   if operazione == "+":
      risultato = num1 + num2
      print("Risultato:", risultato)
   elif operazione == "-":
      risultato = num1 - num2
      print("Risultato:", risultato)
   elif operazione == "*":
      risultato = num1 * num2
      print("Risultato:", risultato)
   elif operazione == "/":
      if num2 == 0:
         print("Errore: Divisione per zero non permessa.")
         continue
      risultato = num1 / num2
      print("Risultato:", risultato)
   else:
      print("Operazione non valida")

   continua = input("Vuoi fare un'altra operazione? (s/n): ")

   if continua.lower() != "s":
      print("Programma Terminato.")
      break
   
   giorni = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   
   mese1 = eval(input("Inserisci il primo mese: "))
   mese2 = eval(input("Inserisci il secondo mese: "))
   totale_giorni = 0
   for i in range(1, 13):
      if(i > (mese1 -1) and i < (mese2 + 1)):
          totale_giorni = totale_giorni + giorni[i]
          
print("La differenza in giorni tra i due mesi e':", totale_giorni)