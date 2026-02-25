caffe: float = 1.20
cappuccino: float = 1.60
orzo: float = 1.40
the: float = 1.50

print("Menù")
print(f"Caffè {caffe} euro")
print(f"Cappuccino {cappuccino} euro")
print(f"Orzo {orzo} euro")
print(f"The {the} euro")

somma: float = 0


while True:
    print("Cosa vuole ordinare?")
    risposta: str = input()
    if risposta == "caffè":
        print(caffe)
        somma = somma + 1.20
    elif risposta == "Caffè":
        print(caffe)
        somma += 1.20
    elif risposta == "cappuccino":
        print(cappuccino)
        somma += 1.60
    elif risposta == "Cappuccino":
        print(cappuccino)
        somma += 1.60
    elif risposta == "orzo":
        print(orzo)
        somma += 1.40
    elif risposta == "Orzo":
        print(orzo)
        somma += 1.40
    elif risposta == "the":
        print(the)
        somma += 1.50
    elif risposta == "The":
        print(the)
        somma += 1.50
    elif risposta == "stop":
        break

print(f"Il tuo totale è {somma} euro")
