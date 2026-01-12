"""
Questo file è lo scheletro per risolvere la prima parte del giorno 1 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/1).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di dizionari organizzati come segue:
    {
        direzione: str
        valore: int
    }
dove:
    - `direzione` è la lettera che indica la direzione della rotazione (L per sinistra, R per destra);
    - `valore` è il numero di posizioni di rotazione.
"""

from parser import ExerciseInput, parse_exercise


def main():
    rotations: list[ExerciseInput] = parse_exercise("./demo.txt")
    pos: int = 50
    password: int = 0
    for i in range(len(rotations)):
        if rotations[i]["direzione"] == "R":
            pos += rotations[i]["valore"]
            while pos > 99:
                pos = pos - 100
                password += 1
            print(password)
        elif rotations[i]["direzione"] == "L":
            if pos == 0:
                password -= 1
            pos -= rotations[i]["valore"]
            while pos < 0:
                pos = 100 + pos
                password += 1
            print(password)
        else:
            print("Errore")
        if pos == 0:
            password += 1
    # print(password)

    # TODO: Implementare la soluzione utilizzando le rotazioni contenute in `rotations`


if __name__ == "__main__":
    main()
