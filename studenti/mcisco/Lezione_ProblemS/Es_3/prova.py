
from parser import parse_exercise


def main():
    banks: list[str] = parse_exercise("./demo.txt")
    # TODO: Implementare la soluzione utilizzando i banchi contenuti in `banks`

    prova = banks.split()
    print(prova)
 
if __name__ == "__main__":
    main()