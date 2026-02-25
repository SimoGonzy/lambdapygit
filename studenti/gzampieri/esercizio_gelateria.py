menu = {
        "cioccolato":  2.0,
        "vaniglia": 3.0,
        "fragola": 3.50,
        "amarena": 2
}
totale = 0

print("ecco il nostro menu")
for prodotti,prezzo in menu.items():
    print(f"{prodotti} {prezzo}£")

while True:
    scelta = input("scegli che gusto vuoi: 'premi STOP per fermare lordine'")

    if scelta == "stop":
        break
    if scelta in menu:
        totale = totale + menu[scelta]
        print(f"hai aggiunto {scelta} il totale provvisorio e'{totale}" )
    else: print("gusto non accettato")

print(f"il tuo totale e' {totale}")
