'''
Questo file è lo scheletro per risolvere la prima parte del giorno 2 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/2).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di tuple con due valori, dove:
    - il primo rappresenta l'ID di inizio intervallo;
    - il secondo rappresenta l'ID di fine intervallo.
'''


from parser import parse_exercise


def main():
    id_ranges: list[tuple[int, int]] = parse_exercise("./demo.txt")
    somma=0
   #print(id_ranges)

    # TODO: Implementare la soluzione utilizzando i range di ID contenuti in `id_ranges`

    for id_range in id_ranges:
        for num in range(id_range[0], id_range[1] + 1):
            num_str = str(num)

            parte_sinistra = num_str[:len(num_str) // 2] #parte sinistra : serve per dividere la stringa partenza e vai fino alla meta
            parte_destra = num_str[len(num_str) // 2:] #parte destra : serve per dividere la stringa parti dalla meta fino alla fine
           #print(parte_sinistra)
           #print(parte_destra)
           #input()
            if parte_sinistra == parte_destra:
                print(num)
                somma+=num
    print(f"\nSomma: {somma}")


if __name__ == "__main__":
    main()
