"""Sviluppare un piccolo gestionale che consenta di memorizzare i
prodotti in catalogo. Il programma deve permettere di:
• Mostrare un prodotto con nome, prezzo e categoria; +10exp
• Rimuovere un prodotto dato il nome; +10exp
• Aggiungere un nuovo prodotto; +20exp
• Filtrare i prodotti per prezzo o categoria; +30exp
• Trovare il prodotto più costoso o più economico; """
catalogo : list[dict[str, float | str]] = []
pane : dict[str, float | str] = {"nome" : "pane", "prezzo" : 2.5, "categoria" :"alimentari"}
catalogo.append(pane)
print(catalogo)
zaino : dict [str, float | str]={"nome" : "zaino", "prezzo" : 10.0, "categoria": "scuola"}
catalogo.append(zaino)
caramella : dict [str, float | str]={"nome" : "caramella", "prezzo" : 0.20, "categoria": "alimentari"}
catalogo.append(caramella)
"""for n in range(0,len(catalogo)) :
    if "zaino" == catalogo[n]["nome"] :
        print(catalogo.pop(n))"""

for n in range(0, len(catalogo)):
    if catalogo[n]["prezzo"]<10.0:
        print(catalogo[n])

for n in range(0, len(catalogo)):
    if catalogo[n]["categoria"]=="alimentari":
        print(catalogo[n])

maggiore : dict[str, str | float] = catalogo[0]
for n in range(1, len(catalogo)):
    
    if maggiore["prezzo"] <= catalogo[n]["prezzo"]:
        maggiore = catalogo[n]
print("l'articolo con il preezzo piu alto è")    

print(maggiore)

minore : dict = catalogo[0]

for n in range(1, len(catalogo)):
    
    if minore["prezzo"] >= catalogo[n]["prezzo"]:
        minore = catalogo[n]
print("l'articolo con il preezzo piu basso è")    
print( minore)
        
