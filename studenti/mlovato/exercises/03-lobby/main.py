'''
Questo file è lo scheletro per risolvere la prima parte del giorno 3 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/3).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di stringhe, ciascuna rappresentante un banco di batterie.
'''


from turtle import numinput
from parser import parse_exercise


def main():
    banks: list[str] = parse_exercise("./puzzle_input.txt")
    total: int = 0
    for bank in banks:
        max: int = 0
        for i in range(0,len(bank)):
            num_x: int = int(bank[i]) * 10
            if i<len(bank):
                for y in range(i+1, len(bank)):
                    num_y = int(bank[y])
                    if num_x + num_y > max:
                        max = num_x + num_y
        total += max
    print(total)



if __name__ == "__main__":
    main()
