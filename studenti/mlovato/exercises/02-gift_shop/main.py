'''
Questo file è lo scheletro per risolvere la prima parte del giorno 2 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/2).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di tuple con due valori, dove:
    - il primo rappresenta l'ID di inizio intervallo;
    - il secondo rappresenta l'ID di fine intervallo.
'''


from parser import parse_exercise


def main():
    id_ranges: list[tuple[int, int]] = parse_exercise("./demo.txt")
    contatore = 0
    for id_range in id_ranges:
        for num in range(id_range[0],id_range[1] + 1):
            num_str = str(num)

            num1 = num_str[:int(len(num_str)/2)]
            num2 = num_str[int(len(num_str)/2):]

            if num1 == num2:
                contatore += num


    print(contatore)

if __name__ == "__main__":
    main()
