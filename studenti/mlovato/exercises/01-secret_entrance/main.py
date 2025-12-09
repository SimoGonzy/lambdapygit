'''
Questo file è lo scheletro per risolvere la prima parte del giorno 1 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/1).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di dizionari organizzati come segue:
    {
        direzione: str
        valore: int
    }
dove:
    - `direzione` è la lettera che indica la direzione della rotazione (L per sinistra, R per destra);
    - `valore` è il numero di posizioni di rotazione.
'''


from parser import ExerciseInput, parse_exercise


def main():
    rotations: list[ExerciseInput] = parse_exercise("./puzzle_input.txt")

    # TODO: Implementare la soluzione utilizzando le rotazioni contenute in `rotations`
    position: int = 50
    contatore: int = 0

    for rotation in rotations:
        # se la rotazione è a sinistra
        if rotation["direzione"] == "L":
            # i valori vanno da 0 a 99
            position = (position - rotation["valore"]) % 100
        else:
            # accetto valori da 0 a 99
            position = (position + rotation["valore"]) % 100

        if position == 0:
            contatore += 1
        
    
    print(contatore)

if __name__ == "__main__":
    main()
