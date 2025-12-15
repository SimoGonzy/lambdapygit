"""
Questo file è lo scheletro per risolvere la prima parte del giorno 3 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/3).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di stringhe, ciascuna rappresentante un banco di batterie.
"""

from parser import parse_exercise


def main():
    banks: list[str] = parse_exercise("./demo.txt")

    # TODO: Implementare la soluzione utilizzando i banchi contenuti in `banks`

    for bank in banks:
        for num in bank:
            num_max = "0"
            for c in num:
                if c > num_max:
                    num_max = c
            indice_max = 0
            for i in range(len(num)):
                if num[i] == num_max:
                    indice_max = i
                    break
            seconda_cifra = "0"
            for j in range(indice_max + 1, len(num)):
                if num[j] > seconda_cifra:
                    seconda_cifra = num[j]
            result = int(num_max + seconda_cifra)

            print(result)


if __name__ == "__main__":
    main()
