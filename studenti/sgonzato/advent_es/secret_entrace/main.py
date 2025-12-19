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

    # TODO: Implementare la soluzione utilizzando le rotazioni contenute in `rotations`
    
    position = 50
    zeri = [0]
    
    for i in range(len(rotations)):
        position = rotate(rotations[i], position, zeri)
    print(position)
    print(zeri)
    
def rotate(rot, pos: int, zeri):
    side = rot["direzione"]
    num = rot["valore"]   
    
    if side == "L":
        step = -1
    else:
        step = +1

    for i in range(num):
        pos += step

        if pos < 0:
            pos = 99
        elif pos >= 100:
            pos = 0

        if pos == 0:
            zeri[0] += 1

    return pos
        
    """
    while pos < 0:
        pos = 100 + pos
        zeri[0] += 1
        print("\n+1 e pos: ", pos)
        
    while pos >= 100:
        pos = pos - 100
        zeri[0] += 1
        print("\n+1 e pos: ", pos)
        
    #per 1° parte
    #if pos == 0:
    #    zeri[0] += 1
    
    """


if __name__ == "__main__":
    main()