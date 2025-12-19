'''
Questo file è lo scheletro per risolvere la prima parte del giorno 3 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/3).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di stringhe, ciascuna rappresentante un banco di batterie.
'''


from parser import parse_exercise


def main():
    banks: list[str] = parse_exercise("./demo.txt")

    # TODO: Implementare la soluzione utilizzando i banchi contenuti in `banks`
    
    parola = banks[3]
    max = int(parola[0] + parola[1])
    for i in range(len(parola)):
        for j in range(1, len(parola) - i):
            if int(parola[i] + parola[j + i]) > max:
                max = int(parola[i] + parola[j + i])
                
    print(max)


if __name__ == "__main__":
    main()
