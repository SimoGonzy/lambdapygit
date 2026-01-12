'''
Questo file è lo scheletro per risolvere la prima parte del giorno 2 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/2).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di tuple con due valori, dove:
    - il primo rappresenta l'ID di inizio intervallo;
    - il secondo rappresenta l'ID di fine intervallo.
'''


from parser import parse_exercise


def main():
    id_ranges: list[tuple[int, int]] = parse_exercise("./mio.txt")

    count = 0

    for pos in range (len(id_ranges)):
        for num in range(id_ranges[pos][0], id_ranges[pos][1]+1):
            s=str(num)
            lunghezza=len(s)
            punto_medio=lunghezza//2
            prima_meta=s[:punto_medio]
            seconda_meta=s[punto_medio:]
            if(prima_meta==seconda_meta):
                count = count+num

    print(count)


if __name__ == "__main__":
    main()
