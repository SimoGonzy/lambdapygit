import random

def coin_flip_game():

    balance = 10000
    history = []
    total_wager = 0

    while balance > 0:
        print("\n--- Testa o Croce ---")
        print(f"Saldo: €{balance}")

        # Input puntata
        while True:
            try:
                bet = float(input("Inserisci importo puntata (0 per uscire): € "))
                if bet == 0:
                    for i, (puntata, result, winnings) in enumerate(history):
                        print(f" Gioco: {i+1}, Scommessa: {puntata}, Risultato: {result}, Puntata: €{winnings}")
                    print(f"Totale puntato: €{total_wager}")
                    print(f"Saldo Finale: €{balance}")
                    return
                if bet > balance:
                    print("Inserisci una puntata di importo minore")
                else:
                    break
            except ValueError:
                print("Puntata non accettata. Inserisci un numero")

        while True:
            try:
                puntata = str(input("Scegli la scommessa. Testa o Croce: "))
                if puntata == "Testa":
                    print("Hai scelto Testa")
                    break
                elif puntata == "Croce":
                    print("Hai scelto Croce")
                    break
                else:
                    print("Puntata non valida. Inserisci Testa o Croce")

            except ValueError:
                print("Inserisci la scommessa: Testa o Croce")

        # Coin flip
        result = random.choice(["Testa", "Croce"])
        print(f"È uscita: {result}")

        # Messaggio risultato
        if result == puntata:
            winnings = bet
            print("Hai vinto!")
        else:
            winnings = -bet
            print("Hai perso!")

        # Nuovo saldo
        balance += winnings
        print(f"Saldo dopo puntata: €{balance}")
        total_wager += bet

        history.append((puntata, result, bet))
    print("\n--- Game Over! ---")
    print(f"Totale puntato: €{total_wager}")
    print("Storico Giocate:")
    for i, (puntata, result, winnings) in enumerate(history):
        print(f" Gioco: {i + 1}, Scommessa: {puntata}, Risultato: {result}, Puntata: €{winnings}")

if __name__ == "__main__":
    coin_flip_game()
