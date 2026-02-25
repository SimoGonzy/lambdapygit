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
    rotations: list[ExerciseInput] = parse_exercise("./demo2.txt")
    position = 50
    # TODO: Implementare la soluzione utilizzando le rotazioni contenute in `rotations`
    zeri = [0, 0]
    for i in range(len(rotations)):
        position = rotate(rotations[i], position, zeri)
        if position != 0:
            zeri[1] = 0
    print(position)
    print(zeri[0])


def rotate(rot, pos: int, zeri):
    side = rot["direzione"]
    num = rot["valore"]
    print(pos)
    if side == "L":
        pos -= num
        if pos == 0:
            if zeri[1] == 0:
                zeri[1] = 1
                zeri[0] += 1
                print("+1")
            else:
                zeri[1] = 0
    else:
        pos += num
        if pos == 0:
            if zeri[1] == 0:
                zeri[1] = 1
                zeri[0] += 1
                print("+1")
            else:
                zeri[1] = 0
    i = 0
    while pos < 0:
        i += 1
        pos = 100 + pos
        if zeri[1] == 0 or i > 0:
            zeri[0] += 1
            zeri[1] = 1
            print("+1")
        else:
            zeri[1] = 0
    while pos >= 100:
        i += 1
        pos = pos - 100
        if zeri[1] == 0 or i > 0:
            zeri[0] += 1
            zeri[1] = 1
            print("+1")
        else:
            zeri[1] = 0
    return pos


if __name__ == "__main__":
    main()
