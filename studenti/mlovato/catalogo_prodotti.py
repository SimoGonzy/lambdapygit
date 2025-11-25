"""
3. 📋 Catalogo Prodotti ⋆⋆⋆
Sviluppare un piccolo gestionale che consenta di memorizzare i
prodotti in catalogo. Il programma deve permettere di:
• Mostrare un prodotto con nome, prezzo e categoria; +10exp
• Rimuovere un prodotto dato il nome; +10exp
• Aggiungere un nuovo prodotto; +20exp
• Filtrare i prodotti per prezzo o categoria; +30exp
• Trovare il prodotto più costoso o più economico; +30exp
Strutture Dati: Liste, Tuple e Dizionari - Python: da Zero a OOP - Riccardo Sacchetto, B.Sc.
"""

prodotto: dict[str, str | int]

catalogo: list[dict[str, str | int]] = []

scelta: str = "inizio"

while scelta != "esci":
    print("Puoi scegliere cosa fare: ")
    print("1 - Mostra un prodotto dato il nome")
    print("2 - Rimuovi un prodotto dato il nome")
    print("3 - Aggiungi un prodotto")
    print("4 - Filtra i prodotti in base a prezzo o categoria")
    print("5 - Trova il prodotto più costoso/economico")
    print("esci")
    print("")

    scelta = input("Fai la tua scelta: ")
    print("---------------")

    if scelta == "1":
        print("Lista di tutti i prodotti: ")
        for prodotto in catalogo:
            print(f"Nome: {prodotto['nome']}")
            print(f"Categoria: {prodotto['categoria']}")
            print(f"Prezzo: {prodotto['prezzo']}")
            print("---------------")
    elif scelta == "2":
        print("Rimuovere un prodotto: ")
        nome: str = input("Il nome del prodotto da rimuovere?: ")

        for prodotto in catalogo:
            if prodotto["nome"] == nome:
                catalogo.remove(prodotto)

    elif scelta == "3":
        prodotto = {}
        print("Aggiungi un nuovo elemento")
        prodotto["nome"] = input("Inserisci il nome del prodotto: ")
        prodotto["categoria"] = input("Inserisci una categoria: ")

        prezzo_str: str = input("Prezzo: ")
        while not(prezzo_str.isnumeric()):
            prezzo_str = input("Il prezzo deve essere un numero: ")
        prodotto["prezzo"] = int(prezzo_str)
        catalogo.append(prodotto)
        print("---------------")
    elif scelta == "4":
        scelta_categoria_prezzo = input("Filtra per categoria o prezzo? ")
        while not (
            scelta_categoria_prezzo == "categoria"
            or scelta_categoria_prezzo == "prezzo"
        ):
            scelta_categoria_prezzo = input("Filtra per categoria o prezzo? ")
        if scelta_categoria_prezzo == "categoria":
            categoria: str = input("Che categoria? ")
            print("categoria")
            for prodotto in catalogo:
                if prodotto["categoria"] == categoria:
                    print(f"Nome: {prodotto['nome']}")
                    print(f"Categoria: {prodotto['categoria']}")
                    print(f"Prezzo: {prodotto['prezzo']}")
                    print("---------------")
        if scelta_categoria_prezzo == "prezzo":
            prezzo_str: str = input("Che prezzo? ")
            while not (prezzo_str.isnumeric()):
                prezzo_str = input("Il prezzo deve essere un numero! ")
            prezzo: int = int(prezzo_str)
            for prodotto in catalogo:
                if prodotto["prezzo"] == prezzo:
                    print(f"Nome: {prodotto['nome']}")
                    print(f"Categoria: {prodotto['categoria']}")
                    print(f"Prezzo: {prodotto['prezzo']}")
                    print("---------------")
    elif scelta == "5":
        scelta_costoso_economico: str = input(
            "Vuoi vedere il prodotto più costoso o più economico? "
        )
        while not (
            scelta_costoso_economico == "costoso"
            or scelta_costoso_economico == "economico"
        ):
            scelta_costoso_economico = input(
                "Le scelte possibili sono costoso o economico: "
            )
        if scelta_costoso_economico == "costoso":
            prezzo_piu_costoso = 0
            for prodotto in catalogo:
                prezzo_prodotto: int = int(prodotto["prezzo"])
                if prezzo_prodotto > prezzo_piu_costoso:
                    prezzo_piu_costoso = int(prodotto["prezzo"])
            for prodotto in catalogo:
                if prodotto["prezzo"] == prezzo_piu_costoso:
                    print(f"Nome: {prodotto['nome']}")
                    print(f"Categoria: {prodotto['categoria']}")
                    print(f"Prezzo: {prodotto['prezzo']}")
                    print("---------------")
        if scelta_costoso_economico == "economico":
            prezzo_piu_economico: int = int(catalogo[0]["prezzo"])
            for prodotto in catalogo:
                prezzo_prodotto: int = int(prodotto["prezzo"])
                if prezzo_prodotto < prezzo_piu_economico:
                    prezzo_piu_economico = int(prodotto["prezzo"])
            for prodotto in catalogo:
                if prodotto["prezzo"] == prezzo_piu_economico:
                    print(f"Nome: {prodotto['nome']}")
                    print(f"Categoria: {prodotto['categoria']}")
                    print(f"Prezzo: {prodotto['prezzo']}")
                    print("---------------")
    elif scelta == "esci":
        print("Uscita in corso...")
    else:
        print("Scelta non gestita")
