'''
Questo file è lo scheletro per risolvere la prima parte del giorno 5 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/5).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in un dizionario organizzato come segue:
    {
        id_fresh: list[tuple[int, int]]
        ingredienti: list[int]
    }
dove:
    - `id_fresh` è la lista dei range di ID dei prodotti freschi;
    - `ingredienti` è la lista degli ID degli ingredienti disponibili.
'''


from parser import ExerciseInput, parse_exercise


def main():
    database: ExerciseInput = parse_exercise("./demo.txt")

    # TODO: Implementare la soluzione utilizzando i dati contenuti in `database`


if __name__ == "__main__":
    main()
