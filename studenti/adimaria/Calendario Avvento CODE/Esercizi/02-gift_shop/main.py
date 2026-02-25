'''
Questo file è lo scheletro per risolvere la prima parte del giorno 2 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/2).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di tuple con due valori, dove:
    - il primo rappresenta l'ID di inizio intervallo;
    - il secondo rappresenta l'ID di fine intervallo.
'''

from parser import parse_exercise


def main():
    id_ranges: list[tuple[int, int]] = parse_exercise("./demo.txt")

    invalid_ids_sum = 0
    for start, end in id_ranges:
        for num in range(start, end + 1):
            s = str(num)
            length = len(s)
            if length % 2 == 0:
                half = length // 2
                if s[:half] == s[half:]:
                    invalid_ids_sum += num
    
    print(f"Sum of invalid IDs: {invalid_ids_sum}")


if __name__ == "__main__":
    main()
