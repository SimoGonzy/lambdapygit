'''
Questo file è lo scheletro per risolvere la prima parte del giorno 3 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/3).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di stringhe, ciascuna rappresentante un banco di batterie.
'''


from parser import parse_exercise


def main():
    banks: list[str] = parse_exercise("./demo.txt")

    total_joltage = 0
    for bank in banks:
        max_bank_joltage = 0
        # Iterate through all pairs of digits (preserving order)
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                # Form the 2-digit number
                joltage = int(bank[i] + bank[j])
                max_bank_joltage = max(max_bank_joltage, joltage)
        total_joltage += max_bank_joltage

    print(f"Total output joltage: {total_joltage}")


if __name__ == "__main__":
    main()
