prodotti = ["PC da Gaming", "Monitor 4K", "Tavolo in legno"]

prezzi: dict[str, float] = {
    "PC da Gaming": 599,
    "Monitor 4K": 299,
    "Tavolo in legno": 10000
}

categorie: dict[str, str] = {
    "PC da Gaming": "Tecnologia",
    "Monitor 4K": "Tecnologia",
    "Tavolo in legno": "Arredamento"
}
 
r=""
while(r!="q"):
    print("\nProdotti:", prodotti)
    r = input("Digita show, rm, add per mostrare, rimuovere o aggiungere un prodotto, oppure filter per filtrare i prodotti.\nAltrimenti digita q per uscire: ")
    if(r=="show"):
        p = input("Quale prodotto vuoi mostrare? ")
        print(p, f"| Prezzo: {prezzi.get(p)}€", f"| Categoria: {categorie.get(p)}")
    elif(r=="rm"):
        p = input("Quale prodotto vuoi rimuovere? ")
        prodotti.remove(p)
        print("Rimosso il prodotto:", p)
    elif(r=="add"):
        p = input("Quale prodotto vuoi aggiungere? ")
        prodotti.append(p)
        prezzo = eval(input("Inserisci il prezzo del prodotto: "))
        categoria = input("Inserisci la categoria del prodotto: ")
        prezzi.update({p:prezzo})
        categorie.update({p:categoria})
        print("Aggiunto il prodotto:", p)
    elif(r=="filter"):

        # filtro categoria
        c = input("Inserisci la categoria da filtrare: ")
        for i in range(len(prodotti)):
            if(categorie.get(prodotti[i]) == c):
               print(prodotti[i], f"| Prezzo: {prezzi.get(prodotti[i])}€", f"| Categoria: {categorie.get(prodotti[i])}")

        # minimo e massimo prezzo
        max = prezzi.get(prodotti[0])
        min = prezzi.get(prodotti[0])
        pmax = ""
        pmin = ""
        for i in range(len(prodotti)-1):
            if(prezzi.get(prodotti[i+1])>max):
                max = prezzi.get(prodotti[i+1])
                pmax = prodotti[i+1]
            if(prezzi.get(prodotti[i+1])<min):
                min = prezzi.get(prodotti[i+1])
                pmin = prodotti[i+1]
        print(f"Il prodotto più costoso è {pmax}", f"| Prezzo: {max}€", f"| Categoria: {categorie.get(pmax)}")
        print(f"Il prodotto meno costoso è {pmin}", f"| Prezzo: {min}€", f"| Categoria: {categorie.get(pmin)}")