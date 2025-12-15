
from parser import parse_exercise


def main():
    banks: list[str] = parse_exercise("./demo.txt")
    somma = 0
    posizione = 0
    # TODO: Implementare la soluzione utilizzando i banchi contenuti in `banks`

    for bank in banks:
        m = 0
        m2 = 0
        posizione = 0
        for num in range(0, len(bank)):
            if int(bank[num]) > m:
                posizione += 1
                m = int(bank[num])
            if posizione == len(bank) - 1 :
                posizione = 0
            print(posizione)
            input()
        for num in range(posizione, len(bank)):
            print(f"posizione: {posizione}")
            if int(bank[num]) > m2:
                m2 = int(bank[num])

            #print(f"Massimo: {m} Secondo massimo: {m2}")
            #input()


        somma = str(m) + str(m2)
        print(f"Somma: {somma}")
        input()

if __name__ == "__main__":
    main()