'''
Questo file è lo scheletro per risolvere la prima parte del giorno 4 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/4).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una matrice di caratteri, con un '@' in ogni cella
in cui si trova un rotolo di carta e un '.' in ogni cella vuota.
'''


from parser import parse_exercise

def verifica_pos(x, y, len_x, len_y):
    if x in range(len_x):
        if y in range(len_y):
            return True
    return False

def main():
    diagram: list[list[str]] = parse_exercise("./puzzle_input.txt")
    contatore: int = 0
    directions = [[(x,y) for y in [-1, 0, 1] if x!=0 or y!=0] for x in [-1, 0, 1]]
    # TODO: Implementare la soluzione utilizzando il diagramma contenuto in `diagram`
    x=0
    y=0
    for x, riga in enumerate(diagram):
        for y, value in enumerate(riga):
            if value == "@":
                adiacenti: int = 0
                for row in directions:
                    for add_x, add_y in row:
                        if verifica_pos(x+add_x, y+add_y, len(diagram), len(diagram[0])):
                            if diagram[x+add_x][y+add_y] == "@":
                                adiacenti += 1
                if adiacenti < 4:
                    contatore += 1

    print(contatore)
if __name__ == "__main__":
    main()
