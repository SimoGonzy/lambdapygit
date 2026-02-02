'''
Questo file è lo scheletro per risolvere la prima parte del giorno 3 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/3).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di stringhe, ciascuna rappresentante un banco di batterie.
'''


from parser import parse_exercise


def main():
    banks: list[str] = parse_exercise("./demo.txt")
    nmax=0
    nmax2=0
    n:str=0
    tot=0
    for bank in banks:
        for num in bank:
            if(nmax<int(num)):
                nmax=nmax+int(num)
            if(nmax2>nmax and nmax2<int(num)):
                nmax2=nmax2+int(num)

        n=str(nmax)+str(nmax2)
        tot=tot+int(n)

        
            
    print(tot)

    # TODO: Implementare la soluzione utilizzando i banchi contenuti in `banks`


if __name__ == "__main__":
    main()
