from functools import reduce

"""
Dato l’elenco nums = [10, 15, 20, 25, 30], estrai solo i
numeri maggiori di 20.
• Dato l’elenco words = ["ciao", "python", "lambda", "hi",
"fun"], ottieni la lista delle lunghezze di ogni parola.
• Dato l’elenco words = ["anna", "bob", "carla", "daniele",
"eve"], estrai solo le parole che iniziano con la lettera “a”.
• Dato l’elenco nums = [2, 3, 5, 7, 11], calcola il prodotto di
tutti i numeri.
"""

#1
nums = [10, 15, 20, 25, 30]
filtered_nums = list(filter(lambda x: x > 20, nums))
print("1) Numeri maggiori di 20: " + str(filtered_nums))

#2
words = ["ciao", "python", "lambda", "hi", "fun"]
lunghezze = list(map(lambda x: len(x), words))
print("2) Lista lunghezze parole: " + str(lunghezze))

#3
words2 = ["anna", "bob", "carla", "daniele", "eve"]
a = list(filter(lambda x: x.find("a") == 0, words))
print("3) Iniziali con a: " + str(a))

#4
nums = [2, 3, 5, 7, 11]
product = reduce(lambda x,y: x*y, nums)
print("4) Prodotti: " + str(product))