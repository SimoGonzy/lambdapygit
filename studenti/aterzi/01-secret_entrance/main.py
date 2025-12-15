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

from turtle import position

from parser import ExerciseInput, parse_exercise


def main():
    rotations: list[ExerciseInput] = parse_exercise("./demo.txt")

    # TODO: Implementare la soluzione utilizzando le rotazioni contenute in `rotations`

    def rotate():
        posizione = 50
        val = posizione
        i = 0
        while i < len(rotations):
            if rotations[i]["direzione"] == "L" and rotations[i]["valore"] > posizione:
                posizione = 100 - rotations[i]["valore"] + val
                print(posizione)
            elif (
                rotations[i]["direzione"] == "L" and rotations[i]["valore"] <= posizione
            ):
                posizione = posizione - rotations[i]["valore"]
                print(posizione)
            elif (
                rotations[i]["direzione"] == "R"
                and rotations[i]["valore"] + posizione >= 100
            ):
                posizione = 0 + rotations[i]["valore"] - val
                print(posizione)
            else:
                posizione = val + rotations[i]["valore"]
                print(posizione)
                i += 1

            break

    rotate()


if __name__ == "__main__":
    main()
