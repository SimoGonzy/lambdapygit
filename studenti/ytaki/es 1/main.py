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
    rotations: list[ExerciseInput] = parse_exercise("./demo.txt")

    posizione = 50
    zeri = 0

    # TODO: Implementare la soluzione utilizzando le rotazioni contenute in `rotations`
    for rotation in rotations:
        if rotation["direzione"] == "L":
            posizione = (posizione - rotation["valore"]) % 100
        else:
            posizione = (posizione + rotation["valore"]) % 100

        if(posizione == 0):
            zeri += 1
    print(zeri)

if __name__ == "__main__":
    main()
