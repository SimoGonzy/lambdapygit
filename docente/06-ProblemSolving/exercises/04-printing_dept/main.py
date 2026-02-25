'''
Questo file è lo scheletro per risolvere la prima parte del giorno 4 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/4).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una matrice di caratteri, con un '@' in ogni cella
in cui si trova un rotolo di carta e un '.' in ogni cella vuota.
'''


from parser import parse_exercise


def main():
    diagram: list[list[str]] = parse_exercise("./demo.txt")

    # TODO: Implementare la soluzione utilizzando il diagramma contenuto in `diagram`


if __name__ == "__main__":
    main()
