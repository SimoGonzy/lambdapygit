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
    rotations: list[ExerciseInput] = parse_exercise("./mio.txt")
    dial: int = 50
    count: int = 0

    for pos in range (len(rotations)):
        if(rotations[pos]["direzione"] == 'L'):
            dial = dial - rotations[pos]["valore"]
            while(dial<0):
                dial = 100 + dial
            if(dial == 0):
                count = count + 1
        elif(rotations[pos]["direzione"] == 'R'):
            dial = dial + rotations[pos]["valore"]
            while(dial>99):
                dial = dial - 100
            if(dial == 0):
                count = count + 1
            
    print(count)
   


if __name__ == "__main__":
    main()
