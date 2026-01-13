'''
Questo file è lo scheletro per risolvere la prima parte del giorno 4 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/4).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una matrice di caratteri, con un '@' in ogni cella
in cui si trova un rotolo di carta e un '.' in ogni cella vuota.
'''


from parser import parse_exercise


def main():
    diagram: list[list[str]] = parse_exercise("./demo.txt")

    rows = len(diagram)
    cols = len(diagram[0])
    accessible_rolls = 0

    for r in range(rows):
        for c in range(cols):
            if diagram[r][c] == '@':
                neighbor_count = 0
                # Check all 8 directions
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if diagram[nr][nc] == '@':
                                neighbor_count += 1
                
                if neighbor_count < 4:
                    accessible_rolls += 1

    print(f"Accessible rolls: {accessible_rolls}")


if __name__ == "__main__":
    main()
