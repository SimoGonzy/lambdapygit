#lista globale contenenti tutti i prodotti
prodotti: list[tuple] = [ 
    ("Acqua", 1.50, "Bevande"),                     
    ("Pane", 2.00, "Alimentari"),
    ("Latte", 1.30, "Alimentari"),
    ("Caffè", 4.50, "Bevande"),
    ("Pasta", 1.20, "Alimentari"),
    ("Biscotti", 2.80, "Snack"),
    ("Succo di frutta", 2.10, "Bevande"),
    ("Cioccolato", 1.90, "Dolci"),
    ("Detersivo", 3.70, "Casa"),
    ("Shampoo", 2.60, "Igiene"),
    ("Sapone", 1.00, "Igiene"),
    ("Riso", 1.90, "Alimentari"),
    ("Tonno", 3.20, "Alimentari"),
    ("Patatine", 1.80, "Snack"),
    ("Aranciata", 1.70, "Bevande"),
    ("Formaggio", 3.40, "Alimentari"),
    ("Tovaglioli", 1.10, "Casa"),
    ("Burro", 2.50, "Alimentari"),
    ("Yogurt", 1.40, "Alimentari"),
    ("Succhero", 1.20, "Alimentari")
]

scelta = ""

def visualizza_prodotti(prodotti):
    print("\nNOME   ---   PREZZO   ---   CATEGORIA\n")
    for i in range(0,len(prodotti)):
        print(f"{prodotti[i][0]} - {prodotti[i][1]}$ - {prodotti[i][2]}")

while scelta != 0:
    print("\n--- MENU ---")
    print("1. Visualizza prodotti")
    print("2. Rimuovi un prodotto")
    print("3. Aggiungi un prodotto")
    print("4. Filtra prodotto per prezzo o categoria")
    print("5. Costoso o economico?")
    print("0. Esci dal programma\n")
    
    scelta_raw = int(input())
    try:
        scelta = int(scelta_raw)
    except ValueError:
        print("\nInserisci un numero valido.\n")
        continue
    
    if scelta == 1:
        
        print("\n--- LISTA PRODOTTI ---")
        visualizza_prodotti(prodotti)
        print("\n")
        
    elif scelta == 2:
        
        print("\nChe prodotto vuoi rimuovere? (nome)")
        pr = input()
        
        for i in range(0,len(prodotti)):
            if prodotti[i][0] == pr:
                pr: tuple[str, float, str] = prodotti[i]
                break
        
        prodotti.remove(pr)
        
        print(f"Prodotto '{pr}' rimosso.\n")
        
    elif scelta == 3:
        
        print("\nInserisci il nome del prodotto che vuoi aggiungere")
        nome = input("Nome: ")
        print("\nInserisci il prezzo del prodotto")
        prezzo = float(input("Prezzo: "))
        print("\nInserisci la categoria del prodotto")
        cat = input("Categoria: ")
        
        prodotti.append((nome,prezzo,cat))
        
        print(f"Prodotto '{nome}' aggiunto.\n")
        
    elif scelta == 4:
        print("Vuoi filtrare per prezzo o categoria?")
        
        inpt = int(input("\n1. Prezzo\n2. Categoria\n"))
        if inpt == 1:
            min = float(input("Inserisci un prezzo minimo: "))
            max = float(input("Inserisci il prezzo massimo: "))
            
            print("\nI prodotti in questo range sono: ")
            
            for i in range(0, len(prodotti)):
                if prodotti[i][1] > min and prodotti[i][1] < max:
                    print(f"{prodotti[i][0]} - {prodotti[i][1]}$ - {prodotti[i][2]}")
        elif inpt == 2:
            nome = input("Inserisci un nome per la categoria: ")    
            print("\nI prodotti in questa categoria sono: ")
            
            for i in range(0, len(prodotti)):
                if prodotti[i][2] == nome:
                    print(f"{prodotti[i][0]} - {prodotti[i][1]}$ - {prodotti[i][2]}")  
        else:
            print("\nError!!!")
        
    elif scelta == 5:
        
        max = prodotti[0][1]
        min = prodotti[0][1]
        
        for i in range(0, len(prodotti)):
            if prodotti[i][1] > max:
                pr_costoso = prodotti[i][0]
                max = prodotti[i][1]
            elif prodotti[i][1] < min:
                pr_eco = prodotti[i][0]
                min = prodotti[i][1]
                
        print(f"Prodotto più costoso: {pr_costoso} {max}\nProdotto più economico: {pr_eco} {min}")
        
    elif scelta == 0:
        print("\nGrazie per aver usato il nostro programma!")
        
        # resettiamo il catalogo dell'utente
        prodotti: list[tuple] = [ ]
        
        # usciamo dal programma
        exit()