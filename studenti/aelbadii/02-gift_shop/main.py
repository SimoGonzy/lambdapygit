'''
Questo file è lo scheletro per risolvere la prima parte del giorno 2 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/2).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di tuple con due valori, dove:
    - il primo rappresenta l'ID di inizio intervallo;
    - il secondo rappresenta l'ID di fine intervallo.
'''


from parser import parse_exercise


def main():
    id_ranges: list[tuple[int, int]] = parse_exercise("./demo1.txt")
    count=0

    for num in range (len(id_ranges)):
        for val in range(id_ranges[num][0],id_ranges[num][1]+1):
            s=str(val)
            lunghezza=len(s)
            punto_medio=lunghezza//2
            prima_meta=s[:punto_medio]
            secondo_meta=s[punto_medio:]
            if(prima_meta==secondo_meta):
                count=count+val

    print(count)  
    # TODO: Implementare la soluzione utilizzando i range di ID contenuti in `id_ranges`


if __name__ == "__main__":
    main()
