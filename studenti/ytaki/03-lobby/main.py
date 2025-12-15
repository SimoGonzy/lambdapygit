"""
Questo file è lo scheletro per risolvere la prima parte del giorno 3 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/3).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di stringhe, ciascuna rappresentante un banco di batterie.
"""

"""
Ricavo i due numeri più grandi da ogni powerbank, ovvero ogni stringa di numeri, e controllo la posizione dei numeri più grandi, li concateno e li metto in un array per poi sommarli.
"""

from parser import parse_exercise
from functools import reduce


def main():
    banks: list[str] = parse_exercise("./demo.txt")

    max_voltages = []
    for bank in banks:
        b = bank
        b2 = []
        lb = len(b)
        max = 0

        # CONTROLLI PER OGNI BANK
        for i in range(lb):
            for j in range(i, lb - 1):
                a = int(b[i] + b[j + 1])
                b2.append(a)
        for i in range(len(b2)):
            if b2[i] > max:
                max = b2[i]
        max_voltages.append(max)
    # print(max_voltages)

    # SOMMA RISULTATI
    risultato = reduce(lambda x, y: x + y, max_voltages)

    print(risultato)


if __name__ == "__main__":
    main()
