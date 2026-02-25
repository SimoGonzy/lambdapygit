# generatore di statistiche
#Generatore di Statistiche ⋆
#Scrivere un programma che chieda all’utente di inserire una serie
#di numeri e consenta successivamente di:

import statistics

#• Calcolare e stampare la media, la mediana e la moda dei numeri inseriti;

langs: list = []



while True:
    num = input("Inserisci un numero (o 'stop' per terminare): ")
    if num.lower() == 'stop':

        # Calcolo Massimo e Minimo
        max = max(langs)
        min = min(langs)
        print(f"Massimo: {max}")
        print(f"Minimo: {min}")

        # Estrazione Numeri Pari e Dispari
        pari = [num for num in langs if num % 2 == 0]
        dispari = [num for num in langs if num % 2 != 0]
        print(f"Numeri Pari: {pari}")
        print(f"Numeri Dispari: {dispari}")

        # Ordinamento Numeri
        ordinati = sorted(langs)
        print(f"Numeri Ordinati: {ordinati}")

        # Calcolo media
        media = sum(langs) / len(langs)
        print(f"Media: {round(media, 3)}")

        # Calcolo mediana
        print(f"Mediana: {statistics.median(langs)}")

        # Calcolo moda
        from collections import Counter
        count = Counter(langs)
        moda = count.most_common(2)
        print(f"Moda: {moda}")


        # Estrazione numeri sopra la media
        sopra_media = [num for num in langs if num > media]
        print(f"Numeri sopra la media: {sopra_media}")

        # Interrompo il ciclo
        break
    else:
        # Aggiungo il numero alla lista
        number = float(num)
        langs.append(number)



