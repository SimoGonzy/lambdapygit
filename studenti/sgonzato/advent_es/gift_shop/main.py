'''
Questo file è lo scheletro per risolvere la prima parte del giorno 2 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/2).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in una lista di tuple con due valori, dove:
    - il primo rappresenta l'ID di inizio intervallo;
    - il secondo rappresenta l'ID di fine intervallo.
'''


from parser import parse_exercise


def main():
    id_ranges: list[tuple[int, int]] = parse_exercise("./demo2.txt")

    # TODO: Implementare la soluzione utilizzando i range di ID contenuti in `id_ranges`
    
    '''
    # PARTE 1 FUNZIONANTE!
    somma = 0
    
    for j in range(0, len(id_ranges)):
        for i in range(id_ranges[j][0], id_ranges[j][1] + 1):
            id = str(i)
            if (len(id) % 2 == 0):
                metà = int(len(id) / 2)
                a = id[0:metà]
                b = id[metà:]
                
                if (a == b):
                    somma += int(id)
    
    print("\nTutti ID sommati: " + str(somma))
    
    '''
    
    '''
    # PARTE 2 NON FUNZIONANTE!
    somma = 0
    
    for i in range(0, len(id_ranges)):
        for j in range(id_ranges[i][0], id_ranges[i][1] + 1):
            id = str(j)
            if (len(id) % 2 == 0):
                metà = int(len(id) / 2)
                a = id[0:metà]
                b = id[metà:]
                
                if (a == b):
                    print("ID valido trovato: " + id)   
                    somma += int(id)
            else:
                uguali = True
                for k in range(len(id) - 1):
                    if id[k] != id[k+1]:
                        uguali = False
                        break
                if uguali:
                    print("ID valido trovato: " + id)   
                    somma += int(id)
            
    print(somma)
    '''

if __name__ == "__main__":
    main()