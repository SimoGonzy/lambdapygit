'''
Questo file è lo scheletro per risolvere la prima parte del giorno 3 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/3).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di stringhe, ciascuna rappresentante un banco di batterie.
'''


from parser import parse_exercise


def main():
    banks: list[str] = parse_exercise("./demo.txt")

    # TODO: Implementare la soluzione utilizzando i banchi contenuti in `banks`


if __name__ == "__main__":
    main()
