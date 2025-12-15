"""
Questo file è lo scheletro per risolvere la prima parte del giorno 2 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/2).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di tuple con due valori, dove:
    - il primo rappresenta l'ID di inizio intervallo;
    - il secondo rappresenta l'ID di fine intervallo.
"""

from sys import meta_path

from parser import parse_exercise


def main():
    id_ranges: list[tuple[int, int]] = parse_exercise("./demo.txt")

    # TODO: Implementare la soluzione utilizzando i range di ID contenuti in `id_ranges`
    somma = 0
    for id_range in id_ranges:
        for id in range(id_range[0], id_range[1] + 1):
            s = str(id)
            l = len(s)
            if l % 2 == 0:
                metà = l // 2
                if s[:metà] == s[metà:]:
                    somma = somma + id

    print(somma)


if __name__ == "__main__":
    main()
