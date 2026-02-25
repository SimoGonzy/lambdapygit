"""
Questo file è lo scheletro per risolvere la prima parte del giorno 3 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/3).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di stringhe, ciascuna rappresentante un banco di batterie.
"""

from parser import parse_exercise


def main():
    banks: list[str] = parse_exercise("./test.txt")
    somma: int = 0
    for bank in banks:
        i = 0
        p = 0
        n = 0
        m = 0
        while i < len(bank) - 1:
            if int(bank[i]) > n:
                n = int(bank[i])
                p = i + 1
            i += 1
            """if int(bank[i]) > m and int(bank[i]) < n:
                m = int(bank[i])"""
        while p < len(bank):
            if int(bank[p]) > m:
                m = int(bank[p])
            p += 1

        stringa = str(n) + str(m)
        somma += int(stringa)
    print(somma)

    # TODO: Implementare la soluzione utilizzando i banchi contenuti in `banks`


if __name__ == "__main__":
    main()
