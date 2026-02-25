gennaio = 31
febbraio = 28
marzo = 31
aprile = 30
maggio = 31
giugno = 30
luglio = 31
agosto = 31
settembre = 30
ottobre = 31
novembre = 30
dicembre = 31

totale_anno = 0

mese1 = int(input("Inserisci mese").lower())
anno1 = int(input("Inserisci anno").lower())

mese2 = int(input("Inserisci mese").lower())
anno2 = int(input("Inserisci anno").lower())


totale_anno1 = 366 if anno1%400 == 0 and anno1%4 == 0 else 365
if(mese1 > 1):
    totale_anno1 = totale_anno1 - gennaio
if(mese1 > 2):
    if(anno1%400 == 0 and anno1%4 == 0):
        totale_anno1 = totale_anno1 - 29
    else:
        totale_anno1 = totale_anno1 - febbraio
if(mese1 > 3):
    totale_anno1 = totale_anno1 - marzo
if(mese1 > 4):
    totale_anno1 = totale_anno1 - aprile
if(mese1 > 5):
    totale_anno1 = totale_anno1 - maggio
if(mese1 > 6):
    totale_anno1 = totale_anno1 - giugno
if(mese1 > 7):
    totale_anno1 = totale_anno1 - luglio
if(mese1 > 8):
    totale_anno1 = totale_anno1 - agosto
if(mese1 > 9):
    totale_anno1 = totale_anno1 - settembre
if(mese1 > 10):
    totale_anno1 = totale_anno1 - ottobre
if(mese1 > 11):
    totale_anno1 = totale_anno1 - novembre

totale_anno2 = 0

if(mese2 >= 1):
    totale_anno2 = totale_anno2 + gennaio
if(mese2 >= 2):
    if(anno1%400 == 0 and anno1%4 == 0):
        totale_anno1 = totale_anno1 + 29
    else:
        totale_anno1 = totale_anno1 + febbraio
if(mese2 >= 3):
    totale_anno2 = totale_anno2 + marzo
if(mese2 >= 4):
    totale_anno2 = totale_anno2 + aprile
if(mese2 >= 5):
    totale_anno2 = totale_anno2 + maggio
if(mese2 >= 6):
    totale_anno2 = totale_anno2 + giugno
if(mese2 >= 7):
    totale_anno2 = totale_anno2 + luglio
if(mese2 >= 8):
    totale_anno2 = totale_anno2 + agosto
if(mese2 >= 9):
    totale_anno2 = totale_anno2 + settembre
if(mese2 >= 10):
    totale_anno2 = totale_anno2 + ottobre
if(mese2 >= 11):
    totale_anno2 = totale_anno2 + novembre
if(mese2 >= 12):
    totale_anno2 = totale_anno2 + dicembre

totale_anno = totale_anno1 + totale_anno2

if anno1 == anno2:
    if anno1%400 == 0 and anno1%4 == 0:
        totale_anno = totale_anno - 366
    else:
        totale_anno = totale_anno - 365

if anno1+1 < anno2: # se non sono sullo stesso anno, sommo tutti i giorni degli anni nel mezzo
    for anno in range(anno1+1, anno2):
        giorni_anno = 366 if anno%400 == 0 and anno%4 == 0 else 365
        totale_anno = totale_anno + giorni_anno

print(f"Totale dei giorni: {totale_anno}")
